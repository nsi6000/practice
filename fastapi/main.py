from contextlib import asynccontextmanager, contextmanager
import os
from pathlib import Path
import sqlite3
from typing import Iterator

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
import uvicorn

DB_PATH = Path(os.getenv("SQLITE_DB_PATH", "./app.db"))


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="SQLite CRUD API", lifespan=lifespan)


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    done: bool = False


class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    done: bool | None = None


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
    done: bool
    created_at: str


def row_to_item(row: sqlite3.Row) -> ItemResponse:
    return ItemResponse(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        done=bool(row["done"]),
        created_at=row["created_at"],
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "db_path": str(DB_PATH)}


@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> ItemResponse:
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO items (name, description, done) VALUES (?, ?, ?)",
            (payload.name, payload.description, int(payload.done)),
        )
        row = conn.execute(
            "SELECT * FROM items WHERE id = ?", (cur.lastrowid,)
        ).fetchone()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to load created item",
        )
    return row_to_item(row)


@app.get("/items", response_model=list[ItemResponse])
def list_items() -> list[ItemResponse]:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM items ORDER BY id DESC").fetchall()
    return [row_to_item(r) for r in rows]


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return row_to_item(row)


@app.patch("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, payload: ItemUpdate) -> ItemResponse:
    updates = payload.model_dump(exclude_unset=True)
    with get_connection() as conn:
        existing = conn.execute(
            "SELECT * FROM items WHERE id = ?", (item_id,)
        ).fetchone()
        if existing is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
            )

        if updates:
            if "done" in updates and updates["done"] is not None:
                updates["done"] = int(updates["done"])
            set_clause = ", ".join(f"{col} = ?" for col in updates)
            params = [*updates.values(), item_id]
            conn.execute(f"UPDATE items SET {set_clause} WHERE id = ?", params)

        row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return row_to_item(row)


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    if cur.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8080")),
        reload=True,
    )

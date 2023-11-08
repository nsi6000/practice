# Go

```bash
apt-get install golang
apt-get install golang-golang-x-tools //for godoc.
go run app.go
go doc fmt.Println
```
```go
package main

import "fmt"

func main() {
  fmt.Println("Hello.")

  var age int = 42
  var name string = "Alice"
  var isTrue bool = true
  const pi float64 = 3.1416
  fmt.Println(len(name), age, pi)
  fmt.Println("%T \n", pi)
  fmt.Println(true && false)
  fmt.Println(true || false)
  fmt.Println(!true)
  // == != < > <= >=

  for i := 0; i < 10; i++ {
    fmt.Println(i)
  }

  a := 2
  if a == 2 {
    fmt.Println("A")
  } else if a == 1 {
    fmt.Println("B")
  } else {
    fmt.Println("C")
  }

  switch a {
    case 2: fmt.Println("A")
    case 1: fmt.Println("B")
    default: fmt.Println("C")
  }
}
```

from prefect import task, Flow


@task
def say_hello():
    print("Hello World.")

with Flow("Flow 1") as flow:
    say_hello()


flow.run()



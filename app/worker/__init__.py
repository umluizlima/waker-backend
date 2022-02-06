import random
import sys
import time

from procrastinate import AiopgConnector, App

app = App(
    connector=AiopgConnector(host="localhost", user="postgres", password="postgres")
)
app.open()


@app.task(name="sum")
def sum(a, b):
    time.sleep(random.random() * 5)  # Sleep up to 5 seconds
    return a + b


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"Scheduling computation of {a} + {b}")
    sum.defer(a=a, b=b)  # This is the line that launches a job

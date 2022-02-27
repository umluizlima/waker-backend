import sys

from app.core.tasks import sum

a = int(sys.argv[1])
b = int(sys.argv[2])
print(f"Scheduling computation of {a} + {b}")
sum.defer(a=a, b=b)  # This is the line that launches a job

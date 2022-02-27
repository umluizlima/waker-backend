import random
import time

from procrastinate import Blueprint

blueprint = Blueprint()


@blueprint.task
def sum(a, b):
    time.sleep(random.random() * 5)  # Sleep up to 5 seconds
    return a + b

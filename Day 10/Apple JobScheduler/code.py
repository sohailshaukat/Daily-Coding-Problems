#! python3
import time


def jobScheduler(func, period):
    for _ in range(10):                 #this could be just while True: but i didn't want to fill up your cli
        func()
        time.sleep(period/1000)


def func():
    print("Funky")


jobScheduler(func, 4)

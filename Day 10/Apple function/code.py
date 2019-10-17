#! python3
import time


def jobScheduler(func, period):
    for _ in range(10):
        func()
        time.sleep(period/1000)


def func():
    print("Funky")


jobScheduler(func, 4)

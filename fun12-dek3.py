import time
import numpy as np  # zaimportujemy jako alias np


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonannia funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_wait():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print('Sum is:', total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print('Sum is:', total)


my_wait()  # Czas wykonannia funkcji my_wait: 2.001020669937134
my_for_sum()  # Czas wykonannia funkcji my_for_sum: 0.7409107685089111
my_sum_without_for()  # Czas wykonannia funkcji my_sum_without_for: 0.5870065689086914
my_sum_np()  # Czas wykonannia funkcji my_sum_np: 0.047003746032714844

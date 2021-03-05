import math
import time
from numba import njit, prange


@njit(fastmath=True, cache=True)
def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
        return True


@njit(fastmath=True, cache=True, parallel=True)
def run_program(N):
    for i in prange(N):
        is_prime(i)


if __name__ == "__main__":
    N = 10000000
    start = time.perf_counter()
    run_program(N)
    end = time.perf_counter()
    print(end - start)

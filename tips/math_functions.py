import math
import time
from numba import njit, prange


@njit(fastmath=True, cache=True)
def is_prime(num: int) -> bool:
    """
    To determine the input integer is prime or not

    Args:
        num: an input integer

    Returns:
        bool (True/False)
    """
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
        return True


@njit(fastmath=True, cache=True, parallel=True)
def run_program(N: int):
    """
    To check each integer is prime or not in range(N) by loop
    """
    for i in prange(N):
        is_prime(i)


if __name__ == "__main__":
    N = 10000000
    start = time.perf_counter()
    run_program(N)
    end = time.perf_counter()
    print(end - start)

"""
提供質因數分解的函數
"""
from typing import Tuple, List, Dict
from IPython.display import display, Latex

import numpy as np


def is_prime(x: int) -> bool:
    """判斷輸入的數字是否為質數"""
    if x <= 0:
        print('please input a positive integer !')
        return False
    if x == 1:
        return False
    x_factors = [i for i in range(2, int(np.sqrt(x) + 1)) if x % i == 0]
    if len(x_factors) == 0:
        return True
    return False


def get_order_of_divisor(number: int, divisor: int) -> Tuple[int]:
    """
    計算出一個除數 (divisor) 在一個數字 (number) 中
    最多可以被它 (divisor) 的幾次方整除；
    並且回傳整除時的商 (quotient)
    """
    remainder = 0
    order = 0
    quotient = number
    while remainder == 0:
        remainder = quotient % divisor
        if remainder == 0:
            order += 1
            quotient = quotient // divisor
    return order, quotient


def get_prime_factor_list(number: int) -> List[str]:
    """
    取得數字的所有質因數
    """
    prime_factor_list = []
    if number <= 1:
        return prime_factor_list
    for i in range(2, int(np.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            prime_factor_list.append(i)
            quotient = number // i
            if is_prime(quotient):
                prime_factor_list.append(quotient)
            number = quotient
    return prime_factor_list


def get_prime_factor_order_dict(number: int) -> Dict[int, int]:
    """
    將一數字做質因數分解，以 dictionary 表示，格式為
    {
        prime_factor_1: order_1,
        prime_factor_2: order_2,
        ...
    }
    """
    if is_prime(number):
        return {
            number: 1
        }
    prime_factor_list = get_prime_factor_list(number)
    prime_factor_order_dict = {}
    for prime_factor in prime_factor_list:
        order, number = get_order_of_divisor(number, prime_factor)
        if order:
            prime_factor_order_dict[prime_factor] = order
    return prime_factor_order_dict


def display_prime_factorization(number: int):
    """
    展示出數字的直因數分解，以 Latex 的方式顯示
    """
    number_list = []
    prime_factor_order_dict = get_prime_factor_order_dict(number)
    for prime_factor, order in prime_factor_order_dict.items():
        number_list.append(f"{prime_factor}^{order}")
    prime_factor_string = "\\times".join(number_list)
    display(Latex(f'${prime_factor_string}$'))


def get_prime_factorization_password(number: int) -> str:
    """
    根據數字的直因數分解，由小到大組合成新的密碼
    Example:
        10 = 2 * 5
        新密碼為 '25'
    """
    prime_factor_order_dict = get_prime_factor_order_dict(number)
    suggest_password = ""
    for prime_factor, order in prime_factor_order_dict.items():
        suggest_password += str(prime_factor) * order
    return suggest_password

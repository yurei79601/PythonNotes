NUMBER_ELEMENT_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
NUMBER_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def filter_integer(number_string):
    if number_string.startswith('+'):
        if number_string[1:].isnumeric():
            return int(number_string[1:])
        return 0
    if number_string.startswith('-'):
        if number_string[1:].isnumeric():
            return -int(number_string[1:])
        return 0
    return int(number_string)


def my_atoi(a_string):
    if a_string.startswith(' '):
        a_string = a_string.strip()

    if not a_string:
        return 0

    number_string = ''
    for i in range(len(a_string)):
        if a_string[i] in NUMBER_ELEMENT_LIST:
            number_string += a_string[i]
            j = 1
            while i + j < len(a_string):
                if a_string[i + j] in NUMBER_LIST:
                    number_string += a_string[i + j]
                    j += 1
                else:
                    break
            break
        else:
            return 0
    print(number_string)
    number = filter_integer(number_string)
    if number >= (2 ** 31 - 1):
        return 2 ** 31 - 1
    if number <= -(2 ** 31):
        return -((2 ** 31))
    return number


class Solution:
    def myAtoi(self, s: str) -> int:
        return my_atoi(s)

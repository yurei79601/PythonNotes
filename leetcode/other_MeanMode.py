"""
判斷一個 list 的平均數是否等於這個 list 的眾數
"""


def get_mode(a_list: list) -> int:
    """
    Find the mode of the input list
    """
    if not a_list:
        return 0

    a_dict = {}

    for x in a_list:
        if x not in a_dict.keys():
            a_dict[x] = 1
        else:
            a_dict[x] += 1

    max_value = max(a_dict.keys())
    mode_list = []

    for k, v in a_dict.items():
        if v == max_value:
            mode_list.append(k)
    if len(mode_list) == 1:
        return mode_list[0]
    return 0


def MeanMode(a_list: int) -> bool:
    """
    check mean of input list is equal to mode of input list
    """
    if min(a_list) < 0:
        return 0

    mode = get_mode(a_list)
    if mode == 0:
        return 0

    _mean = sum(a_list) / len(a_list)
    return _mean == mode

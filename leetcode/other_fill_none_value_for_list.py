def fill_none_value_for_list(a_list: list) -> list:
    """
    fill None value in input list by closest index non-empty value

    Example:
        input: [None, 1, 2, 3, None, 4, None, None]
        output: [1, 1, 2, 3, 3, 4, 4, 4]
    """
    for i, a in enumerate(a_list):
        if a is None:
            if i == 0:
                a_list[i] = a_list[i + 1]
            else:
                a_list[i] = a_list[i - 1]
    return a_list
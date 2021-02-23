"""
some interesting functions built by yurei

1. df_to_markdown
2. time_calculator
"""
import pandas as pd


def get_markdown_table_delimiter(df: pd.DataFrame) -> str:
    """
    To get markdown table delimiter according to
    number of columns of input dataframe

    Args:
        df: input table of dataframe

    Returns:
        string of delimiters

    Example:
        |||
    """
    delimiter_list = ['|'] * (df.shape[1]+1)
    return '-'.join(delimiter_list)



def get_markdown_table_initial_string(df: pd.DataFrame)\
    -> str:
    """
    To get the initial string of table in markdown

    Args:
        df: input table of dataframe

    Returns:
        string of head table in markdown
    """
    initial_string = ''
    initial_string += get_markdown_table_values(df.columns) + '\n' + \
                      get_markdown_table_delimiter(df) + '\n'
    return initial_string


def get_markdown_table_values(a_list: list) -> str:
    """
    Transform row value to markdown string
    to represent a row of table

    Args:
        a_list: a list of a row of some dataframe

    Returns:
        a string of row value in markdown

    Example:
        |a|b|c|
    """
    return '|' + '|'.join(a_list) + '|'


def df_to_markdown(df: pd.DataFrame) -> str:
    """
    To get the whole markdown string of input dataframe

    Args:
        df: input table of dataframe

    Returns:
        To get the whole markdown string to represent a table
    """
    df = df.astype(str)
    s = get_markdown_table_initial_string(df)
    for i in range(df.shape[0]):
        s += get_markdown_table_values(list(df.loc[i, :])) + '\n'
    return s


def time_calculator(function):
    def wrap(*args, **kwargs):
        start = time.time()
        output = function(*args, **kwargs)
        end = time.time()
        print('{} cost {} seconds'.format(function.__name__, end-start))
        return output
    return wrap
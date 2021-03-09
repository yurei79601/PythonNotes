"""
some interesting functions built by yurei

1. df_to_markdown
2. time_calculator
3. market_value_after_exclude_dividend_right
"""
import time
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


def get_stock_earned_after_exclude_right(shares: int, stock_dividends: float) -> float:
    """
    取得經過除權後，會得到有多少股

    Args:
        shares: 股數
        stock_dividends: 股利

    Returns:
        除權後的所獲的股數
    """
    return (shares * stock_dividends)/10


def get_cash_earned_after_exclude_dividend(shares: int, cash_dividends: float) -> float:
    """
    經過除息後，會得到多少現金股息

    Args:
        shares: 股數
        cash_dividends: 股息

    Returns:
        除權後所得到個現金股息
    """
    return shares * cash_dividends


def market_value_after_exclude_dividend_right(shares: int,
                                              stock_dividends: float,
                                              cash_dividends: float,
                                              market_value_per_share: float
                                             ) -> float:
    """
    根據現在的股數、股價以及配股配息的數量，計算之後會有多少總資產

    Args:
        shares: 股數
        stock_dividends: 股利
        cash_dividends: 股息
        market_value_share: 股票現值

    Returns:
        除權息後的資產總量
    """
    stock_earned = get_stock_earned_after_exclude_right(shares, stock_dividends)
    cash_earned = get_cash_earned_after_exclude_dividend(shares, cash_dividends)
    return (shares + stock_earned) * market_value_per_share + cash_earned


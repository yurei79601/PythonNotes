"""
Zigzag Conversion: 曲折字串轉換。根據曲折的高度，轉換字串的排序。
例如 numRows = 3, s = 'PAYPALISHIRING'
[step: 1]
P   A   H   N
A P L S I I G
Y   I   R

[step: 2]
第一排組起來, 第二排組起來, ...，會得到 'PAHNAPLSIIGYIR'

[我的解題想法]
* numRows = 3
將字串裡面的字母，依序以序號代替，所以上限的 zigzag 就會變成
0   4   9     13 -> (除 4 餘 0)
1 3 5 8 10 12 14 -> (除 4 餘 1, -1)
2   6   11       -> (除 4 餘 2)
為什麼是除 4，因為 4 = 2 * 3 - 2

* numRows = 4
這個例子可能會更明顯，以下看一下 zigzag
0    6       12 -> (除 6 餘 0) -> (第 0 排的餘數邏輯，餘數為 0)
1  5 7    11 13 -> (除 6 餘 1, -1) -> (中間第 j 排，餘數 j, -j)
2 4  8 10    14 -> (除 6 餘 2, -2)
3    9       15 -> (除 6 餘 3) -> (最後一排，餘數為 j)

至於為什麼要除以 2 * n - 2，是因為一次 zigzag 會走一次 width 與 height，又要扣掉起點、終點
"""
def get_first_list(a_string, n):
    """
    以 list 顯示第 0 排的字串，用餘 0 篩選
    """
    return [a for i, a in enumerate(a_string) if i % (2 * n - 2) == 0]

def get_midlle_list(a_string, n, j):
    """
    以 list 顯示中間排的字串，用餘 j 或 -j 篩選
    因為不能寫 -j，所以就再加上 2 * n - 2，
    所以 -j 就會是 2 * n - 2 - j
    """
    middle_list = [
        a for i, a in enumerate(a_string) if i % (2 * n - 2) == j or i % (2 * n - 2) == 2 * n - 2 - j
    ]
    return middle_list

def get_last_list(a_string, n):
    """
    以 list 顯示第最後一排的字串，用餘 n - 1 篩選
    """
    return [a for i, a in enumerate(a_string) if i % (2 * n - 2) == n - 1]


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        step1: 篩選出中間排的 index
        step2: 用以上函數找出第 0 ~ numRows - 1 排的 list
               並且逐步 extend 到 new_order 這個 list
               所以 new_order 會收集 zigzag 從左至右的 letter
        step3: join 起來
        """
        if numRows == 1:
            return s
        middle_index_list = range(1, numRows - 1)

        new_order = get_first_list(s, numRows)
        for j in middle_index_list:
            new_order.extend(get_midlle_list(s, numRows, j))
        new_order.extend(get_last_list(s, numRows))

        return ''.join(new_order)

"""
這個 idea 其實很容易
[step: 1]
將數字轉為字串

[step: 2]
迴圈檢查第 i 個字是否與倒數第 i 個字一樣
如果不一樣，就 early return
* 注意：只有檢查字串的前半串即可

[step: 3]
如果前半串的字母都一樣，就 return True
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """主要檢查的函數"""
        a_string = str(x)
        if len(a_string) == 1:
            return True
        half_length = int(len(a_string) / 2)
        for i in range(half_length):
            if a_string[i] != a_string[len(a_string)-1-i]:
                return False
        return True

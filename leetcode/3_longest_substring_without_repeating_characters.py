class Solution:
    def check_duplicated_letter(self, a_string: str) -> bool:
        """
        判斷 a_string 內的字串是否有重複
        比較字串的長度以及字串的相異字母的數量決定
        
        Returns:
            True: 有重複
            False: 沒有重複
        """
        return len(a_string) > len(set(a_string))

    def lengthOfLongestSubstring(self, a_string: str) -> int:
        """
        主要解答函數，步驟為
            1. 如果是空字串，直接給 0
            2. 如果本身的字串就沒有重複，那就直接回覆
            3. 迴圈式判斷，從較長的 sub_string 開始判斷
               再根據整個字串的相異字元數，選取 sub_string
               的最長長度，再遞減尋找
            4. 找到的話立刻回傳 len(sub_string)
            5. 如果想要知道是哪個 sub_string，就改 return 就好
        """
        if a_string == "":
            return 0
        elif not self.check_duplicated_letter(a_string):
            return len(a_string)
        else:
            string_length = len(a_string)
            distinct_count = len(set(a_string))
            for i in range(1, string_length):
                j = min(string_length - i, distinct_count)
                for k in range(i+1):
                    sub_string = a_string[k: k+j]
                    if not self.check_duplicated_letter(sub_string):
                        return len(sub_string)

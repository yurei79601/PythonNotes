roman_symbol_dict = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}


def deal_a_part(num, divisor_list):
    roman_numeral = ""
    for i, divisor in enumerate(divisor_list):
        print(f"num: {num}, roman_numeral: {roman_numeral}")
        count = num // divisor
        remainder = num % divisor
        if count > 3:
            symbol = f"{roman_symbol_dict[divisor]}{roman_symbol_dict[divisor_list[i - 1]]}"
        else:
            symbol = count * roman_symbol_dict[divisor]
        num = remainder
        if remainder >= divisor - divisor_list[-1] and divisor != divisor_list[-1]:
            symbol += f"{roman_symbol_dict[divisor_list[-1]]}{roman_symbol_dict[divisor]}"
            num = remainder - (divisor - divisor_list[-1])

        roman_numeral += symbol
    return roman_numeral, num


def main(num):
    thousand_part, num = deal_a_part(num, [1000, 500, 100])
    hundred_part, num = deal_a_part(num, [100, 50, 10])
    digital_part, num = deal_a_part(num, [10, 5, 1])
    return f"{thousand_part}{hundred_part}{digital_part}"


class Solution:
    def intToRoman(self, num: int) -> str:
        return main(num)
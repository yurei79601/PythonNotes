"""
the solution re-write from https://leetcode.com/problems/coin-change/discuss/1909377/Python-3-dp-solution
"""

import numpy as np


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # set a default list because it would return -1 if there is no change method
        solution_list = [-1] * (amount + 1)
        
        for sub_amount in range(amount + 1):
            if sub_amount in coins:
                solution_list[sub_amount] = 1
            else:
                place_to_solution_list = np.inf
                for a_coin in coins:
                    if a_coin < sub_amount:
                        last_amount = sub_amount - a_coin
                        last_solution = solution_list[last_amount]
                        if last_solution > 0:
                            # this solution will be last solution +1 if the substraction is a coin value
                            this_solution = last_solution + 1
                            if this_solution < place_to_solution_list:
                                place_to_solution_list = this_solution
                                solution_list[sub_amount] = place_to_solution_list
        return solution_list[amount]

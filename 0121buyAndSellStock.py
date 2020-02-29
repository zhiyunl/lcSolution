"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

idea: same as maxSubarray problem 0053,
construct a delta array containing the diff of consecutive days. O(n)
kadane's alg to find best sum O(n)
Modification: return 0 if all minus
kadane's alg:
1. scan array O(n)
2. sum elements up to this location, compare with new element, cur_sum=max
3. the best sum would be updated if the cur_sum is greater
4. iterate
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = set.difference(prices[1:] + [prices[0]], prices)  # shift right and get diff
        # prices = prices[1:]
        for i in range(len(prices) - 1):
            prices[i] = prices[i + 1] - prices[i]
        cur_sum = 0
        best_sum = 0  # set to 0 if want to return 0 when minus
        for i in prices[:-1]:
            cur_sum = max(0, cur_sum + i)  # i -> 0
            best_sum = max(best_sum, cur_sum)
        return best_sum


sl = Solution()
str1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str2 = [5, 4, 3, 2, 1]
str3 = [7, 1, 5, 3, 6, 4]
print(sl.maxProfit(str3))

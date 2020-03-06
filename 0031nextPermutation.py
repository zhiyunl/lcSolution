"""
just find the next permutation of current sequence,
1. start from tail, look backwards, follow the ascending order,
2. stop at the first node *p* does satisfy.
3. find in p.right for next bigger value than *p*, *next*
4. switch *p* with *next*,
5. reverse right side number
"""

# TODO
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#
#         def reverse(index: int):
#
#         tail = len(nums) - 1
#         if tail == 0 or tail == -1:
#             return
#         while nums[tail] < nums[tail - 1]:
#             tail -= 1
#             if tail <= 0:
#                 break
#         # tail-1 is the p
#         # search for next bigger value
#         p = tail
#         mini = 0
#         for i in nums[tail:-1]:
#
#         if tail == 0:
#             # stop, reverse all
#             reverse(tail)
#         else:
#             if tail ==

# from countAndSay import Solution
# import time
# start = time.time()
#
# sl = Solution()
# # s = "MCMXCIV"
# # result = sl.romanToInt(s=s)
#
# print(sl.countAndSay(12))
# print("time is %.5f"%((time.time()-start)*10000))

# from defangIPaddr import Solution
# import time
#
# N = 20
# start = time.time()
# for i in range(N):
#     sl = Solution()
#     # str = "192.168.1.1"
#     str = "0.0.0.1"
#     sl.defangIPaddr(str)
#
# print("time is %.5f"%((time.time()-start)*10000/N))
# print(sl.defangIPaddr(str))


# from longestCommonPrefix import Solution
# import time
#
# N = 20
# start = time.time()
# sl = Solution()
# list = ["flower", "flow", "flight"]
# list=["dog","racecar","car"]
# for i in range(N):
#     sl.longestCommonPrefix(list)
#
# print("time is %.5f"%((time.time()-start)*10000/N))
# print(sl.longestCommonPrefix(list))

# import time
# from mergeTwoLists import *
# N = 1
# start = time.time()
# sl = Solution()
# l1 = ListNode(0)
# l2 = ListNode(1)
# sp1 = l1
# sp2 = l2
# for i in range(1, 10):
#     sp1.next = ListNode(i)
#     sp2.next = ListNode(i + 1)
#     sp1 = sp1.next
#     sp2 = sp2.next
# l1 = ListNode(None)
# l2 = ListNode(None)
# # for i in range(N):
# #     sl.mergeTwoLists(l1, l2)
# print("time is %.5f" % ((time.time() - start) * 10000 / N))
# # print(sl.mergeTwoLists(list))
# l = sl.mergeTwoLists(l1, l2)
# while l.next is not None:
#     print(l.val)
#     l = l.next
# print(l.val)

# import time
# from countAndSay import *
# N = 20
# n = 30
# start = time.time()
# sl = Solution()
# for i in range(N):
#     sl.countAndSay(n)
# print("time is %.5f" % ((time.time() - start) * 10000 / N))
# print(sl.countAndSay(n))

# import time
# from stringCompression import *
# N = 20
# chars = ["a", "a", "b", "b", "c", "c", "c"]
# start = time.time()
# sl = Solution()
# for i in range(N):
#     # sl.compress(chars)
#     pass
# print("time is %.5f" % ((time.time() - start) * 10000 / N))
# print(sl.compress(chars))
# print(chars)

# not finished test function, solution is done
# import time
# from diameterOfBinaryTree import *
# N = 20
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # init tree
# start = time.time()
# sl = Solution()
# for i in range(N):
#     sl.diameterOfBinaryTree(chars)
# print("time is %.5f" % ((time.time() - start) * 10000 / N))
# print(sl.diameterOfBinaryTree(chars))

import time
from isPalindrome import *
start = time.time()
sl = Solution()
l1 = ListNode(0)
sp1 = l1
for i in [2, 1, 2, 1, 3, 1, 2, 1, 2]:
    sp1.next = ListNode(i)
    sp1 = sp1.next
l1 = l1.next
print("time is %.5f" % ((time.time() - start) * 10000))
# bo = sl.isPalindrome1(l1)
bo = sl.isPalindrome2(l1)
print(bo)

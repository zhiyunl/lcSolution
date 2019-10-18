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

from defangIPaddr import Solution
import time

N = 20
start = time.time()
for i in range(N):
    sl = Solution()
    # str = "192.168.1.1"
    str = "0.0.0.1"
    sl.defangIPaddr(str)

print("time is %.5f"%((time.time()-start)*10000/N))
print(sl.defangIPaddr(str))
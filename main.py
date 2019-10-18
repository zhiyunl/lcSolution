from countAndSay import Solution
import time
start = time.time()

sl = Solution()
# s = "MCMXCIV"
# result = sl.romanToInt(s=s)

print(sl.countAndSay(12))
print("time is %.5f"%((time.time()-start)*10000))

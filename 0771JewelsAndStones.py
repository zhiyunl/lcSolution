"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
 Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.
Idea:
    linear scan, each type of J in S, O(mn)
    use hash table makes it O(n)
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        # sets = set(J)
        Dict = {e: 1 for e in J}
        for x in S:
            if x in Dict:
                cnt += 1
        return cnt


if __name__ == '__main__':
    sl = Solution()
    J = "aA"
    S = "aAAbbbbbBBsdhkhkj"
    tmp = sl.numJewelsInStones(J, S)
    print(tmp)

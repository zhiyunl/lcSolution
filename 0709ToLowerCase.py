"""
as title
idea:
    use the ASCII range for capital and lowercase to check, and use the diff to do the conversion
    A 65, a 97 diff = 32
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        stri = list(str)
        for i, x in enumerate(stri):
            if 'A' <= x <= 'Z':
                stri[i] = chr(ord(stri[i]) + 32)
        return "".join(stri)
        # don;t use list conversion


if __name__ == '__main__':
    sl = Solution()
    stri = "helo"
    tmp = sl.toLowerCase(stri)
    print(tmp)

from collections import deque, defaultdict
import numpy as np
import bisect
import heapq


def q1(n):
    s = 0
    p = 1
    while n != 0:
        s += n % 10
        p *= n % 10
        n = n // 10
    return p - s


def test1():
    print(q1(230))
    assert q1(230) == -5


def q2(s, chars):

    if len(chars) == 0:
        return 0
    if len(s) == 0:
        return 0

    chars = set([c.lower() for c in chars])

    words = s.split()
    count = 0
    for word in words:
        valid = True
        for char in word:
            if char.isalnum() and char.lower() not in chars:
                valid = False
        if valid:
            count += 1
    return count


def test2():
    soln2 = q2("Hello, my dear friend!", ['h', 'e', 'l', 'o', 'm'])
    print(soln2)
    assert(soln2 == 1)


def _count(l):
    count = {}
    for e in l:
        count[e] = count.get(e, 0) + 1
    return count


def q3(s1, s2):
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False
    if set(s1) != set(s2):
        return False

    c1 = _count(s1)
    c2 = _count(s2)
    cc1 = _count(c1)
    cc2 = _count(c2)
    return cc1 == cc2


def test3():
    assert q3("babzccc", "abbzczz")
    assert not q3("babzcccm", "bbazzczl")


def _find_sum(a, b, t):
    if len(a) == 0 or len(b) == 0:
        return 0

    b = set(b)
    count = 0
    visited = []
    for e in set(a):
        if t - e in b and e not in visited:
            count += 1
            visited.append(e)
    return count


def q4(a, b, qs):
    if len(a) == 0 or len(b) == 0:
        return []
    if len(qs) == 0:
        return []

    result = []
    for q in qs:
        if len(q)==3:
            _, idx, val = q
            b[idx] = val
        else:
            _, target = q
            count = _find_sum(a, b, target)
            result.append(count)
    return result


def test4():
    result = q4([1, 2, 3], [3, 4], [[1, 5], [1, 1, 1], [1, 5]])
    print(result)
    assert result == [2, 1]


def q5(l):
    count = 0
    for num in l:
        if num < 0:
            num = -num
        if len(str(num)) % 2 == 0:
            count += 1
    return count


def test5():
    soln5 = q5([12, 3, 5, 3456])
    print(soln5)
    assert soln5 == 2
    soln5 = q5([-12, -3, -5, -3456])
    print(soln5)
    assert soln5 == 2


def q6(l):
    count = {}
    for n in l:
        count[n] = count.get(n, 0) + 1
    most_num = []
    most_count = -float('inf')
    for n, c in count.items():
        if c > most_count:
            most_count = c
            most_num = [n]
        elif c == most_count:
            most_num.append(n)
    return most_num


def test6():
    soln6 = q6([2, 2, 3, 3, 5])
    print(soln6)
    assert soln6 == [2, 3]


def _count_parts(l, s):
    return sum([n // s for n in l])


def q7(arr, k):
    l = 1
    r = max(arr) + 1
    parts = sum(arr)

    while l < r - 1:
        mid = (l + r) // 2
        print(l, r, mid)
        parts = _count_parts(arr, mid)
        # print(parts)
        if parts < k:
            r = mid - 1
        else:
            l = mid

    if parts < k:
        return -1

    return l


def test7():
    soln = q7([1, 2, 3, 4, 9], 5)
    print(soln)
    assert soln == 3
    soln = q7([9, 9, 9, 9, 9], 5)
    print(soln)
    assert soln == 9
    soln = q7([1, 1, 1, 1, 1], 6)
    print(soln)
    assert soln == -1


def q8(l, criterion):
    if len(l) <= 2:
        return 0

    if len(l) == 3:
        return 1 if criterion(l) else 0

    sub_arr = deque(l[:3])
    count = 1 if criterion(sub_arr) else 0
    for e in l[3:]:
        sub_arr.popleft()
        sub_arr.append(e)
        count += 1 if criterion(sub_arr) else 0

    return count


def test8():
    soln = q8([1, 1, 2, 1, 5, 3, 2, 3], lambda x: len(set(x)) == 2 and len(x) == 3)
    print(soln)
    assert soln == 3
    soln = q8("aabdcreff", lambda x: len(set(x)) == 3 and len(x) == 3)
    print(soln)
    assert soln == 5


def q9(mat, diag):
    assert 1 <= diag <= 4

    if diag == 4:
        return mat

    if len(mat) <= 2:
        return mat

    N = len(mat)
    # Consider all squares one by one
    for x in range(0, int(N/2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):
            if x == y or x == N-1-y:
                continue

            # top:    mat[x][y]
            # right:  mat[y][N-1-x]
            # bottom: mat[N-1-x][N-1-y]
            # left:   mat[N-1-y][x]
            if diag == 1:
                # store top in temp variable
                temp = mat[x][y]
                # move values from left to top
                mat[x][y] = mat[N-1-y][x]
                # move values from bottom to left
                mat[N-1-y][x] = mat[N-1-x][N-1-y]
                # move values from right to bottom
                mat[N-1-x][N-1-y] = mat[y][N-1-x]
                # assign temp to right
                mat[y][N-1-x] = temp
            elif diag == 2:
                # store top in temp variable
                temp = mat[x][y]
                # move values from bottom to top
                mat[x][y] = mat[N-1-x][N-1-y]
                # move values from temp to bottom
                mat[N-1-x][N-1-y] = temp
                # store left in temp variable
                temp = mat[N-1-y][x]
                # move values from right to left
                mat[N-1-y][x] = mat[y][N-1-x]
                # move values from temp to right
                mat[y][N-1-x] = temp
            elif diag == 3:
                # store current cell in temp variable
                temp = mat[x][y]
                # move values from right to top
                mat[x][y] = mat[y][N-1-x]
                # move values from bottom to right
                mat[y][N-1-x] = mat[N-1-x][N-1-y]
                # move values from left to bottom
                mat[N-1-x][N-1-y] = mat[N-1-y][x]
                # assign temp to left
                mat[N-1-y][x] = temp

    return mat


def test9():
    mat = np.random.randint(10, size=(10,10))
    new_mat = mat.copy()
    for i in range(2):
        new_mat = q9(new_mat, 2)
    assert np.all(mat == new_mat)
    new_mat = mat.copy()
    for i in range(4):
        new_mat = q9(new_mat, 1)
    assert np.all(mat == new_mat)
    new_mat = mat.copy()
    for i in range(4):
        new_mat = q9(new_mat, 3)
    assert np.all(mat == new_mat)
    new_mat = q9(mat.copy(), 4)
    assert np.all(mat == new_mat)


"""
isPrefix. Given string array A and B. Return true if every string in B
can be constructed by the string in A.
Input: A = ["ab","c","d"] B = ["abc", "abd", "cd"]
Output: true
"""
def composable(l, s, mem={}):
    if s == '':
        return True

    if s in mem:
        return mem[s]

    mem[s] = False

    for w in l:
        length = len(w)
        if s[:length] == w and composable(l, s[length:], mem):
            mem[s] = True

    return mem[s]


def composable_nonrepeat(l, s, used=0, mem={}):
    if s == '':
        return True

    if s in mem:
        return mem[s]

    mem[s] = False

    for idx, w in enumerate(l):
        if used >> idx:
            continue
        length = len(w)
        if s[:length] == w and composable_nonrepeat(l, s[length:], used | (1 << idx), mem):
            mem[s] = True

    return mem[s]


def q10(a, b):
    return all([composable(a, s) for s in b])


def q10_nonrepeat(a, b):
    return all([composable_nonrepeat(a, s) for s in b])


def test10():
    assert q10(["ab","c","d"], ["abc", "abd", "cd", "ababcc"])
    assert not q10(["ab","c","d"], ["abc", "abd", "cd", "ababcq"])
    assert q10_nonrepeat(["ab","c","d"], ["abc", "abd", "cd"])
    assert not q10_nonrepeat(["ab","c","d"], ["abc", "abd", "cd", "ababcc"])


# longestArithSeqLength
def longestArithSeqLength(a, b):
    reverse_a = a[::-1]
    reverse_b = b[::-1]

    A = []
    while len(reverse_a) != 0 or len(reverse_b) != 0:
        if len(reverse_a) == 0:
            A.append(reverse_b.pop())
        elif len(reverse_b) == 0:
            A.append(reverse_a.pop())
        elif reverse_a[-1] < reverse_b[-1]:
            A.append(reverse_a.pop())
        else:
            A.append(reverse_b.pop())

    d = defaultdict(dict)
    n = len(A)
    res = -1  # usually this is 1 for longest arith seq problem
    for i in range(n):
        for j in range(i):
            v = A[i] - A[j]
            # the default length is 1
            if v not in d[j]: d[j][v] = 1
            if v not in d[i]: d[i][v] = 0
            d[i][v] = max(d[i][v] ,d[j][v] + 1)
            res = max(res, d[i][v])
    return res


def test11():
    soln = longestArithSeqLength([0,4,8,20], [5,7,12,16,22])
    print(soln)
    assert soln == 6


def q12(n, k):
    visited = set()
    s = str(n)
    count = 0
    for i in range(len(s)-k+1):
        sub_s = s[i:i+k]
        if sub_s in visited:
            continue
        else:
            visited.add(sub_s)
            if n % int(sub_s) == 0:
                count += 1
    return count


def test12():
    soln = q12(120, 2)
    print(soln)
    assert soln == 2
    soln = q12(555, 1)
    print(soln)
    assert soln == 1
    soln = q12(2345, 2)
    print(soln)
    assert soln == 0


def q13(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    diff = len(s1) - len(s2)
    l = [s1[:diff]]
    s1 = s1[diff:]

    for n1, n2 in zip(s1, s2):
        l.append(str(int(n1) + int(n2)))

    return ''.join(l)


def test13():
    soln = q13('99', '99')
    print(soln)
    assert soln == '1818'
    soln = q13('999', '99')
    print(soln)
    assert soln == '91818'


## https://leetcode.com/discuss/interview-question/388944/Google-or-Phone-Screen-or-Range-Queries-for-Frequencies
def find_range_query_frequencies(nums, queries):
    dd = defaultdict(list)
    ans = 0
    for i, num in enumerate(nums):
        dd[num].append(i) # key: num;  value: indexes where nums[index] = num
    for query in queries:
        left, right, k = query
        if k not in dd:
            continue
        i, j = bisect.bisect_left(dd[k], left), bisect.bisect_right(dd[k], right)
        frequency = j - i
        ans += frequency
    return ans


def test14():
    nums = [1, 2, 1, 3, 1, 2, 1]
    queries = [[1, 3, 3], [0, 4, 1], [2, 5, 2], [5, 6, 1]]
    soln = find_range_query_frequencies(nums, queries)
    print(soln)
    assert soln == 6
    nums = [1,1,2,3,2]
    queries = [[1,2,1], [2,4,2], [0,3,1]]
    soln = find_range_query_frequencies(nums, queries)
    print(soln)
    assert soln == 5


def q15(qs):
    disabled_rows = 0
    disabled_cols = 0
    min_row, min_col = 0, 0
    results = []

    for q in qs:
        qtype, val = q
        if qtype == 0:
            results.append((min_row+1)*(min_col+1))
        elif qtype == 1:
            disabled_rows = disabled_rows | (1 << val)
            while disabled_rows & (1 << min_row) != 0:
                min_row += 1
        else:
            assert qtype == 2
            disabled_cols = disabled_cols | (1 << val)
            while disabled_cols & (1 << min_col) != 0:
                min_col += 1

    return results


def test15():
    soln = q15([[0, 0], [1, 0], [0, 0], [2, 0], [0, 0]])
    print(soln)


def reverse(x):
    sign = (x > 0) * 2 - 1
    digits = int(str(x * sign)[::-1])
    return sign * digits * (digits < 2**31)


def test16():
    soln = reverse(123)
    print(soln)
    assert soln == 321
    soln = reverse(120)
    print(soln)
    assert soln == 21


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()


if __name__ == '__main__':
    main()

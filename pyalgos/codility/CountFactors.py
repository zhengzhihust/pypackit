"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
"""
Detected time complexity: O(N)
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
RANGE_N = (1, 2147483647)


def solution(N):
    # write your code in Python 3.6
    assert isinstance(N, int) and RANGE_N[0] <= N <= RANGE_N[1]

    result = []
    count = N
    for i in range(1, N + 1):
        ret, le = divmod(count, i)
        if le == 0:
            result.append(ret)
    return len(result)


"""
Complexity:
expected worst-case time complexity is O(sqrt(N));
expected worst-case space complexity is O(1).
"""


def solution_best(N):
    cnt = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt

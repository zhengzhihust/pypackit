"""
This is a demo task.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
RANGE_N = (1,100000)
RANGE_E = (-1000000,1000000)
def solution(A):
    # write your code in Python 3.6
    assert A is not None
    N = len(A)
    assert RANGE_N[0] <= N <= RANGE_N[1]
    M = max(A)
    assert min(A) >= RANGE_E[0] and M <= RANGE_E[1]
    if M <= 0:
        return 1
    else:
        for i in range(1,M + 1):
            if i not in A:
                return i
    return M + 1
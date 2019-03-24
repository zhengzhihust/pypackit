"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.

https://github.com/zhengzhihust/pypackit/blob/master/files/6f5e8faa3000c0a74157e6e0bc759b8a.png

Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
RANGE_N = (1, 400000)
RANGE_E = (0, 1000000000)


def solution(A):
    # write your code in Python 3.6
    assert A is not None
    N = len(A)
    assert RANGE_N[0] <= N <= RANGE_N[1]
    peaks = []
    for idx in range(1, N - 1):
        assert RANGE_E[0] <= A[idx - 1] <= RANGE_E[1]
        assert RANGE_E[0] <= A[idx] <= RANGE_E[1]
        assert RANGE_E[0] <= A[idx + 1] <= RANGE_E[1]

        if A[idx - 1] < A[idx] > A[idx + 1]:
            peaks.append(idx)

    if not peaks:
        return 0

    M = len(peaks)
    S = []
    while peaks:
        peak = peaks.pop()
        if not S:
            S.append(peak)
        else:
            if abs(peak - S[-1]) >= M:
                S.append(peak)
    return len(S)
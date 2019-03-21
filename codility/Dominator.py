"""
Dominator
Find an index of an array such that its value occurs at more than half of indices in the array.

Task description
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
RANGE_N = (0, 100000)
RANGE_E = (-2147483648, 2147483647)

def solution(A):
    assert A is not None
    N = len(A)
    if N == 0:
        return -1
    elif N == 1:
        return 0
    dominator = ''
    count = 0
    for idx, value in enumerate(A):
        assert isinstance(value, int) and RANGE_E[0] <= value <= RANGE_E[1]
        if dominator == '':
            dominator = value
            count += 1
        else:
            if dominator == value:
                count += 1
            else:
                count -= 1
                if count == 0:
                    dominator = ''
    if dominator == 0:
        return -1

    cnt = 0
    last_index = 0
    for idx, value in enumerate(A):
        if value == dominator:
            cnt += 1
            last_index = idx
    if cnt * 2 > N:
        return last_index
    return -1
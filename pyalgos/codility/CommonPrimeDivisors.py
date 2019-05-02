"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A, B is an integer within the range [1..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

"""
Detected time complexity: O(Z * (max(A) + max(B))**(1/2))
"""
RANGE_Z = (1, 6000)
RANGE_E = (1, 2147483647)


def factorization(X):
    i = 2
    result = []
    while i * i <= X:
        while X % i == 0:
            result.append(i)
            X = X // i
        i += 1
    if X > 1:
        result.append(X)
    return result


def solution(A, B):
    # write your code in Python 3.6
    assert A is not None and B is not None
    Z = len(A)
    assert RANGE_Z[0] <= Z == len(B) <= RANGE_Z[1]
    cnt = 0
    for idx in range(0, Z):
        assert RANGE_E[0] <= A[idx] <= RANGE_E[1] and RANGE_E[0] <= B[idx] <= RANGE_E[1]
        a = factorization(A[idx])
        b = factorization(B[idx])

        if sorted(set(a)) == sorted(set(b)):
            cnt += 1
    return cnt
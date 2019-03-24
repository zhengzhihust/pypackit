"""
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
"""
Detected time complexity: O(sqrt(N))
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
RANGE_N = (1,1000000000)
def solution(N):
    # write your code in Python 3.6
    assert isinstance(N, int) and RANGE_N[0] <= N <= RANGE_N[1]
    min_val = RANGE_N[1]
    i = 1
    while i * i <= N:
        quot, remain = divmod(N, i)
        if remain == 0:
            perimeter = 2 * (i + quot)
            min_val = min(min_val, perimeter)
        i += 1
    return min_val

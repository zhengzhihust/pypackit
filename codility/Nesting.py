"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

"""
Detected time complexity: O(N)
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
RANGE_N = (0, 1000000)
RANGE_E = ('(', ')')


def solution(S):
    # write your code in Python 3.6
    assert S is not None
    N = len(S)
    assert RANGE_N[0] <= N <= RANGE_N[1]
    if N == 0:
        return 1
    count = 0
    for idx, value in enumerate(S):
        assert value in RANGE_E
        if value == "(":
            count += 1
        else:
            if count == 0:
                return 0
            else:
                count -= 1
    if count != 0:
        return 0
    return 1

"""
Euclidean algorithm by subtraction
"""

"""
Greatest common divisor by subtraction
"""


def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


"""
Least common multiple
"""


def lcm(a, b):
    return a * (b / gcd(a, b))


"""
Prime factorization - list
"""


def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

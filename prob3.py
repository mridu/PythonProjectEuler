def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(int(raw_input("Enter number:")))
largest_prime_factor = max(pfs)
print "largest_prime_factor :: %r" %largest_prime_factor
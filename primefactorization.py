#Returns prime factors of a positive integer number. 240 = [[2, 4], [3, 1], [5, 1]]
def primeFactorization(int):
    primes = getPrimes(2,int)
    divisors = getDivisors(int)
    factors = []
    i = 0
    for prime in primes:
        total = 0
        step = int
        while step%prime == 0:
            total += 1
            step /= prime
        if int%prime == 0:
            factors.append([prime])
            factors[i].append(total)
        else:
            continue
        i += 1
    return factors

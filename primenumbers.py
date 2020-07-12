#Returns prime numbers in an interval
def getPrimes(min, max):
    primes = []
    for int in range(min, max+1):
        if int <= 1: continue
        modulos = []
        for divisor in range (2, int):
            modulos.append(int%divisor)
        primes.append(int) if not 0 in modulos else None
    return primes

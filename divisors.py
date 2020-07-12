#Returns positive integer divisors of a positive integer number.
def getDivisors(int):
    if int == 0: return False
    divisors = []
    for divisor in range(1, int+1):
        divisors.append(divisor) if int%divisor == 0 else None
    return divisors

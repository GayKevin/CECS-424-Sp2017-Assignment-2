import math


def is_prime(nbr):
    if nbr < 2:
        return False
    for i in range(2, int(math.sqrt(nbr)) + 1):
        if nbr % i == 0:
            return False
    return True


def sum_primes(nbr, total):
    return nbr + total


def get_primes(nbr):
    while True:
        if is_prime(nbr):
            yield nbr
        nbr += 1


def showprimes(nbr):
    total = 0
    primes = get_primes(nbr)

    for x in primes:
        if x >= 2000000:
            return total
        total = sum_primes(x, total)


def main():
    print(showprimes(0))


if __name__ == "__main__":
    main()

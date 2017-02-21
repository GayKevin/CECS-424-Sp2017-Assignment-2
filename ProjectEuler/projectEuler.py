def is_prime(nbr):
    if nbr == 2 or nbr == 3 or nbr == 5 or nbr == 7:
        return True
    elif nbr % 2 == 0 or nbr % 3 == 0 or nbr % 5 == 0 or nbr % 7 == 0:
        return False
    else:
        return True


def sum_primes(nbr, total):
    return nbr + total


def get_primes(nbr):
    total = 0

    while total < 2000000:
        if is_prime(nbr):
            print(nbr)
            total = sum_primes(nbr, total)
        nbr += 1


def main():
    get_primes(70)


if __name__ == "__main__":
    main()

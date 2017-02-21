import random

def main():

    coin = ["H", "H", "H", "H", "H", "T", "T", "T", "T", "T"]
    random.shuffle(coin)

    print(coin)

if __name__ == "__main__":
    main()
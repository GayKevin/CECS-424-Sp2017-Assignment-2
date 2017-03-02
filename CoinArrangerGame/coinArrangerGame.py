#!/usr/bin/env python3
def firstRound(coins, tiretposition):
    coinInput = input()
    size = len(coinInput)

    print("Type 1 to move your coin to the left - Type 2 for the right")
    userinput = input()

    if size <= 10:
        if userinput == "1":
            createTiret(coins, size, 1, tiretposition)
            return True
        elif userinput == "2":
            createTiret(coins, size, 2, tiretposition)
            return True

    print("You must have at least one spaces")
    return False


def createTiret(coins, size, type, tiretposition):
    a = coins[size]
    b = coins[size + 1]
    coins[size] = "-"
    coins[size + 1] = "-"
    tiretposition.insert(0, size)

    if type == 2:
        coins.append(a)
        coins.append(b)
    else:
        tiretposition.insert(0, size)
        coins.insert(size + 2, a)
        coins.insert(size + 3, b)


def checkTiret(coin, size):
    if coin[size + 1] == "-" or coin[size] == "-":
        print("It's impossible to select a -")
        return False
    return True


def checkWin(coins, tiretposition):
    coinCheck = ""

    if 1 < tiretposition[0] < 8:
        return False

    for coin in coins:
        if coin is not "-":
            if coin is not coinCheck:
                coinCheck = coin
            else:
                return False
    return True


def swapList(coins, userInput, tiretposition):
    size = len(userInput)

    if len(userInput) <= 9:
        if checkTiret(coins, size) is False:
            return False
        a = coins[size]
        b = coins[size + 1]
        tiret = coins[tiretposition[0]]

        coins[tiretposition[0]] = a
        coins[tiretposition[0] + 1] = b
        coins[size] = tiret
        coins[size + 1] = tiret
        tiretposition.insert(0, size)

    return checkWin(coins, tiretposition)


def main():
    coins = ["H", "H", "H", "H", "H", "T", "T", "T", "T", "T"]
    i = 0
    tiretposition = []

    print("Coin Arranger Game!")
    showCoins(coins)

    while firstRound(coins, tiretposition) is False:
        continue

    showCoins(coins)

    while swapList(coins, input(), tiretposition) is False:
        if i == 4:
            print("You have move your coins 5 times, you have loose")
            return
        showCoins(coins)
        i += 1
        continue

    showCoins(coins)
    print("You have finished the game!")


def showCoins(coins):
    print("".join(coins))


if __name__ == "__main__":
    main()

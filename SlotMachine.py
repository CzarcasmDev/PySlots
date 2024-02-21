import random
money = 100
spins = 0
wins = 0
miniwins = 0
jackpots = 0


print("Welcome to the slot machine! 3 in a row of any number is a win, 2 of any number is a mini-win, and 777 is jackpot.")
while money != 0:
    input("Press enter to spin.")
    print("Money:",money)
    print("Spins:",spins)
    print("Jackpots:",jackpots)
    print("Wins:",wins)
    print("Small Wins:",miniwins)

    s1 = random.randint(0,7)
    s2 = random.randint(0,7)
    s3 = random.randint(0,7)
    money = money - 1

    print("_________________")
    print("|               |")
    print("[",s1,"]","[",s2,"]","[",s3,"]")
    print("|               |")
    print("|               |")
    print("|               |")
    print("|               |")
    print("_________________")
    spins = spins + 1
    if s1 == s2 or s2 == s3 or s1 == s3:
        print("Small win!")
        money = money + 5
        spins = spins + 1
        miniwins = miniwins + 1


    if s1 == s2 and s2 == s3:
     print("WIN!")
     money = money + 25
     spins = spins + 1
     wins = wins + 1

    if s1 == 7 and s2 == 7 and s3 == 7:
        print("J A C K P O T!!!")
        money = money + 25
        spins = spins + 1
        jackpots = jackpots + 1
else:
    print("You ran out of money. Game over!")
    exit()

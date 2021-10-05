import random

number = random.randint(1,9)

chances = 0

print("Guess a number (between 1 and 9): ")
while chances <5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation YOU WON!!!"),
        print("You are the winner boy")
        break
    elif guess<number:
        print("your guess was too low: Guess a number huigher than that")
    else:
        print("Your guess was high: Guess a number smaller than that: ")

    chances += 1

    if not chances < 5:
        print("You LOSE!!! The number is", number ),
        print("Imppoteybobbob")
2
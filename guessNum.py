from logo import gtn
import random

random_number = random.randint(1, 100)
attempts = 0
guess = 0

print(gtn)
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
print(random_number)
def higher_or_lower(guess, num_a):
    if guess > random_number:
        print("Too high\n")
        num_a -= 1
    elif guess < random_number:
        print("Too low\n")
        num_a -= 1
    elif guess == random_number:
        print("You got it!")
        exit()
    return guess, num_a


if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.")
    while attempts > 0:
        number_guess = int(input("Make a guess: "))
        higher_or_lower(guess=number_guess, num_a=attempts)
        attempts -= 1
        print(f"Your current attempt is {attempts} ")
        if attempts == 0:
            print("You lose")

elif difficulty == 'hard':
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.")
    while attempts > 0:
        number_guess = int(input("Make a guess: "))
        higher_or_lower(guess=number_guess, num_a=attempts)
        attempts -= 1
        print(f"Your current attempt is {attempts} ")
        if attempts == 0:
            print("You lose")

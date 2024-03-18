import random

def main():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print("Try to guess the number in as few attempts as possible")
    number = random.randint(1, 100)
    guess = 0
    count = 0
    while guess != number:
        guess = int(input("Enter your guess: "))
        count += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Congratulations! You guessed the number in", count, "attempts.
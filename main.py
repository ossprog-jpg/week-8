import random

number = random.randint(1, 10)
guess = 0
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts = attempts - 1 #attempts -= 1

    if guess == number:
        print("Congratulations! You have guessed the number!")
    else:
        print("Too bad. Try again.")

    print(f"attempts left: {attempts}")


if guess != number:
    print(f"Game over! The secret number was: {number}")

    

# while guess != number:
#     guess = int(input("Guess a number between 1 and 10: "))

# if guess == number:
#     print("Congratulations! You have guessed the number!")
# else:
#     print("Too bad. Try again.")

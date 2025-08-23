# Guess the number game:

import random

n = random.randint(1, 100)
b = -1
guesses = 1

while(b != n):
    b = int(input("Enter number: "))
    if(b > n):
        print("Enter lower number")
        guesses += 1
    elif(b < n):
        print("Enter higher number")
        guesses += 1
print(f"You have guessesed the number {n} in {guesses} attempt")
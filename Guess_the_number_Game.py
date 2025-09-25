# Guess the number game:
import random

n = random.randint(1, 100) # Here through random module we are generating random numbers between 1 to 100 in storing in n variable.
b = -1 # Here we initialize the value of b from -1.
guesses = 1 # Here we initialize the value of guesses from 1.

while(b != n): # Here we are using while loop to check if b is not equal to n then ask the user untill he guess the ritgh number.
    b = int(input("Enter number: "))
    if(b > n): # This condition checks that if the number is greater then n then infrom the user.
        print("Enter lower number")
        guesses += 1
    elif(b < n): # This condition checks that if the number is smaller then n then infrom the user.
        print("Enter higher number")
        guesses += 1
print(f"You have guessesed the number {n} in {guesses} attempt")
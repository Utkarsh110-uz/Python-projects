import random

def check():
    n = random.randint(1, 100) 
    b = -1 
    guesses = 1
    while(b != n):
        b = int(input("Enter number here: "))
        if(b > n):
            print("Enter lower number please")
            guesses += 1
        elif(b < n): 
            print("Enter higher number please")
            guesses += 1
    print(f"You have guessesed the number {n} in {guesses} attempt")
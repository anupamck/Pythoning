print("Hi there, what is your name?")
name = input()
print("Hi "+name+". You are cute!")
import random
secretNumber = random.randint(1,30)
print("Well, "+name+" I am thinking of a number between 1 and 30.")

for guessesTaken in range(1,100):
    print("Take a guess")

    try:
        guess = int(input())
        if guess<1 or guess>30:
           print("That is not in the expected range")
        elif guess>secretNumber:
           print("That is too high. Guess lower")
        elif guess<secretNumber:
           print("That is too low. Guess higher")
        else:
           print("That is the right number, you smart, gorgeous human. You have taken " +str(guessesTaken)+ " guesses. I bow before you with my virtual arms")
           break

    except ValueError:
        print("Please enter an integer, darling. You are smarter than that")
          


#This program is about to find and guess the random number generated from random function

#import the random and math module
import random
import math

#Range of the numbers
lower = int(input("Enter the lower bound : "))

upper = int(input("enter the upper bound : "))

#Compiler generates a random number
rand = random.randint(lower,upper)

#Number of guesses
Guess = int(math.log2(upper-lower+1))

print("Number of Guesses : " , Guess)

#holder for number of guesses
count = 0

while (True):
    count += 1

    #Check if the user ran out of gueeses
    if (count > Guess):
        print("You ran out of guesses\n")
        print("Better luck next time!\n")
        break; 

    #Taking input from user
    val = int(input("Enter your number : "))

    #Handeling exceptions and errors
    if (val < lower or val > upper):
        print("The number you entered is out of range, please enter a number "
              "between", lower , " and " , upper , "\n")
        print("This will not effect the number of gusses you have left")

        count -= 1
        print("number of guesses left : ", count)

    #Condition
    if (val > rand ):
        print("Try Again! you guessed too high\n")
    elif (val < rand) :
        print("Try Again! you guessed too small\n")
    elif (val == rand) :
        print("Congratulations, you guessed the number correctly\n")
        print("You guessed the number with only " , count ," guesses")
        break;  #If the number is guessed exit the loop


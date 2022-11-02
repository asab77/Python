import random

mylist = ["Rock" , "Paper", "Scissors"]

# rand will hold a random item in the list for computer
rand = random.choice(mylist)

#To hold the score of the players
computer_score = 0
user_score = 0

print("Welcome to the game of Rock, Paper, Scissors\n")

# ask the player how many rounds would like to play
turn = int(input("How many rounds do you want to play?"))

i=0
while (i < turn):
    print("Choose your option from menu")
    print("1-Rock     2-Paper     3-Scissors")

    # Get the input from user
    user_input = input("Enter your choice: ")

    if (user_input == rand):
        print(f"Both players selected {user_input}. it's a tie!\n")
        computer_score +=1
        user_score +=1
        print(f"User : {user_score}\n")
        print(f"Computer : {computer_score}\n")

    elif (user_input == "Rock"):
        if (rand == "scissors"):
            print("Rock smashes scissors! you win\n")
            user_score += 1
            print(f"User : {user_score}\n")
            print(f"Computer : {computer_score}\n")
        else:
            print("Paper covers Rock! you lost\n")
            computer_score += 1
            print(f"User : {user_score}\n")
            print(f"Computer : {computer_score}\n")
    elif (user_input == "paper"):
        if(rand == "rock"):
            print("Paper covers Rock! you win\n")
            user_score += 1
            print(f"User : {user_score}\n")
            print(f"Computer : {computer_score}\n")
        else:
            print("Scissors cuts Paper! you lost\n")
            computer_score += 1
            print(f"User : {user_score}\n")
            print(f"Computer : {computer_score}\n")
    elif (user_input == "scissors"):
        if(rand == "paper"):
            print("Scissors cuts paper! you win\n")
            user_score += 1
            print(f"User : {user_score}\n")
            print(f"Computer : {computer_score}\n")
        else:
            print("rock smashes scissors! you lost\n")
            computer_score += 1
            print(f"User : {user_score}\n")
            print(f"Computer : {computer_score}\n")
    turn -= 1
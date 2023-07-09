import random   #IMPORT RANDOM LIBRARY TO CREATE ALEATORY NUMBER

#ASK FOR PLAYER INFORMATION 
name = input("Welcome, what's your name?: ")
init = input(f"{name} ¿Would you like to play guess the number? (y/n) ")   

#CREATE THE VARIBALES USED IN THE PROGRAM
count = 8
wins = 0
attempts = 0
game_range = list(range(101))

#IF THE PLAYERS WANTS TO PLAY BEGIN THE GAME
if init == "y":

#CREATE THE RANDOM VARIABLE AND EXPLAIN THE RULES
    print("Okay, I'll think about a number between 1 and 100, you start with 8 lifes, let's play!")
    number = random.randint(1,100)

#START A LOOP THAT DEPENDS ON THE NUMBER OF LIFES
    while count > 0:

        #ASK FOR A NUMBER
        number_user = input("Guess the number I'm thinking: ")
        
        #CONDITIONALS TO VERIFY IF THE INPUT IS A VALID ENTRY AND GIVE THE JOINTS TO THE PLAYER
        if not number_user.isdigit():
            print("Not a valid input")
        elif int(number_user) < 1 or int(number_user) > 100:
            print("Input out of range")
        elif (int(number_user) < number):         
            print("Your entry is minor than the number i'm thinking")
            count -= 1
        elif ( int(number_user) > number):      
            print("Your entry is major than the number i'm thinking")
            count -= 1

        #CONDITIONAL WHEN PLAYER GET THE NUMBER RIGHT
        elif (int(number_user) == number):
            number = random.randint(1,100)
            wins += 1
            count += 3
            print(f"Congratulations, you gained 3 more attempts, you have {count} lifes, keep playing!")
        attempts +=1

#WHEN THERE IS NO MORE LIFES, THE GAME IT'S OVER AND THE INFORMATION ABOUT THE WINS AND THE ATTEMPTS ARE SHOWN
    if wins > 1 or wins == 0:
        print(f"Out of lifes :(, you won {wins} times, with {attempts} attempts")
    else:
        print(f"Out of lifes :(, you won {wins} time, with {attempts} attempts")

#CONDITIONAL WHEN THE PLAYER DECIDES NOT TO PLAY OR WHEN AN INVALID ENTRY IS GIVEN
elif init == "n":
    print("Okay, see you next time :)")
else:
    print("That's not a valid option, exiting ...")
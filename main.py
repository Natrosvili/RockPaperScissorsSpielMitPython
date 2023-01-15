import random
gameOver = False
userScore = 0
computerScore = 0

print("\nHello and welcome to the rock-paper-scissors game.")
requiredAnswer = input("\nWould you like to play?\n1. -> Yes\n2. -> No\nAnswer: ")



if requiredAnswer  == "2" or requiredAnswer  == "No" or requiredAnswer  == "no" or requiredAnswer  == "NO" or requiredAnswer  == "N" or requiredAnswer  == "n":
    print("\nHave a nice day!")
    game_over = True


def score():
    return f"User: {userScore}\nComputer: {computerScore}"



if requiredAnswer  == "1" or requiredAnswer  == "Yes" or requiredAnswer  == "yes" or requiredAnswer  == "YES" or requiredAnswer  == "y" or requiredAnswer  == "Y":
    while not gameOver:
        computerChoice = random.randint(1, 3)

        userChoice = int(input("""What do you choose?
'1' for Rock
'2' for Paper
'3' for Scissors
Answer: """))
            
            
            
        if userScore == 3: 
            gameOver = True 
            print("Congrats! You win")
        elif computerScore == 3: 
            gameOver = True
            print("What a shame! The computer wins")


        if userChoice > 3 or userChoice < 1:
            print("\nYou've written an invalid number. You lose!")
            computerScore += 1
            userScore = userScore
            print(score())

            
        elif userChoice == 1 and computerChoice == 2:
            print(f"\nThe computer chose {computerChoice}. You lose!")
            computerScore += 1
            userScore = userScore
            print(score())

            
        elif userChoice == 1 and computerChoice == 3:
            print(f"\nThe computer chose {computerChoice}. You win!")
            userScore += 1
            computerScore = computerScore
            print(score())

        
        elif userChoice == 2 and computerChoice == 3:
            print(f"\nThe computer chose {computerChoice}. You lose!")
            computerScore += 1
            userScore = userScore
            print(score())

            
        elif userChoice == 2 and computerChoice == 1:
            print(f"\nThe computer chose {computerChoice}. You win!")
            userScore += 1
            computerScore = computerScore
            print(score())            
            
            
        elif userChoice == 3 and computerChoice == 1:
            print(f"\nThe computer chose {computerChoice}. You lose!")
            computerScore += 1
            userScore = userScore
            print(score())

            
        elif userChoice == 3 and computerChoice == 2:
            print(f"\nThe computer chose {computerChoice}. You win!")
            userScore += 1
            computerScore = computerScore
            print(score())
        
        
        elif userChoice == computerChoice:
            print("\nBalance!")
            computerScore = computerScore
            userScore = userScore
            print(score())            

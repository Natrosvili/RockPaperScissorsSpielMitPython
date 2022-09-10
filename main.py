import random
game_over = False
user_score = 0
computer_score = 0

print("\nHallo und Herzlich Wilkommen zum Rock-Paper-Scissors spiel.")
x= input("\nMöchten Sie spielen?\n1. -> Ja\n2. -> Nein\nAntwort: ")



if x == "2" or x == "Nein" or x == "nein" or x == "NEIN" or x == "N" or x == "n":
    print("\nSchade! Schönnen Tag noch")
    game_over = True


def score():
    return f"User: {user_score}\nComputer: {computer_score}"



if x == "1" or x == "Ja" or x == "ja" or x == "JA" or x == "j" or x == "J":
    while not game_over:
        computer_choice = random.randint(1, 3)

        user_choice = int(input("\nWas wälhen Sie?\n"
            "'1' für Rock\n"
            "'2' für Paper\n"
            "'3' für Scissors: "))
            
            
        # Hier entscheiden wir, wie viele Punkte 
        # gewonnen werden müssen, um das Spiel zu gewinnen. 
        # Beispielswiese 3.
        
        if user_score == 3: 
            print("Glückwünsch! Sie haben den Computer gewonnen")
            game_over = True 
        elif computer_score == 3: 
            print("Schade! der Computer hat gewonnen")
            game_over = True


        if user_choice > 3 or user_choice < 1:
            print("\nSie haben ein invalid Nummer geschrieben. Sie haben Verloren! ")
            computer_score += 1
            user_score = user_score
            print(score())

            
        elif user_choice == 1 and computer_choice == 2:
            print(f"\nDer Computer hat {computer_choice} gewählt. Sie haben verloren!")
            computer_score += 1
            user_score = user_score
            print(score())

            
        elif user_choice == 1 and computer_choice == 3:
            print(f"\nder Computer hat {computer_choice} gewählt. Sie haben gewonnen!")
            user_score += 1
            computer_score = computer_score
            print(score())

        
        elif user_choice == 2 and computer_choice == 3:
            print(f"\nder Computer hat {computer_choice} gewählt. Sie haben verloren!")
            computer_score += 1
            user_score = user_score
            print(score())

            
        elif user_choice == 2 and computer_choice == 1:
            print(f"\nder Computer hat {computer_choice} gewählt. Sie haben gewonnen!")
            user_score += 1
            computer_score = computer_score
            print(score())            
            
            
        elif user_choice == 3 and computer_choice == 1:
            print(f"\nder Computer hat {computer_choice} gewählt. Sie haben verloren!")
            computer_score += 1
            user_score = user_score
            print(score())

            
        elif user_choice == 3 and computer_choice == 2:
            print(f"\nder Computer hat {computer_choice} gewählt. Sie haben gewonnen!")
            user_score += 1
            computer_score = computer_score
            print(score())
        
        
        elif user_choice == computer_choice:
            print("\nAusgleich!")
            computer_score = computer_score
            user_score = user_score
            print(score())            

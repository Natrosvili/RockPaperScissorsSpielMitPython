import random
game_over = False

print("\nHallo und Herzlich Wilkommen zum Rock-Paper-Scissors spiel.")

while not game_over:
    x= input("\nMöchten Sie spielen?\n1. -> Ja\n2. -> Nein\nAntwort: ")
    
    if x == "1" or x == "Ja" or x == "ja" or x == "JA" or x == "j" or x == "J":
        
        computer_choice = random.randint(1, 3)

        user_choice = int(input("\nWas wälhen Sie?\n"
            "'1' für Rock\n"
            "'2' für Paper\n"
            "'3' für Scissors: "))
		
            
        if user_choice > 3 or user_choice < 1:
            print("\nSie haben ein invalid Nummer geschrieben. Sie haben Verloren! ")
        elif user_choice < computer_choice:
            print(f"\nDer Computer hat {computer_choice} gewählt. Sie haben verloren!")
        elif user_choice > computer_choice:
            print(f"\nDer Computer hat {computer_choice} gewählt. Sie haben verloren!")
        elif user_choice == computer_choice:
            print("\nAusgleich!")
    
    elif x == "2" or x == "Nein" or x == "nein" or x == "NEIN" or x == "N" or x == "n":
        print("\nSchade! Schönnen Tag noch")
	break

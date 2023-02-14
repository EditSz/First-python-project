import random


while True:
    computer_greets = input(f"Howdy! I want to play with you rock, paper, scissors, lizard, Spock!")
    player_choice = input("Your choice is: ")
    player_choice = player_choice.lower()
    

    if player_choice == "quit":
        break

    if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors" and player_choice != "lizard" and player_choice != "Spock":
        print("Oh, come on! Please choose a correct one!")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "Spock"])
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("You tied. Try again!")
        continue
    elif player_choice == "paper" and computer_choice == "rock":
        print("Nice, paper covers rock! You win!")
        break
    elif player_choice == "paper" and computer_choice == "Spock":
        print("That is a tricky choice! Paper disproves Spock. You win!")
        break
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Yep, rock crushes the scissors. You win!")
        break
    elif player_choice == "rock" and computer_choice == "lizard":
        print("Oh, it is disgusting but clever! Rock crushes the lizard. You win!")
        break
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Everyone knows that scissors cuts the paper. Meh... You win!")
        break
    elif player_choice == "scissors" and computer_choice == "lizard":
        print("Eww... Scissors decapitates the lizard. You win!")
        break
    elif player_choice == "lizard" and computer_choice == "Spock":
        print("Nifty choice. Lizard poisons Spock. You win!")
        break
    elif player_choice == "lizard" and computer_choice == "paper":
        print("Very clever! Lizard eats paper. You win!")
        break
    elif player_choice == "Spock" and computer_choice == "rock":
        print("Good choice, Spock evaporizes rock. You win!")
        break
    elif player_choice == "Spock" and computer_choice == "scissors":
        print("Yes, Spock smashes the scissors. You win!")
        break

    else:
        print("You lose! Come on, you can do it better! Try again!")
        continue

    next_round = input("Do you want a next round? Y/N: ")
    if next_round != "y":
        break

    

   
    
        
    

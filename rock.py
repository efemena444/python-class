import random

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    user_choice = user_choice.lower()
    
    # Generate computer's choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please try again.")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()

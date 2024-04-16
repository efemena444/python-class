# black.py
from ast import main
import os
import random

# Deal both user and computer a starting hand of 2 random card values.
user_cards = [random.randint(1,11),random.randint(1,11)]
computer_cards = [random.randint(1,11),random.randint(1,11)]

# Detect when computer or user has a blackjack.
if (user_cards[0] == 1 and user_cards[1] == 10) or (computer_cards[0] == 1 and computer_cards[1] == 10):
    is_blackjack = True
else:
    is_blackjack = False

# Calculate the user's and computer's scores based on their card values.
user_score = user_cards[0] + user_cards[1]
computer_score = computer_cards[0] + computer_cards[1]

# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
for i in range(2):
    if user_cards[i] == 1:
        if (user_score + 10) <= 21:
            user_score += 10
        else:
            user_score += 1
    if computer_cards[i] == 1:
        if (computer_score + 10) <= 21:
            computer_score += 10
        else:
            computer_score += 1

# Reveal computer's first card to the user.
print("Dealer's hand: " + str(computer_cards[0]) + " ? ")

# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
while not is_blackjack and user_score < 21:
    # Ask the user if they want to get another card.
    answer = input("Type 'y' to get another card, type 'n' to pass: ")
    if answer == "y":
        user_cards.append(random.randint(1,11))
        user_score += user_cards[len(user_cards) - 1]
        if user_score > 21:
            for i in range(len(user_cards) - 1):
                if user_cards[i] == 1:
                    user_score -= 10
                    break
                elif user_cards[i] == 11:
                    user_score -= 10
                    break
    else:
        # Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
        while computer_score < 16:
            computer_cards.append(random.randint(1,11))
            computer_score += computer_cards[len(computer_cards) - 1]
            if computer_score > 21:
                for i in range(len(computer_cards) - 1):
                    if computer_cards[i] == 1:
                        computer_score -= 10
                        break
                    elif computer_cards[i] == 11:
                        computer_score -= 10
                        break

# Compare user and computer scores and see if it's a win, loss, or draw.
if user_score > 21 and computer_score > 21:
    print("It's a tie!")
elif user_score > 21:
    print("Dealer wins!")
elif computer_score > 21:
    print("You win!")
elif user_score > computer_score:
    print("You win!")
elif computer_score > user_score:
    print("Dealer wins!")
else:
    print("It's a tie!")

# Print out the player's and computer's final hand and their scores at the end of the game.
print("Your final hand: " + str(user_cards) + " Your score: " + str(user_score))
print("Dealer's final hand: " + str(computer_cards) + " Dealer's score: " + str(computer_score))

# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
play_again = input("Would you like to play again? Type 'y' to play, type 'n' to exit: ")
if play_again == "y":
    clear = lambda: os.system('cls') 
    clear()
    main()

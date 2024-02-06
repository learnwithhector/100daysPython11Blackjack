import random
import os
import sys
import time
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(dealt_cards):
    if len(dealt_cards) == 2 and sum(dealt_cards) == 21:
        return 0
    elif 11 in dealt_cards and sum(dealt_cards) > 21:
        dealt_cards.remove(11)
        dealt_cards.append(1)
    return sum(dealt_cards)


def compare(user_score, opponent_score):
    if user_score == opponent_score or (user_score > 21 and opponent_score > 21):
        return "It's a draw"
    elif user_score == 0:
        return "Blackjack! You win"
    elif opponent_score == 0:
        return "Computer has blackjack! You lose"
    elif user_score > 21:
        return "You are bust! You lose"
    elif opponent_score > 21:
        return "Computer is bust! You win"
    else:
        if user_score > opponent_score:
            return "You win!"
        else:
            return "You lose!"


def main():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    print(user_cards)
    print(computer_cards)

    player_score = calculate_score(user_cards)
    while player_score < 21 and player_score != 0:
        print(f"Your score is {player_score}")
        another = input("Do you want another card (y/n): ").casefold()
        if another == 'y' or another == 'yes':
            user_cards.append(deal_card())
            print(f"Your cards are now {user_cards}")
            player_score = calculate_score(user_cards)
        elif another == 'n' or another == 'no':
            break
        else:
            continue

    computer_score = calculate_score(computer_cards)
    if computer_score == 0:
        pass
    elif computer_score >= 17:
        print(f"Computer cards are {computer_cards}")
        print(f"Computer score is {computer_score}")
    else:
        while computer_score < 17:
            print("Computer is thinking")
            time.sleep(2)
            computer_cards.append(deal_card())
            print(f"Computer cards are now {computer_cards}")
            computer_score = calculate_score(computer_cards)
            print(f"Computer score is now {computer_score}")

    print(compare(player_score, computer_score))

    again = input("Play another game? press 'y' (anything else exits): ").casefold()
    if again == 'y' or again == 'yes':
        os.system('cls')
        main()
    else:
        print("GOODBYE!")
        sys.exit()


main()

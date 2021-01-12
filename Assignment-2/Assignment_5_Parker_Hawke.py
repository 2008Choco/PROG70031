"""
Assignment 5 for PROG-70030, Python
Author: Parker Hawke
"""

import random

def main():
    """
    The main method.
    """
    print("Welcome to Blackjack.")

    while True:
        padded_print("------------------------------------------------")

        # Draw cards for the player
        first_card = draw_card()
        second_card = draw_card()
        player_value = first_card + second_card
        padded_print(f'You draw a {first_card} and a {second_card}. Your total is {player_value}.')

        # Draw cards for the dealer (one hidden)
        first_card = draw_card()
        second_card = draw_card()
        padded_print(f'The dealer draws a {first_card} and a hidden card.')
        dealer_value = first_card + second_card

        # Do the player's turn
        draw = 0
        while player_value < 21:
            player_move = required_input(
                "Hit or stand?"
                if draw == 0 else
                f'Hit! You draw a {draw}. Your total is {player_value}. Hit or stand?', 'h', 's'
            )

            if player_move == 'h':
                draw = draw_card()
                player_value += draw

                if player_value >= 21:
                    padded_print(
                        f'You drew a {draw} and busted (total: {player_value}).'
                        if player_value > 21 else
                        f'You drew a {draw} and achieved Blackjack. Standing.'
                    )
                    break

                continue

            # Only called if the option 's' is used - to stand
            padded_print(f'You stand at {player_value}.')
            break

        # Do the dealer's turn
        padded_print(f'The dealer reveals the hidden card of {second_card} and has a total of {dealer_value}.')
        while dealer_value < 21:
            if dealer_value < 16:
                draw = draw_card()
                dealer_value += draw
                padded_print(f'Hit! The dealer draws a {draw}. The dealer\'s total is {dealer_value}.')

                if dealer_value > 21:
                    padded_print("The dealer busts!")
                continue

            padded_print(f'The dealer stays at {dealer_value}.')
            break

        # Calculate who won
        padded_print(f'Your total is {player_value} and the dealer\'s total is {dealer_value}.')
        if player_value > 21 and dealer_value > 21:
            padded_print("It's a draw! Both the player and dealer have busted.")
        elif player_value <= 21 and (player_value > dealer_value or dealer_value > 21):
            padded_print("You win!")
        elif player_value == dealer_value or (dealer_value <= 21 and (dealer_value > player_value or player_value > 21)):
            padded_print("The dealer wins!")

        # Ask whether or not to start a new game
        if required_input("Do you wish to start a new game", 'y', 'n') == 'n':
            break

    padded_print("Thank you for playing!")

def required_input(query, *expected_values):
    """
    Request user input with an expected set of values.
    The user will be constantly polled for a value until one of the expected values are input.
    """
    if len(expected_values) == 0:
        raise Exception("Unexpected length of expected_values tuple. Should be > 0.")

    query += f' ({"/".join(expected_values)}): '
    while True:
        user_input = input(f'\n{query}').lower()
        if user_input in expected_values:
            return user_input

def draw_card():
    """
    Generate a random card value from 1 to 10 (inclusive).
    """
    return random.randint(1, 10)

def padded_print(string):
    """
    Print a string with newline padding on the top and bottom.
    """
    print(f'\n{string}\n')

if __name__ == '__main__':
    main()

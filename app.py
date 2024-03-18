from random import choice
import os

items = ["rock", "paper", "scissor"]
player1 = input("Type Player's name: ")


def game():
    while True:
        bot_choice = choice(items)
        player_choice = input(f'{player1} choose one: rock | paper | scissor [Type "exit" anytime to exit the game]: ')
        if player_choice == 'exit':
            os.system('cls')
            print('### Game Over ###')
            break
        if player_choice not in items:
            print('Invalid option! Please choose one of the options: rock | paper | scissor')
        if bot_choice == player_choice:
            print(f'DRAW! The robot chose {bot_choice} and {player1} chose {player_choice}')
        elif bot_choice == 'rock' and player_choice == 'paper':
            print(f'You WIN! The robot chose {bot_choice} and {player1} chose {player_choice}')
        elif bot_choice == 'rock' and player_choice == 'scissor':
            print(f'You LOST! The robot chose {bot_choice} and {player1} chose {player_choice}')
        elif bot_choice == 'paper' and player_choice == 'rock':
            print(f'You LOST! The robot chose {bot_choice} and {player1} chose {player_choice}')
        elif bot_choice == 'paper' and player_choice == 'scissor':
            print(f'You WIN! The robot chose {bot_choice} and {player1} chose {player_choice}')
        elif bot_choice == 'scissor' and player_choice == 'rock':
            print(f'You WIN! The robot chose {bot_choice} and {player1} chose {player_choice}')
        elif bot_choice == 'scissor' and player_choice == 'paper':
            print(f'You LOST! The robot chose {bot_choice} and {player1} chose {player_choice}')


game()

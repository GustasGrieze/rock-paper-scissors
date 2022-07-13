import time
import logging
from datetime import datetime
from functions import user_won, user_lost, user_tied, write_information_to_file, calculate_user_win_rate, print_user_choice, select_computer_choice
from python_pictures import rock, paper, scissors

games_played = 0
games_won = 0
games_lost = 0
games_tied = 0

print("\n----Welcome to Rock Paper Scissors----\n")
choice = input("Which do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")

while True:
    try:
        choice = int(choice)            
    except ValueError:
        choice = input("\nThat's not a number! Pick again!\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        continue
    
    if choice > 2 or choice < 0:
        choice = input("\nOops! that's not one of the options! Pick again!\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        continue

    print_user_choice(choice, rock, paper, scissors)

    print("\nThe computer chose...: ")
    time.sleep(2.5)

    image_chosen = select_computer_choice(rock, paper, scissors)

    if user_won(choice, image_chosen):
        print("\n---- You won! ----\n\n")
        logging_result = "WON!"
        games_won += 1
    if user_lost(choice, image_chosen):
        print("\n---- You lost! ----\n\n")
        logging_result = "LOST!"
        games_lost += 1
    if user_tied(choice, image_chosen):
        print("\n---- It's a tie! ----\n\n")
        logging_result = "TIED!"
        games_tied += 1

    games_played += 1

    logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info(f"You {logging_result}")

    continue_playing = str.casefold(input("If you would like to continue playing type 0 for Rock, 1 for Paper or 2 for Scissors. \nIf you wish to exit the game type 'Exit': "))
    if continue_playing == "exit":
        print("\n-- The program has ended --")
        break
    else:
        choice = continue_playing
        continue


if games_played >= 1:
    write_information_to_file(f"""
Play session date: {datetime.now()}
Games played: -- {games_played} --
Games won: {games_won}
Games lost: {games_lost}
Games tied: {games_tied}
Session win rate: {calculate_user_win_rate(games_played, games_won, games_tied)}%\n\n""")


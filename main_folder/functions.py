import random

def print_user_choice(choice: int, rock: str, paper: str, scissors: str) -> None:
    if choice == 0:
        print(f"\nYou chose: \n{rock}")
    elif choice == 1:
        print(f"\nYou chose: \n{paper}")
    elif choice == 2:
        print(f"\nYou chose: \n{scissors}")
        
def select_computer_choice(rock: str, paper: str, scissors: str) -> int:
    game_images = [rock, paper, scissors]
    image_chosen = random.randint(0, len(game_images) - 1)
    print(game_images[image_chosen])
    return image_chosen

def user_won(choice: int, image_chosen: int) -> bool:
    return (choice == 0 and image_chosen == 2) or (choice == 1 and image_chosen == 0) or (choice == 2 and image_chosen == 1)

def user_lost(choice: int, image_chosen: int) -> bool:
    return (choice == 1 and image_chosen == 2) or (choice == 0 and image_chosen == 1) or (choice == 2 and image_chosen == 0)

def user_tied(choice: int, image_chosen: int) -> bool:
    return choice == image_chosen

def write_information_to_file(data: str) -> None:
    with open("../results.txt", 'a') as f:
        f.write(data)

def calculate_user_win_rate(games_played: int, games_won: int, games_tied: int) -> int:
    games_played = games_played - games_tied
    try:
        return round(games_won / games_played * 100)
    except Exception as e:
        return 0

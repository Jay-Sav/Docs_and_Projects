#Import External Files
from services.title import title_screen
from services.clear_screen import clear_screen
from services.loading_screen import progress_bar
from services.tally import tally_bar
from player_data.player_data import GameManager, Player

# Variables and list for get_player_names
    
player_count = 1
entry_count = 1

manager = GameManager()


#Get Player Names and Display    
def get_player_names():
    global player_count, entry_count
    while True:
        print(f"Enter Player {player_count} Name: ", end="")
        user_input = input().strip().lower().capitalize()
        if user_input.isalpha() and user_input != "":
            try:
                player = Player(user_input, 0)
                manager.add_player(player)
                print(f"Player {player_count}: {user_input} added successfully.\n")
                player_count += 1
                entry_count += 1
            except Exception as e:
                print(f"Error adding player: {e}")
            print(f"Would you like to add another player? (y/n): ", end="")
            user_choice = input().strip().lower()
            if user_choice not in ('y', 'yes'):
                break
              
def main():
    title_screen()
    progress_bar()
    input(f'Ready to Play? Press Enter to continue\n')
    clear_screen()
    title_screen()
    get_player_names()
    clear_screen()
    title_screen()
    print("Current Leaderboard")
    print("----------------------\n")
    manager.print_players()
    input('Press Enter to continue\n')
    clear_screen()
    title_screen()

    #Get Number of Rounds to Play
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? (3, 6, or 9): "))
            if rounds in [3, 6, 9]:
                rounds = manager.roundsToPlay(rounds)
                break
            else:
                print("Invalid input. Please enter 3, 6, or 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"You have chosen to play {rounds} rounds.\n Game is starting...")
    progress_bar()
    input("Game has loaded! Press Enter to continue.")
    clear_screen()
    title_screen()
    manager.gameState(rounds)

    


if __name__ == '__main__':
    main()



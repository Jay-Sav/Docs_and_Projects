#Importing the necessary modules and functions from other files in the project
from src.ui.title_screen import print_title
from src.ui.loading_screen import progress_bar
from src.ui.dash_line import print_dash_line
from src.ui.training_history_title import print_training_history_title
from src.services.clear_screen import clear_screen
from src.services.get_time import get_current_time
from src.models.user_data import UserData
from src.services.health_metrics import calculate_bmi
from src.services.training_service import ( 
    list_training_options, validate_training_option_selection, get_training_sub_option, validate_training_sub_option_selection,
    get_training_duration, write_user_data_to_csv, display_user_training_data,get_user_weight,get_user_height,confirm_height_and_weight)


#Main 
def main():

#Screen 1 - Title Screen and Loading Screen
    print_title()
    progress_bar(1)
    clear_screen()
# End of Screen 1 - Title Screen and Loading Screen


#Screen 2 - Title Screen and Time 
    print_title()
    print_dash_line()
    print("\n")
    current_time = get_current_time()
    continue_prompt = input("\nPress [ENTER] to continue...")
    clear_screen()
    print_title()
    print(f"Current date and time: {current_time}\n")
# End of Screen 2 - Title Screen and Time


########## Screen 3 - Display Existing Training Data if user would like to view it ########## #################################################

    while True:

        user_choice = input("\nWould you like to view your existing training data? (Y/N): ").strip().lower()

        if user_choice not in ('y', 'yes','n', 'no'):
            print("\nInvalid input. Please enter 'Y' to view existing training data or 'N' to skip.\n")
            continue

        elif user_choice in ('n', 'no'):
            print("\nSkipping view of existing training data.\n")
            break

        elif user_choice in ('y', 'yes'):
            username = str(input("\nPlease enter your username to view your training data: ").strip())
            existing_data = display_user_training_data(username)
            if existing_data:
                        print_training_history_title()
                        print(f"\nExisting training data for user {username}:\n")
                        for row in existing_data:
                            print(row)
            else:
                print(f"\nNo existing training data found for user {username}.\n")
            break

    continue_prompt = input("\nPress [ENTER] to continue...")
    clear_screen()

 ########## End of Screen 3 - Display Existing Training Data ###########################################################


########### Screen 4 - Gather User Weight, Training Option, Sub-Option, and Duration ###########################################################
    while True:
        weight = get_user_weight()    
        height = get_user_height()
        while not confirm_height_and_weight(height, weight):
            print("\nLet's try again.\n")
            weight = get_user_weight()    
            height = get_user_height()
        print_dash_line()

        see_bmi = input("\nWould you like to calculate your BMI? (Y/N): ").strip().lower()
        if see_bmi in ('y', 'yes'):
            user_bmi = calculate_bmi(weight, height)
            print(f"\nYour BMI is: {user_bmi:.2f}\n")
        else:
            print("\nSkipping BMI calculation.\n")
        print_dash_line()

        #Prints the available training options
        options_data = list_training_options()

        #Get the user's training option selection and validates it against the list of available options, loop until a valid selection is made.
        while True:
            try:
                training_option_selected = int(input("\nHow did you you train today (Enter the corresponding number): ").strip())
                training_option_selected = validate_training_option_selection(training_option_selected, options_data)
                break
            except ValueError:
                print("\nINVALID INPUT. Please enter a valid number for your training option.\n")


        print(f"\nWhat specific type of {options_data[training_option_selected]} did you do today?\n"+"--" * 30)
        display_sub_option = get_training_sub_option(int(training_option_selected))

        #Validate the user's sub-option selection and loop until a valid selection is made.
        while True:
            try:
                training_sub_option_selected = int(input("\nEnter the corresponding number for your specific training type: ").strip())
                training_sub_option_selected = validate_training_sub_option_selection(training_sub_option_selected, display_sub_option)
                break
            except ValueError:
                print("\nINVALID INPUT. Please enter a valid number for your specific training type.\n")
        
        print(f"\nYou selected: {options_data[training_option_selected]} - {display_sub_option[int(training_sub_option_selected)]}")
        training_option_selected = options_data[training_option_selected]
        training_sub_option_selected = display_sub_option[int(training_sub_option_selected)]
        print_dash_line()
        training_duration = get_training_duration()
        print(f"\nYour training duration was: {training_duration} minutes\n")

        user  = UserData(weight,height, training_option_selected, training_sub_option_selected, training_duration)
        user.print_user_data()

        print_dash_line()
        confirm_data = input("\nIs the above information correct? (Y/N): ").strip().lower()
        while True:
            if confirm_data not in ('y', 'yes','n', 'no'):
                print("\nInvalid input. Please enter 'Y' to confirm or 'N' to re-enter your data.\n")
                confirm_data = input("\nIs the above information correct? (Y/N): ").strip().lower()
            else:
                break
        if confirm_data == 'y' or confirm_data == 'yes':
           username = str(input("\nPlease enter your username: ").strip())
           write_user_data_to_csv(user, username,current_time)
           print(f"\nYour data has been saved to {username}_Training_Data.csv in your Documents folder.\n")
           break
        else:
            print("\nLet's try again.\n")
            progress_bar(1)
            clear_screen()
            print_title()
            
    input("\nSession complete. Press [ENTER] to close this window...")

########### End of Screen 4 - Gather User Weight, Training Option, Sub-Option, and Duration ###########################################################

if __name__ == "__main__":
    main()
  
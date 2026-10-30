import csv
from pathlib import Path

def get_user_weight():
    while True:
        try:
            weight = float(input("\nPlease enter your weight in pounds (lbs): ").strip())
            if weight <= 50 or weight > 700:
                print("Invalid input. Please enter a valid weight between 50 and 700 lbs.")
            else:
                return weight
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_user_height():
    while True:
        try:
            height = float(input("\nPlease enter your height in inches (in): ").strip())
            if height <= 36 or height > 96:
                print("Invalid input. Please enter a valid height between 36 and 96 inches.")
            else:
                return height
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def confirm_height_and_weight(height, weight):
    print(f"\nYour Weight is: {weight} lbs and your Height is: {height} inches..is that right? (Y/N): ", end="")
    confirm = input().strip().lower()
    while confirm not in ('y', 'yes', 'n', 'no'):
        print("\nInvalid input. Please enter 'Y' to confirm or 'N' to re-enter your data.\n")
        confirm = input("Is this information correct? (Y/N): ").strip().lower()
    if confirm in ('y', 'yes'):
        return True
    else:
        return False

###Prints training_options then returns training options to variable options_data in main function
def list_training_options():
    training_options= {
        1: "Resistance Training",
        2: "High-Intensity Interval Training (HIIT)",
        3: "Endurance Training",
        4: "Hybrid Training",
        5: "Active Recovery"
    }
    for counter,option in enumerate(training_options.values(), 1):
            print(f"{counter}:{option}")
    return training_options

### Take training option selected and validate it against the options_data dictionary. If invalid, prompt user to re-enter until valid.
def validate_training_option_selection(training_option_selected, options_data):
    while training_option_selected not in options_data:
        print("\nINVALID INPUT. Please enter a valid number corresponding to the training option.\n")
        training_option_selected = int(input("How did you you train today (Enter the corresponding number): \n").strip())
    return training_option_selected


#Present and return Sub-Options based on Training Option Selected
def get_training_sub_option(training_option_selected):

    main_option = training_option_selected

    sub_options = {
        1:{1: "Hypertrophy (Muscle Growth) (8-12 reps)",
            2: "Strength Training (1-6 reps)",
            3: "Power Training (1-5 reps with explosive movements)"
           },

        2:{1: "Short Intervals (20-30 seconds work, 10-15 seconds rest)",
            2: "Long Intervals (1-4 minutes work, equal rest)",
            3: "Tabata (20 seconds work, 10 seconds rest for 4 minutes)"
           },

        3:{1: "Long Slow Distance (LSD) (steady pace for 60+ minutes)",
            2: "Tempo Runs (comfortably hard pace for 20-40 minutes)",
            3: "Moderate Intensity Steady State (MISS) (jogging or cycling at a steady pace)"
           },

        4:{1: "CrossFit (varied functional movements performed at high intensity)",
            2: "Circuit Training (series of exercises performed in sequence with minimal rest)",
            3: "Mixed Modal Training (combination of strength, endurance, and cardio exercises)"
           },
           
        5:{1: "Yoga (gentle stretching and breathing exercises)",
            2: "Light Walking (easy pace for 20-30 minutes)",
            3: "Foam Rolling (self-myofascial release to improve mobility)"
        }
    }

    display_sub_options = sub_options[main_option]
    for option_number, option_description in display_sub_options.items(): 
        print(f"{option_number}. {option_description}")
    return display_sub_options


def validate_training_sub_option_selection(training_option_sub_option_selected, display_sub_option):
    while True:
        try:
            training_option_sub_option_selected = int(training_option_sub_option_selected)
            if training_option_sub_option_selected not in display_sub_option:
                print(f"\nINVALID INPUT of {training_option_sub_option_selected}. Please enter a valid number corresponding to the training sub-option.\n")
                training_option_sub_option_selected = int(input("Enter the corresponding number for your specific training type: ").strip())
            else:
                return training_option_sub_option_selected
        except ValueError:
            print(f"\nINVALID INPUT of {training_option_sub_option_selected}. Please enter a valid number corresponding to the training sub-option.\n")
            training_option_sub_option_selected = int(input("Enter the corresponding number for your specific training type: ").strip())
  
#Get Training Duration
def get_training_duration():
    try:
        duration = float(input("\nEnter the duration of your training session in minutes: ").strip())
        if duration <= 0 or duration > 300:
            raise ValueError("Duration must be between 0 and 300 minutes.")
        return duration
    except ValueError as e:
        print(f"Invalid input. Please enter a valid number. ({e})")
        return get_training_duration()

# Write user data to CSV file located in the user's Documents directory under Documents -- > "Recovery_Suite_Data"
def write_user_data_to_csv(user, username, current_time):
    documents_dir = Path.home() / "Documents"/"Recovery_Suite_Data" # Directory to store the user's training data CSV file
    file_path = documents_dir / f"{username}_Training_Data.csv" # CSV file to store the user's training data
    documents_dir.mkdir(parents=True, exist_ok=True)  # Ensure the Documents directory exists

    file_exists = file_path.exists() # Check if the CSV file already exists

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Weight", "Training Option Selected", "Training Sub-Option Selected", "Training Duration", "Time Recorded"])
        writer.writerow([user.weight, user.training_option_selected, user.training_sub_option_selected, user.training_duration, current_time])

# Function to display the user's training data from the CSV file 
def display_user_training_data(username):
    documents_dir = Path.home() / "Documents"/"Recovery_Suite_Data" # Directory to store the user's training data CSV file
    file_path = documents_dir / f"{username}_Training_Data.csv" # CSV file to store the user's training data
    if not file_path.exists():
        print(f"No training data found for user {username}.")
        return
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)
class UserData:
    def __init__(self, weight, training_option_selected, training_sub_option_selected, training_duration):
        self.weight = weight
        self.training_option_selected = training_option_selected
        self.training_sub_option_selected = training_sub_option_selected
        self.training_duration = training_duration

    def print_user_data(self):
        print("User Data\n"+ "-" * 30)
        print(f"Weight: {self.weight} lbs")
        print(f"Training Option Selected: {self.training_option_selected}")
        print(f"Training Sub-Option Selected: {self.training_sub_option_selected}")
        print(f"Training Duration: {self.training_duration} minutes")
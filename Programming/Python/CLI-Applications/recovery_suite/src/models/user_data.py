class UserData:
    def __init__(self, weight, height, training_option_selected, training_sub_option_selected, training_duration):
        self.weight = weight
        self.height = height
        self.training_option_selected = training_option_selected
        self.training_sub_option_selected = training_sub_option_selected
        self.training_duration = training_duration
        

    def print_user_data(self):
        print("User Data\n"+ "-" * 30)
        print(f"Weight: {self.weight} lbs")
        print(f"Height: {self.height} inches")
        print(f"Training Option Selected: {self.training_option_selected}")
        print(f"Training Sub-Option Selected: {self.training_sub_option_selected}")
        print(f"Training Duration: {self.training_duration} minutes")
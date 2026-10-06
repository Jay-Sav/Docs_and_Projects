def get_training_sub_option(training_option_selected):

    sub_option_choice = training_option_selected

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
    return sub_options[sub_option_choice]



    
sub_option = get_training_sub_option(1)
for option_number, option_description in sub_option.items():
    print(f"{option_number}. {option_description}")




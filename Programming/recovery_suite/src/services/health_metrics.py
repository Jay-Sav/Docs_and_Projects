def calculate_bmi():
    user_input = ""
    while user_input != "q":
        try:
            weight = int(input("Enter weight (in pounds): "))
            height = int(input("Enter height (in inches): "))

            bmi = (float(weight) / float(height * height)) * 703
            print(f"BMI: {bmi}")
            print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov
        except ValueError:
            print("Could not calculate health info.\n")
        except ZeroDivisionError:
            print("Invalid height entered. Must be > 0.")

        user_input = input('Enter any key ("q" to quit): ')

class FoodItem:
    # Define constructor with parameters to initialize instance attributes (name, fat, carbs, protein)
    def __init__(self, name="Water", fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) +
                    (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print(f"Nutritional information per serving of {self.name}:")
        print(f"  Fat: {self.fat:.2f} g")
        print(f"  Carbohydrates: {self.carbs:.2f} g")
        print(f"  Protein: {self.protein:.2f} g")

def heart_rate():
    try:
        user_age = int(input("Enter your age: "))

        if user_age < 0:
            raise ValueError("Invalid age")

        # Source: https://www.heart.org/en/healthy-living/fitness
        avg_max_heart_rate = 220 - user_age

        print(f"Avg: {avg_max_heart_rate}")

    except ValueError as excpt:
        print(f"Error: {excpt}")
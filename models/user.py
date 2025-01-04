class User:
    def __init__(self):
        self.preferences = {
            "age": None,
            "height": None,
            "budget": None,
            "preferred_type": None,
            "fuel_type": None,
            "transmission": None,
            "country": None,
            "winter_driver": None,
        }

    def gather_user_preferences(self):
        try:
            # self.preferences["age"] = int(input("Enter your age: "))
            # self.preferences["height"] = int(input("Enter your height (in cm): "))
            # self.preferences["budget"] = int(input("Enter your budget (in $): "))
            # self.preferences["preferred_type"] = input("Enter your preferred car type (SUV, Sedan, etc.): ").strip().lower()
            # self.preferences["fuel_type"] = input("Enter your preferred fuel type (Gasoline, Diesel, Electric, etc.): ").strip().lower()
            # self.preferences["transmission"] = input("Enter your preferred transmission (Manual or Automatic): ").strip().lower()
            # self.preferences["country"] = input("Enter your country: ").strip().capitalize()
            self.preferences["age"] = 26
            self.preferences["height"] = 182
            self.preferences["budget"] = 1500
            self.preferences["preferred_type"] = "Sedan"
            self.preferences["fuel_type"] = "Gasoline"
            self.preferences["transmission"] = "Manual"
            self.preferences["country"] = "Lithuania"
            self.preferences["winter_driver"] = "Yes"
        except ValueError:
            print("Invalid input. Please enter correct data.")
            self.gather_user_preferences()

    def get_user_preferences(self):
        return f"""
        User Preferences:
        - Age: {self.preferences['age']}
        - Height: {self.preferences['height']} cm
        - Budget: {self.preferences['budget']}
        - Preferred Type: {self.preferences['preferred_type']}
        - Fuel Type: {self.preferences['fuel_type']}
        - Transmission: {self.preferences['transmission']}
        - Country: {self.preferences['country']}
        - Will be driving in winter: {self.preferences['winter_driver']}
        """

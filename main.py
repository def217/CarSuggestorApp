from models.client import OpenAIClient
from models.user import User
from utils.validators import validate_menu_option
from utils.prints import dash_line
from managers.car_recommendation_system import CarRecommendationSystem


class CarRecommendationApp:
    def __init__(self):
        self.client = OpenAIClient()
        self.user = User()
        self.system = CarRecommendationSystem(self.client, self.user)

    def run(self):
        print("Welcome to the Car Recommendation Program!\n")
        print("Please input your preferences.")
        self.user.gather_user_preferences()

        self.cars = self.system.get_car_recommendations()

        if len(self.cars) > 0:
            self.display_main_menu()

    def display_main_menu(self):
        show_main_menu = True
        
        while show_main_menu:
            dash_line()
            print("1. Generate more car options")
            print("2. Compare cars")
            print("3. More details about a specific car")
            print("4. Show all data on a car")
            print("5. Exit")
            dash_line()

            option = validate_menu_option("Choose a menu option (1 - 5): ", 5)

            match option:
                case 1:
                    self.system.get_car_recommendations()
                case 2:
                    self.system.compare_cars()
                case 3:
                    self.system.query_car_details()
                case 4:
                    self.system.print_car_info()
                case 5:
                    return


if __name__ == "__main__":
    app = CarRecommendationApp()
    app.run()

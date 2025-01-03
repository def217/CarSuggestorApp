from models.client import OpenAIClient
from models.user import User
from managers.car_recommendation_system import CarRecommendationSystem

class CarRecommendationApp:
    def __init__(self):
        self.client = OpenAIClient()
        self.user = User()
        self.system = CarRecommendationSystem(self.client, self.user)

    def run(self):
        print("Welcome to the Car Recommendation Program!")
        self.user.gather_user_preferences()
        
        self.system.get_car_recommendations()
        
        self.display_main_menu()
            
    def display_main_menu(self):
        while True:
            self.system.display_cars()
            
            print("-------------------------------------")
            print("1. Generate more car options.")
            print("2. Compare cars.")
            print("3. More details about a specific car.")
            print("-------------------------------------")
            
            option = input("Choose an option (1 - 3): ")
            
            match option:
                case "1":
                    self.system.get_car_recommendations()
                    ...
                case "2":
                    self.system.compare_cars()
                    ...
                case "3":
                    self.system.query_car_details()


if __name__ == "__main__":
    app = CarRecommendationApp()
    app.run()
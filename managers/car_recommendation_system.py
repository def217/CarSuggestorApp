from models.car import Car
from utils.prompts import generate_car_prompt, generate_more_info_on_car_prompt, compare_cars_based_on_user_prefs

class CarRecommendationSystem:
    def __init__(self, api_client, user):
        self.cars = []
        self.api_client = api_client
        self.user = user
        
    def get_car_recommendations(self):
        prompt = generate_car_prompt(self.user)
                
        response = self.api_client.generate_response(prompt)
        
        try:
            for car in response:
                self.cars.append(Car(**car))
            
            return self.cars
        except (ValueError, SyntaxError) as e:
            print(e)
            print("Failed to parse recommendations. Please try again.")
            return []
        
    def get_more_info_on_car(self, selected_car):
        prompt = generate_more_info_on_car_prompt(selected_car)
        
        response = self.api_client.generate_response(prompt)
        try:
            selected_car.set_add_info(
                response['model_updates'], 
                response['reliability'], 
                response['common_issues'], 
                response['maintenance_cost'], 
                response['engine_options'], 
                response['ownership_experience'], 
                response['availability'], 
                response['resale_value'], 
                response['known_issues'], 
                response['tips']
            )
        except (ValueError, SyntaxError):
            print("Failed to parse recommendations. Please try again.")
            return []
        
    def compare_cars(self):
        prompt = compare_cars_based_on_user_prefs(self.user, self.cars)
        
        response = self.api_client.generate_response(prompt)
    
        for compared_car in response:
            if compared_car['best_option'] == "Yes":
                print(f"{compared_car['name']} is the best car based on your preferances.")
                
                for car in self.cars:
                    if car.id == compared_car['id']:
                        car.best_option = "Yes"
                        print("Updated best option.")

    def print_compared_cars(self, compared_car):
        return (f"{compared_car['name']}\n"
                f"{compared_car['sustainability']}\n"
                f"{compared_car['driving_conditions']}\n"
                f"{compared_car['reliability']}\n"
                f"{', '.join(compared_car['engine_options'])}\n"
                f"{compared_car['maintenance']}\n"
                f"{compared_car['best_option']}")
    
    def display_cars(self):
            if not self.cars:
                print("No recommendations available.")
                return
            print("\nHere are your car recommendations:\n")
            self.print_cars()

    def query_car_details(self):
        if not self.cars:
            print("No cars to query.")
            return

        print("You can ask for more details about these cars:")
        self.print_cars()

        try:
            choice = int(input("Enter the number of the car you want to learn more about: ")) - 1
            if 0 <= choice < len(self.cars):
                selected_car = self.cars[choice]
                self.get_more_info_on_car(selected_car)
                print("Here are more details about this specific model:")
                print(selected_car.main_car_info())
            else:
                print("Invalid input. Please enter a number.")
        except ValueError as e:
            print(e)
            print("Error getting information about a car.")
            
    def print_cars(self):
        for idx, car in enumerate(self.cars, start=1):
            print(f"{idx}. {car}")
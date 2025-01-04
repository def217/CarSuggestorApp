from models.car import Car
from utils.prints import get_compared_car, print_cars, main_car_info
from utils.prompts import (
    generate_car_prompt,
    generate_more_info_on_car_prompt,
    compare_cars_based_on_user_prefs,
)
from utils.validators import validate_menu_option


class CarRecommendationSystem:
    def __init__(self, api_client, user):
        self.cars = []
        self.api_client = api_client
        self.user = user

    def get_car_recommendations(self):
        prompt = generate_car_prompt(self.user, self.cars)

        response = self.api_client.generate_response(prompt)

        try:
            for car in response:
                self.cars.append(Car(**car))
            self.display_cars()

            return self.cars
        except (TypeError, ValueError, SyntaxError):
            print("Failed to parse recommendations. Please try again.")
            return []

    def get_more_info_on_car(self, selected_car):
        prompt = generate_more_info_on_car_prompt(selected_car)

        response = self.api_client.generate_response(prompt)
        try:
            selected_car.set_add_info(
                response["model_updates"],
                response["reliability"],
                response["common_issues"],
                response["maintenance_cost"],
                response["engine_options"],
                response["ownership_experience"],
                response["availability"],
                response["resale_value"],
                response["known_issues"],
                response["tips"],
            )
        except (ValueError, SyntaxError):
            print("Failed to parse recommendations. Please try again.")
            return []

    def compare_cars(self):
        prompt = compare_cars_based_on_user_prefs(self.user, self.cars)

        response = self.api_client.generate_response(prompt)

        for compared_car in response:
            print(get_compared_car(compared_car))
            if compared_car["best_option"] == "Yes":
                best_car_option = compared_car
                for car in self.cars:
                    if int(car.id) == int(compared_car["id"]):
                        car.best_option = "Yes"

        if best_car_option:
            print(
                f"{best_car_option['name']} is the best car based on your preferances."
            )

    def display_cars(self):
        if not self.cars:
            print("No recommendations available.")
            return
        print("Car recommendations list:\n")
        print_cars(self.cars)

    def query_car_details(self):
        if not self.cars:
            print("No cars to query.")
            return

        print("You can ask for more details about these cars:")
        print_cars(self.cars)

        try:
            choice = (
                validate_menu_option(
                    "Enter the number of the car you want to learn more about: ",
                    len(self.cars),
                )
                - 1
            )
            if 0 <= choice < len(self.cars):
                selected_car = self.cars[choice]
                self.get_more_info_on_car(selected_car)
                print("Here are more details about this specific model:\n")
                print(main_car_info(selected_car))
            else:
                print("Invalid input. Please enter a number.")
        except ValueError as e:
            print(e)
            print("Error getting information about a car.")

    def print_car_info(self):
        print_cars(self.cars)
        try:
            choice = (
                validate_menu_option(
                    "Enter the number of the car you want more information about: ",
                    len(self.cars),
                )
                - 1
            )

            selected_car = self.cars[choice]

            print("Here is the information about this specific model:\n")
            print(selected_car.display_data())

        except ValueError as e:
            print(e)
            print("Error getting information about a car.")

import openai
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_response(self, prompt):
        print("\nGenerating response...\n")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Provide output in valid JSON."},
                    {"role": "user", "content": prompt}
                    ],
                temperature=0.5,
                max_tokens=500,
            )
            
            if response.choices[0].finish_reason == "stop":    
                print(response)
                response_data = json.loads(response.choices[0].message.content)
            else:
                print("More tokens needed.")
            
            return response_data

        except openai.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
            pass
        except openai.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass
        except openai.APITimeoutError:
            print("OpenAI API request timed out.")
        except Exception as e:
            print(e)
            print("Something went wrong with the OpenAI API request.")

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

class Car:
    def __init__(self, make, model, price, year_from, year_until, pros, cons):
        self.make = make
        self.model = model
        self.price = price
        self.year_from = year_from
        self.year_until = year_until
        self.pros = pros
        self.cons = cons
        self.reliability = None
        self.common_issues = []
        self.maintenance_cost = None
        self.engine_options = []
        self.ownership_experience = {}
        self.availability = None
        self.resale_value = None
        self.known_issues = []
        self.tips = []
    
    def set_add_info(self, model_updates, reliability, common_issues, maintenance_cost, engine_options, ownership_experience, availability, resale_value, known_issues, tips):
        self.model_updates = model_updates
        self.reliability = reliability
        self.common_issues = common_issues
        self.maintenance_cost = maintenance_cost
        self.engine_options = engine_options
        self.ownership_experience = ownership_experience
        self.availability = availability
        self.resale_value = resale_value
        self.known_issues = known_issues
        self.tips = tips
        
    def main_car_info(self):
        return (f"{self.year_from}-{self.year_until} {self.make} {self.model} ({self.price})\n"
                f"Pros: {', '.join(self.pros)}\n"
                f"Cons: {', '.join(self.cons)}\n"
                f"Model updates: {self.model_updates}\n"
                f"Reliability: {self.reliability}\n"
                f"Common issues: {', '.join(self.common_issues)}\n"
                f"Maintenance cost: {self.maintenance_cost}\n"
                f"Engine options:\n      {self.print_engines()}\n"
                f"Pros: {', '.join(self.ownership_experience["pros"])}\n"
                f"Cons: {', '.join(self.ownership_experience["cons"])}\n"
                f"Availability: {self.availability}\n"
                f"Resale value: {self.resale_value}\n"
                f"Known issues: {', '.join(self.known_issues)}\n"
                f"Tips: {', '.join(self.tips)}\n")
        
    def all_car_info(self):
        return (f"{self.year_from}-{self.year_until} {self.make} {self.model} ({self.price})\n"
                f"Pros: {', '.join(self.pros)}\n"
                f"Cons: {', '.join(self.cons)}\n")
        
    def print_engines(self):
        engine_details = []
        for option in self.engine_options:
            engine_details.append(f"{option['engine']}, {option['description']}")
        return "\n      ".join(engine_details)

    
    def __str__(self):
        return (f"{self.year_from}-{self.year_until} {self.make} {self.model}")

class CarRecommendationSystem:
    def __init__(self, api_client, user):
        self.cars = []
        self.api_client = api_client
        self.user = user
            
    def generate_car_prompt(self):
        return f"""
        Based on the user preferences, recommend 3 cars with their pros and cons, also take note on the user's country and format
        the price and car names accordingly:
        
        **User Preferences:**
        {self.user.get_user_preferences()}
        
        Provide your response in this structured format, as a valid JSON object without any additional text or commentary:
        [
            {{"make": "Make 1", "model": "Model 1", "year_from": "XXXX", "year_until": "XXXX", "price": "XX,XXX", "pros": ["..."], "cons": ["..."]}},
            {{"make": "Make 2", "model": "Model 2", "year_from": "XXXX", "year_until": "XXXX", "price": "XX,XXX", "pros": ["..."], "cons": ["..."]}},
            {{"make": "Make 3", "model": "Model 3", "year_from": "XXXX", "year_until": "XXXX", "price": "XX,XXX", "pros": ["..."], "cons": ["..."]}},
        ]
        """
        
    def generate_more_info_on_car_prompt(self, car):
        return f"""
        Based on the user preferences, provide a detailed analysis of a {car}. Focus on aspects that are most valuable to the owner, including:

        1. **Model Updates**: A very short overview of the car model's production years and any significant updates or redesigns.
        2. **Reliability**: Information about the car's overall reliability, common issues, and average maintenance costs.
        3. **Engine Options**: Highlight available engine options, including fuel efficiency, performance, and standout features.
        4. **Ownership Experience**: Insights about comfort, driving dynamics, and usability features.
        5. **Market Availability and Resale Value**: Availability in the user's region and resale value trends.
        6. **Known Issues and Tips**: Known issues and best practices for choosing the right version or model year.

        ### Provide your response in this structured format, as a valid JSON object without any additional text or commentary:
        {{
            "model_updates": "Significant updates or redesigns",
            "reliability": "<reliable/problematic>",
            "common_issues": ["<Issue 1>", "<Issue 2>", "..."],
            "maintenance_cost": "<Estimated yearly cost in user's country currency, e.g., 500>",
            "engine_options": [
                {{"engine": "<Engine Type 1>", "description": "<Details>"}},
                {{"engine": "<Engine Type 2>", "description": "<Details>"}}
            ],
            "ownership_experience": {{
                "pros": ["<Pro 1>", "<Pro 2>", "..."],
                "cons": ["<Con 1>", "<Con 2>", "..."]
            }},
            "availability": "<e.g., widely available/limited availability>",
            "resale_value": "<e.g., strong/moderate/low>",
            "known_issues": ["<Known Issue 1>", "<Known Issue 2>", "..."],
            "tips": ["<Tip 1>", "<Tip 2>", "..."]
        }}
        """
        
    def get_car_recommendations(self):
        prompt = self.generate_car_prompt()
                
        response = self.api_client.generate_response(prompt)
        
        try:
            for car in response:
                self.cars.append(Car(**car))
            
            return self.cars
        except (ValueError, SyntaxError) as e:
            print(e)
            print("Failed to parse recommendations. Please try again.")
            return []
        
    def get_more_info_on_car(self, car):
        prompt = self.generate_more_info_on_car_prompt(car)
        
        response = self.api_client.generate_response(prompt)
        try:
            car.set_add_info(
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
                    # self.system.compare_cars()
                    ...
                case "3":
                    self.system.query_car_details()


if __name__ == "__main__":
    app = CarRecommendationApp()
    app.run()
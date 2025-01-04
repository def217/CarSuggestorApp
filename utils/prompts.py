def generate_car_prompt(user, cars):
    
    car_list = build_car_list(cars)
        
    return f"""
    Here is the current car list {car_list}, based on the user preferences given below, recommend 3 more cars with their pros and cons, do not generate
    duplicates, take note on the user's country and format the price and car names accordingly:
    
    **User Preferences:**
    {user.get_user_preferences()}
    
    Provide your response in this structured format, as a valid JSON object without any additional text or commentary:
    [
        {{"make": "Make 1", "model": "Model 1", "year_from": "XXXX", "year_until": "XXXX", "price_from": "XX,XXX", "price_to": "XX,XXX", "pros": ["..."], "cons": ["..."]}},
        {{"make": "Make 2", "model": "Model 2", "year_from": "XXXX", "year_until": "XXXX", "price_from": "XX,XXX", "price_to": "XX,XXX","pros": ["..."], "cons": ["..."]}},
        {{"make": "Make 3", "model": "Model 3", "year_from": "XXXX", "year_until": "XXXX", "price_from": "XX,XXX", "price_to": "XX,XXX","pros": ["..."], "cons": ["..."]}},
    ]
    """


def generate_more_info_on_car_prompt(car):
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


def compare_cars_based_on_user_prefs(user, cars):
    car_list = build_car_list(cars)

    return f"""
    Based on the user's preferences, compare the following car options and choose the best option: {car_list}. 

    **User Preferences:**
    {user.get_user_preferences()}

    For each car, analyze its suitability for the user based on these aspects:
    - Fit for the user's preferences (e.g., size, budget, fuel type).
    - Driving conditions (e.g., winter performance, AWD needs).
    - Reliability, known issues, and engine options.

    ### Provide your response in the following structured format as a valid JSON array, with no extra text or commentary:
    [
        {{
            "id": "<Same ID from provided car list>",
            "name": "<Car Name>",
            "suitability": "<Key reason why this car suits the user>",
            "driving_conditions": "<Performance in typical conditions>",
            "reliability": "<One-line summary of reliability>",
            "engine_options": ["<Engine 1>", "<Engine 2>"],
            "maintenance": "<Cost and availability summary>"
            "best_option": "<Is this the best option out of the provided cars?>"
        }},
        {{
            "id": "<Same ID from provided car list>",
            "name": "<Car Name 2>",
            ...
        }}
    ]
    """
    
def build_car_list(cars):
    car_list = []

    if len(cars) > 1:
        for car in cars:
            car_list.append((car.id, car.year_from, car.year_until, car.make, car.model))
    
    return car_list

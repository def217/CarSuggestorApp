def get_compared_car(compared_car):
    return (
        f"Car: {compared_car['name']}\n"
        f"Suitability for user: {compared_car['suitability']}\n"
        f"Driving conditions: {compared_car['driving_conditions']}\n"
        f"Realiability: {compared_car['reliability']}\n"
        f"Engine options: {', '.join(compared_car['engine_options'])}\n"
        f"Maintenance: {compared_car['maintenance']}\n"
    )
    
def main_car_info(car):
    return (
        f"{car.year_from}-{car.year_until} {car.make} {car.model} ({car.price_from} - {car.price_to})\n"
        f"Pros: {', '.join(car.pros)}\n"
        f"Cons: {', '.join(car.cons)}\n"
        f"Model updates: {car.model_updates}\n"
        f"Reliability: {car.reliability}\n"
        f"Common issues: {', '.join(car.common_issues)}\n"
        f"Maintenance cost: {car.maintenance_cost}\n"
        f"Engine options:\n      {print_engines(car)}\n"
        f"Pros: {', '.join(car.ownership_experience["pros"])}\n"
        f"Cons: {', '.join(car.ownership_experience["cons"])}\n"
        f"Availability: {car.availability}\n"
        f"Resale value: {car.resale_value}\n"
        f"Known issues: {', '.join(car.known_issues)}\n"
        f"Tips: {', '.join(car.tips)}\n"
    )


def print_engines(car):
    engine_details = []
    for option in car.engine_options:
        engine_details.append(f"{option['engine']}, {option['description']}")
    return "\n      ".join(engine_details)


def print_cars(cars):
    for idx, car in enumerate(cars, start=1):
        print(f"{idx}. {car}")


def dash_line():
    print("-------------------------------------")

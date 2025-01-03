class Car:
    _id_counter = 1
    
    def __init__(self, make, model, price, year_from, year_until, pros, cons):
        self.id = Car._id_counter
        Car._id_counter += 1
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
        self.best_option = None
    
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
        return (self.main_car_info(),
                f"Is this the best option? {self.best_option}\n")
        
    def print_engines(self):
        engine_details = []
        for option in self.engine_options:
            engine_details.append(f"{option['engine']}, {option['description']}")
        return "\n      ".join(engine_details)

    def __str__(self):
        return (f"{self.year_from}-{self.year_until} {self.make} {self.model}")
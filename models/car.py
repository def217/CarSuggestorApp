from utils.prints import print_engines


class Car:
    _id_counter = 1

    def __init__(self, make, model, price_from, price_to, year_from, year_until, pros, cons):
        self.id = Car._id_counter
        Car._id_counter += 1
        self.make = make
        self.model = model
        self.price_from = price_from
        self.price_to = price_to
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

    def set_add_info(
        self,
        model_updates,
        reliability,
        common_issues,
        maintenance_cost,
        engine_options,
        ownership_experience,
        availability,
        resale_value,
        known_issues,
        tips,
    ):
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
    
    def display_data(self):
        formatters = {
            "pros": lambda v: f"Pros: {', '.join(v)}",
            "cons": lambda v: f"Cons: {', '.join(v)}",
            "common_issues": lambda v: f"Common Issues: {', '.join(v)}",
            "engine_options": lambda v: "Engine Options: " + ", ".join(
            f"{item['engine']} ({item['description']})" if isinstance(item, dict) else str(item) for item in v
            ),
            "ownership_experience": lambda v: "\n".join([
                f"Ownership Experience - {key.capitalize()}: {', '.join(value)}"
                for key, value in v.items() if value
            ]),
            "tips": lambda v: f"Tips: {', '.join(v)}",
            "known_issues": lambda v: f"Known Issues: {', '.join(v)}",
        }

        output = []
        for key, value in vars(self).items():
            if value:
                if key in formatters:
                    formatted_value = formatters[key](value)
                else:
                    formatted_value = f"{key.replace('_', ' ').capitalize()}: {value}"
                output.append(formatted_value)

        return "\n".join(output)

    def __str__(self):
        return f"{self.year_from}-{self.year_until} {self.make} {self.model}"

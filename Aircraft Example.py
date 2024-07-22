class Aircraft:
    def __init__(self, name, registration, from_city, to_city, intermediate_cities):
        self.name = name
        self.registration = registration
        self.from_city = from_city
        self.to_city = to_city
        self.intermediate_cities = intermediate_cities

    def __str__(self):
        intermediate_cities_str = ", ".join(self.intermediate_cities)
        return(f"Name: {self.name}, Registration: {self.registration}, From: {self.from_city}, To: {self.to_city}, Intermediate cities: {intermediate_cities_str}")
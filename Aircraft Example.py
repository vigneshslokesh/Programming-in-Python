class Aircraft:
    def __init__(self, name, registration, from_city, to_city, intermediate_cities):
        self.name = name
        self.registration = registration
        self.from_city = from_city
        self.to_city = to_city
        self.intermediate_cities = intermediate_cities

    def __str__(self): # human readable output of the object and easy to understand
        intermediate_cities_str = ", ".join(self.intermediate_cities)
        return(f"Name: {self.name}, Registration: {self.registration}, From: {self.from_city}, To: {self.to_city}, Intermediate cities: {intermediate_cities_str}")
    

class Aircraft_database:
    def __init__(self): #initializing a variable aircrafts with list datastructure to store all the list of aircrafts
        self.aircrafts = []

    def add_aircrafts(self, aircraft):
        self.aircrafts.append(aircraft)
        print(f"Aircraft {aircraft.registration}, added successfully.")

    def remove_aircrafts(self, aircraft):
        for aircraft in self.aircrafts:
            
        self.aircrafts.romove(aircraft)
        print(f"Aircraft {aircraft.registration}, removed successfully.")
db = Aircraft_database()
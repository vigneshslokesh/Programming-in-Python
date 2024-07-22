class Aircraft:
    def __init__(self, name, registration, from_city, to_city, intermediate_cities):
        self.name = name
        self.registration = registration
        self.from_city = from_city
        self.to_city = to_city
        self.intermediate_cities = intermediate_cities

    def __str__(self): # human readable output of the object and easy to understand
        if not self.intermediate_cities:
            intermediate_cities_str = "Direct Flight"
        else:
            intermediate_cities_str = ", ".join(self.intermediate_cities)
            
        return(f"Name: {self.name}, Registration: {self.registration}, From: {self.from_city}, To: {self.to_city}, Intermediate cities: {intermediate_cities_str}")
    

class Aircraft_database:
    def __init__(self): #initializing a variable aircrafts with list datastructure to store all the list of aircrafts
        self.aircrafts = []

    def add_aircrafts(self, aircraft): #adding new aircrafts to the database
        self.aircrafts.append(aircraft)
        print(f"Aircraft {aircraft.registration}, added successfully.")

    def remove_aircrafts(self, del_reg): #removing existing aircrafts from the database
        for aircraft in self.aircrafts:
            if aircraft.registration == del_reg:
                self.aircrafts.romove(aircraft)
                print(f"Aircraft {aircraft.registration}, removed successfully.")
            else:
                print(f"Aircraft {aircraft.registration}, does not exist.")

    def view_aircrafts(self): #viewing all the aircrafts in the database
        if not self.aircrafts:
            print("No aircrafts in the database.")
        for aircraft in self.aircrafts:
            print(aircraft)

db = Aircraft_database()

def uindex():
    while True:
        print("Welcome to Aircraft DB")
        print("1. Add Aircraft")
        print("2. Delete Aircraft")
        print("3. View Aircrafts")
        print("4. Exit")
        opt = input("Select an option between (1-4)")

        if opt == '1':
            uinput()
        elif opt == '2':
            registartion = input("Enter the Aircraft registration number to be removed")
            db.remove_aircrafts(registartion)
        elif opt == '3':
            db.view_aircrafts()
        elif opt == '4':
            print("Exiting Aircraft DB. Goodbye!")
            break  
        else: 
            print("Invalid input, Enter a valid option")
        

def uinput():
    name = input("Enter the name of the aircraft: ")
    registration = input("Enter the registration number: ")
    from_city = input("Enter the departure city: ")
    to_city = input("Enter the destination city: ")
    intermediate_cities = input("Enter the intermediate cities (comma-separated): ").split(',')
    intermediate_cities = [city.strip() for city in intermediate_cities]
    
    new_aircraft = Aircraft(name, registration, from_city, to_city, intermediate_cities)
    db.add_aircrafts(new_aircraft)


# testing cases
# air_cft1 = Aircraft("Boeing A370", "B1234", "BLR", "DEL", ["IXA, HYD"])
# air_cft2 = Aircraft("Boeing A371", "B1235", "BLR", "KOL", ["HYD, DEL"])

# db.add_aircrafts(air_cft1)
# db.add_aircrafts(air_cft2)

# db.view_aircrafts()

uindex()



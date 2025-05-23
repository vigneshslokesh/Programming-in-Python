capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting List in Dictioanry

# travel_log = {
#     "France": ['Paris', 'Lille', 'Dijon'],
#     "Germany": ["Stuttgart, 'Berlin"]
# }

# # printing the item in a list contained inside a dictionary
# print(travel_log["France"][1])

# # printing item in a nested list
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ['Paris', 'Lille', 'Dijon']
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    }    
}

print(travel_log["Germany"]["cities_visited"][0])
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting List in Dictioanry

travel_log = {
    "France": ['Paris', 'Lille', 'Dijon'],
    "Germany": ["Stuttgart, 'Berlin"]
}

# printing the item in a list contained inside a dictionary
print(travel_log["France"][1])

# printing item in a nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
"""
Lesson 23: Dictionary in List - (Day 9 Concepts)
 -- Nesting: Lists and Dictionaries
"""

country = input("Add country name: ")
visits = int(input("Number of visits: "))  # Number of visits
user_cities = input("Enter a list of Cites (separated by a comma (,)): ")  # create list from formatted string
list_of_cities = user_cities.split(", ")

print(list_of_cities)

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country_name, num_visits, cities_visited):
    # create a new dictionary (object) with the associated key:value pairs
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = num_visits
    new_country["cities"] = cities_visited

    # Dictionary Literal
    # new_country = {"country": country_name, "visits": num_visits, "cities": cities_visited}

    # append the new dictionary to the existing travel_log dictionary
    travel_log.append(new_country)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

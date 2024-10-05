"""
Concept: Nesting: Lists and Dictionaries
 -- Example:
     {
       Key: [List],
       Key: {Dict},
     }
"""

# Nesting- Simpy Dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
# NOTE: Dictionary Key can only have 1 value;
#       so to represent multiply values that could be associated with a Dictionary Key -> use Lists or another Dictionary for the Key's value
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
# Can nest a List within a List - but not as useful as nesting a list inside a dictionary
some_list = ["A", "B", ["C", "D", "E"], "F"] # valid python code

# Nesting Dictionary in a Dictiorary
travel_log_visits = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg","Stuttgart"], "total_visits": 3},
}

# Nesting a Dictionary in a List; when there are more than 1 key:value pairs -> best practice is to put them on separate lines for readability
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg","Stuttgart"],
        "total_visits": 3
    },
]

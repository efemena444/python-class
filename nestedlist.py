country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
travel_log = [
  {
    "country": "Nigeria",
    "visits": 12,
    "cities": ["ekpoma", "Benin", "auchi"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Your code here 👇
def new_country(name,country_visited,cities_visited):
    country = {}
    country["country"]=name  
    country["visits"]  = country_visited
    country["cities"]=cities_visited
    travel_log.append(new_country)
    







new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
# using json module for writing and reading file data
import json
# create a dictionary for Star Wars movie (from 05-dictionaries.py)
star_wars_dict = {"title": "Star Wars",
                  "year": 1977,
                  "rating": "PG",
                  "director": "George Lucas"}

with open('./day-2/movies.json', 'w') as f:
    json.dump(star_wars_dict, f)

print('done writing data')
print('load movies into dictionary')
with open('./day-2/movies.json') as json_file:
    data = json.load(json_file)
    print("data type: ", type(data))
    print("data:", data)
    print("title:", data['title'])
    print("year:", data['year'])
    print("rating:", data['rating'])
    print("director:", data['director'])


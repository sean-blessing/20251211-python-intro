# movie
# Star Wars, 1977, PG, George Lucas
# title, year, rating, director

star_wars_dict = {"title": "Star Wars",
                  "year": 1977,
                  "rating": "PG",
                  "director": "George Lucas"}

print("SW Dictionary:", star_wars_dict)

print("title:", star_wars_dict["title"])
# change a property:
star_wars_dict["title"] = "Star Wars Ep IV: A New Hope"
print(star_wars_dict)

# add a property
star_wars_dict.update({"run_time": 121})
print(star_wars_dict)

# list all keys
print("Keys:", list(star_wars_dict.keys()))

# list all values
print("Values:", list(star_wars_dict.values()))

# key that doesn't exist
#star_wars_dict["star_rating"]

# get - with default value
print(star_wars_dict.get("star_rating", "Movie doesn't have star rating"))

from movie import Movie
from actor import Actor

print("Welcome to the movies app")

# star wars movie
# Star Wars, 1977, PG, George Lucas
# id, title, year, rating, director

# create an instance of Movie
m1 = Movie(1, "Star Wars", 1977, "PG", "George Lucas")

# print the details to console
print(m1.detail())

# actor class
# first_name, last_name, birth_year (int)
# Sadie Sink 2002
a1 = Actor(1, "Sadie", "Sink", 2002)

# print actor details
print(a1.detail())

print("Bye")
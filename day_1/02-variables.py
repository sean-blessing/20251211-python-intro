# single line comment
'''
a
multi
line
comment
'''

# declare some variables
first_name = "Bob"
print(first_name)
print(type(first_name))
# first_name = 5
# print(type(first_name))

last_name = "Marley"
# other_name = "O'Maley"

print(first_name, last_name)
print(first_name, last_name, sep="*")
print(first_name + " " + last_name)
print("His name is: "+ first_name + " " + last_name)
print(f"His name is: {first_name} {last_name}")

# length of strings
full_name = f"{first_name} {last_name}"
print(len(full_name)) 
# indexOf
first_space = full_name.index(" ")
print(first_space)

# range
# list of numbers 0 to 10
range_1 = range(11)
print(list(range_1))
range_2 = range(0,21)
print(list(range_2))
range_even = range(0,21,2)
print(list(range_even))
range_backwards = range(100, 0, -5)
print(list(range_backwards))

# print w/ 'end' attribute
print(first_name, end="...")
print(last_name)
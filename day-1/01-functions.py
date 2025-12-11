# define some functions!
# prompt for first_name, last_name, print a welcome message

# input function
# function - prompting for a string, printing to screen
def prompt_string(prompt):
   input_str = input(prompt) 
   print("You entered: "+input_str)
# first_name = input('First Name?: ')
# print(first_name)
prompt_string('First Name?: ')
prompt_string('Last Name?: ')

# store birth_month in a variable, call a function 
def prompt_int(prompt):
   input_int = int(input(prompt))
   return input_int

birth_month = prompt_int('Birth Month?: ')
print(birth_month)

# define a add function that has a default value
def add(nbr_1 = 0, nbr_2 =0):
    return nbr_1 + nbr_2

print(add(5,4))
print(add(5))
print(add())

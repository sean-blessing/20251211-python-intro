#functions to help with console IO

# prompt for a string
def prompt_string(prompt):
    print(f"prompt_string called. __name__=",__name__)
    return input(prompt)

# prompt for a whole number
def prompt_int(prompt):
    nbr = 0
    success = False
    while not success:
        try:
            nbr = int(input(prompt + " "))
            success = True
        except ValueError as ve:
            print(f"Invalid Entry. Please try again.")
    return nbr
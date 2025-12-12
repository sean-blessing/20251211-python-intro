# dir function
first_name = "George"
#print(dir(first_name))
full_name = "Sean N Blessing"
name_parts = full_name.split()
print(name_parts)
phone_nbr = '513-123-4567'

phone_parts = phone_nbr.split('-')
print(phone_parts)

# join - piece phone parts into new phone number?
print("-".join(phone_parts))
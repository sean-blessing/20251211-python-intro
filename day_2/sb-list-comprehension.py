# use a for loop to build a list of even #s, 2 to 20
even_nbrs_1 = []
for i in range(2,21,2):
    even_nbrs_1.append(i)

print(f"even_nbrs_1:",even_nbrs_1)

# use list comprehension to do the same thing
even_nbrs_2 = [i for i in range(2,21,2)]
print(f"even_nbrs_2:",even_nbrs_2)

# use math in a list comprehension
even_nbrs_times_ten = [nbr*10 for nbr in even_nbrs_2]
print(f"even_nbrs_time_ten:",even_nbrs_times_ten)
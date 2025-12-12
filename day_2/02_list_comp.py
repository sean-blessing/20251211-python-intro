#demonstrate list comprehension in Python

# creating a list of even numbers, 2 to 20
# old school
even_nbrs_1 = []
for n in range(2,21,2):
    even_nbrs_1.append(n)

print(f"even_nbrs_1:", even_nbrs_1)

# same thing using list comprehension
even_nbrs_2 = [n for n in range(2, 21, 2)]
print(f"even_nbrs_2:", even_nbrs_2)

even_nbrs_times_ten = [n*10 for n in range(2, 21, 2)]
print(f"even_nbrs_times_ten:", even_nbrs_times_ten)

even_nbrs_times_two = [n*2 for n in even_nbrs_2]
print(f"even_nbrs_times_two:", even_nbrs_times_two)


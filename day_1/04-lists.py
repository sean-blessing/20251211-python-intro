# create a list of marvel heroes
marvel_heroes = ["Spiderman", "Black Widow", "The Hulk"]

# create a list of marvel villains
marvel_villains = ["Thanos", "Doc Octopus", "Loki"]

# print the heroes and villains
print("Heroes: "+",".join(marvel_heroes))
print("Villains: "+",".join(marvel_villains))

# add a hero
marvel_heroes.append("Thor")
print(marvel_heroes)

# remove a villain
removed_villain = marvel_villains.pop()
print(removed_villain + " was removed")
print(marvel_villains)

numbers_list = list(range(1,11))
print("numbers_list: ",numbers_list)
# remove #5 (idx position 4)
numbers_list.pop(4)
print("numbers_list: ",numbers_list)
# insert a value into position 4
numbers_list.insert(4,50)
print("numbers_list: ",numbers_list)

# slicing
# first 4 values
print('first four: ',numbers_list[0:4])
# first 5 values
print('first five: ',numbers_list[:5])
# 4th to 8th values
print('4th to 8th: ',numbers_list[4:9])
# last 3
print('last three: ',numbers_list[-3:])
# last element
print('last element: ',numbers_list[-1])
# last element
print('last element(len): ',numbers_list[len(numbers_list)-1])

# add villains into heroes list
marvel_heroes.extend(marvel_villains)
print('Marvel Heroes:',marvel_heroes)

# random #s
import random
# random # between 1 and 10
print(random.randint(1,10))

# street light example
light_color = input('Light Color: ')
if light_color.lower() == "red":
    print("Stop")
elif light_color.lower() == "yellow":
    print("Slow down")
elif light_color.lower() == "green":
    print("Go!")
else:
    print("Error - invalid color")


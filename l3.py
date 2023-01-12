import random

my_array = [0] * 100

max=-2**31
for i in range(len(my_array)):
    my_array[i] = random.randint(0, 100)

for i in range(len(my_array)):
    if(max<my_array[i]):
        max=my_array[i]

print(max)
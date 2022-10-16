x, y, z = 10, 'Hello', True


names=["Jeff", "Bill", "Steve", "Mohan"] 
del names[0] # removes item at index 0
print("After del names[0]: ", names)

names.remove("Bill") # removes "Bill"
print("After names.remove('Bill'): ", names)

print(names.pop(0)) # return and removes item at index 0
print("After names.pop(0): ", names)

names.pop() # return removes item at last index
print("After names.pop(): ", names)

del names # removes entire list object
print(names)




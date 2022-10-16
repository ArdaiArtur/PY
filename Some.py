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



tpl = tuple('Hello') # converts string to tuple
print(tpl)
tpl = tuple([1,2,3,4,5]) # converts list to tuple
print(tpl)
tpl = tuple({1,2,3,4,5}) # converts set to tuple
print(tpl)
tpl = tuple({1:"One",2:"Two"}) # converts dictionary to tuple
print(tpl)

names = ('Jeff', 'Bill', 'Steve', 'Yash') 
print('names type: ', type(names))

nums = (1,2,3,4,5) 
print('nums type: ', type(nums))


even_nums = {2, 4, 6, 8, 10} # set of even numbers
emp = {1, 'Steve', 10.5, True} # set of different objects



d = {} # empty dictionary

numNames={1:"One", 2: "Two", 3:"Three"} # int key, string value

decNames={1.5:"One and Half", 2.5: "Two and Half", 3.5:"Three and Half"} # float key, string value

items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"} # tuple key, string value

romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} # string key, int value


capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}

for key in capitals:
    print("Key = " + key + ", Value = " + capitals[key]) 

captains = {'England': 'Root', 'Australia': 'Paine', 'India': 'Virat', 'Srilanka': 'Jayasurya'}
'England' in captains

price = 100

if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif price < 100:
    print("price is less than 100")




nums = (10, 20, 30, 40, 50)
for i in nums:
    print(i)

for char in 'Hello':
    print (char)
numNames = { 1:'One', 2: 'Two', 3: 'Three'}

for pair in numNames.items():
    print(pair)
    
    
for i in range(5):
    print(i) 
       

for x in range(1,4):
    for y in range(1,3):
        print('x = ', x, ', y = ', y) 

















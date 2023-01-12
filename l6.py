
   
with open('l6.txt', 'r') as file:
    data = file.read()
    print(data)
with open('l6.txt', 'r') as file:
    for line in file:
        print(line)
       
with open('l6.txt', 'r') as file:
    text = file.read()
    words = text.split(' ')
    print(words)
a=len(words)
print("all words in txt: " + str(words) + " " + "final value of a:" + str(a))
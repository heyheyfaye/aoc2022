import re

contains=0
overlap=0

with open("input4.txt", "r") as inputPuzzle3:
    liste = inputPuzzle3.read().split("\n")
#print("Liste: ", liste)
    
for i in liste:
    kleineListe = i.split(",")
    #print("kleine Liste: ", kleineListe)
    x = re.findall("\d+",kleineListe[0])
    y = re.findall("\d+",kleineListe[1])

    if int(x[0])>=int(y[0]) and int(x[1])<=int(y[1]) or int(y[0])>=int(x[0]) and int(y[1])<=int(x[1]):
        #print(int(x[0]), int(x[1]), int(y[0]), int(y[1]))
        contains+=1

    if int(x[1])>=int(y[0]) and int(y[1])>=int(x[0]) or int(y[1])>=int(x[0]) and int(x[1])>=int(y[0]):
        #print(int(x[0]), int(x[1]), int(y[0]), int(y[1]))
        overlap+=1

print("contains:", contains)  
print("overlap:",overlap) 
with open("input1.txt", "r") as inputPuzzle1:
    liste = inputPuzzle1.read().split("\n\n")
    #print("Liste: ", liste)

großeListe = []
calories = 0
    
for i in liste:
    kleineListe = sum([int(x) for x in i.split("\n")])
    großeListe.append(kleineListe)
    #print("kleine Liste: ", kleineListe)

    if kleineListe > calories:
        calories = kleineListe

print(calories)
print(sum(sorted(großeListe)[-3:]))

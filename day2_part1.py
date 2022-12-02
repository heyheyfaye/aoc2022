# A - X - Rock - 1
# B - Y - Paper - 2
# C - Z - Scissors - 3

# + looser of round 0
# + winner of round 6
# + draw round 3

elf_score=0
my_score=0

with open("input2.txt", "r") as inputPuzzle2:
    liste = inputPuzzle2.read().split("\n")
    #print("Liste: ", liste)

for i in liste:
    kleineListe = i.split(" ")
    #print("kleine Liste", kleineListe)
    print(kleineListe[0], "-", kleineListe[1])
    if kleineListe[0] == "A":
        elf_score+=1
    elif kleineListe[0] == "B":
        elf_score+=2
    elif kleineListe[0] == "C":
        elf_score+=3
    
    if kleineListe[1] == "X":
        my_score+=1
    elif kleineListe[1] == "Y":
        my_score+=2
    elif kleineListe[1] == "Z":
        my_score+=3
    else:
        print("what happened?")
    print("My score:", my_score, "Elf score:", elf_score)

    #print("i:", i)
    if i == "A X" or i == "B Y" or i == "C Z":
        my_score+=3
        elf_score+=3
    elif i == "A Y" or i == "B Z" or i == "C X":
        my_score+=6
    elif i == "A Z" or i == "B X" or i == "C Y":
        elf_score+=6
    else:
        print("what happened here again?")

    print("My score:", my_score, "Elf score:", elf_score)
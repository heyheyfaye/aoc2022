# A Rock - 1
# B Paper - 2
# C Scissors - 3

# X looser of round 0
# Z winner of round 6
# Y draw round 3

elf_score=0
my_score=0

with open("input2.txt", "r") as inputPuzzle2:
    liste = inputPuzzle2.read().split("\n")
    #print("Liste: ", liste)

for i in liste:
    kleineListe = i.split(" ")
    #print("kleine Liste", kleineListe)
    print(kleineListe[0], "-", kleineListe[1])
    
    if kleineListe[1] == "X":
        if kleineListe[0] == "A":
            elf_score+=1
            my_score+=0+3
        elif kleineListe[0] == "B":
            elf_score+=2
            my_score+=0+1
        elif kleineListe[0] == "C":
            elf_score+=3
            my_score+=0+2
    elif kleineListe[1] == "Y":
        if kleineListe[0] == "A":
            elf_score+=1
            my_score+=3+1
        elif kleineListe[0] == "B":
            elf_score+=2
            my_score+=3+2
        elif kleineListe[0] == "C":
            elf_score+=3
            my_score+=3+3
    elif kleineListe[1] == "Z":
        if kleineListe[0] == "A":
            elf_score+=1
            my_score+=6+2
        elif kleineListe[0] == "B":
            elf_score+=2
            my_score+=6+3
        elif kleineListe[0] == "C":
            elf_score+=3
            my_score+=6+1
    else:
        print("what happened?")
    print("My score:", my_score, "Elf score:", elf_score)
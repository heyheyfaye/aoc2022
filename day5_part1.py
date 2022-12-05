import re

stack1 = ["D","T","R", "B","J","L","W","G"]
stack2 = ["S","W","C"]
stack3 = ["R","Z","T","M",]
stack4 = ["D","T","C","H","S","P","V"]
stack5 = ["G","P","T","L","D","Z"]
stack6 = ["F","B","R","Z","J","Q","C","D"]
stack7 = ["S","B","D","J","M","F","T","R"]
stack8 = ["L","H","R","B","T","V","M"]
stack9 = ["Q","P","D","S","V"]

stackList=[stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]

with open("input5.txt", "r") as inputPuzzle5:
    liste = inputPuzzle5.read().split("\n")
#print("Liste: ", liste)
    
for i in liste:
    moves = re.findall("\d+",i)
    #print("moves: ", moves)

    #from where
    from_where = stackList[int(moves[1])-1]

    #where to
    where_to = stackList[int(moves[2])-1]

    #shift
    for i in range (int(moves[0])):
        where_to.append(from_where.pop())

print(stack1.pop(),stack2.pop(),stack3.pop(),stack4.pop(),stack5.pop(),stack6.pop(),stack7.pop(),stack8.pop(),stack9.pop())
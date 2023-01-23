matrix = []
len_Row=0
len_Col=0
visible = 0
scenicScoreList=[]

with open("input8.txt", "r") as inputPuzzle8:
    liste = inputPuzzle8.read().split("\n")
    #print("Liste: ", liste)

for i in liste:
    #print(i)
    row = list(i.strip(""))
    len_Col=len(i)
    matrix.append(row)
    len_Row=len(liste)

print("length of row", len_Row)
print("length of column", len_Col)
#print(matrix)

for i in range(1,(len_Row-1)):
    for j in range(1,(len_Col-1)):
        #print("i-j:", i, j)
        visibleOben=0
        visibleRechts=0
        visibleUnten=0
        visibleLinks=0

        counterOben=0
        counterRechts=0
        counterUnten=0
        counterLinks=0
        
        #oben
        for x in reversed(range(0,i)):
            if matrix[i][j] > matrix[x][j]:
                #print("oben:", "matrix[",x,"][",j,"]", "=", matrix[x][j])
                counterOben+=1
            elif matrix[i][j] <= matrix[x][j]:
                counterOben+=1
                break

        #rechts
        for x in range(j+1,len_Row):
            if matrix[i][j] > matrix[i][x]:
                #print("rechts:", "matrix[",i,"][",x,"]", "=", matrix[i][x])
                counterRechts+=1 
            elif matrix[i][j] <= matrix[i][x]:
                counterRechts+=1 
                break
                   
        #unten
        for x in range(i+1,len_Col):
            if matrix[i][j] > matrix[x][j]:
                #print("unten:", "matrix[",x,"][",j,"]", "=", matrix[x][j])
                counterUnten +=1 
            elif matrix[i][j] <= matrix[x][j]:
                counterUnten +=1 
                break                   

        #links
        for x in reversed(range(0,j)):
            if matrix[i][j] > matrix[i][x]:
                #print("links:", "matrix[",i,"][",x,"]", "=", matrix[i][x])
                counterLinks +=1   
            elif matrix[i][j] <= matrix[i][x]:
                counterLinks +=1
                break 
      

        if visibleOben!=0 or visibleRechts!=0 or visibleUnten!=0 or visibleLinks!=0:
                visible+=1   
        #print("visible",visible)
        #print("")

        scenic_score = counterOben*counterRechts*counterUnten*counterLinks 
        scenicScoreList.append(scenic_score)
        #print("counterOben:", counterOben)
        #print("counterRechts:", counterRechts)
        #print("counterUnten:", counterUnten)
        #print("counterLinks:", counterLinks)
        #print("scenic_score:",scenic_score)
        #print("")
                     
edge = 2*len_Row + 2*(len_Col-2)
print("edge:", edge)    
print("visible interor:", visible)
print("visible all together:", visible+edge)
print("highest scenic score", max(scenicScoreList))
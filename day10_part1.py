import re

cycle = 0
x = 1
registerList=[]

with open("input10.txt", "r") as inputPuzzle10:
    liste = inputPuzzle10.read().split("\n")
    #print("Liste: ", liste)

for i in liste:
    #print("---",i,"---")
    if re.findall("noop",i):
        cycle += 1
        registerList.append(x)
        #print("cycle noop:",x)

    if re.findall("addx \d",i):
        register = int(re.findall("\d+",i)[0])
        cycle += 1
        registerList.append(x)
        #print("cycle:",cycle)
        #print("x", x)
        cycle += 1
        #print("cycle:",cycle)
        x+=register
        registerList.append(x)
        #print("x", x)

    if re.findall("addx -\d",i):
        register = int(re.findall("-\d+",i)[0])
        cycle += 1
        registerList.append(x)
        #print("cycle:",cycle)
        #print("x", x)
        cycle += 1
        #print("cycle:",cycle)
        x+=register
        registerList.append(x)
        #print("x", x)

#print(registerList)
#print(len(registerList))
print("signal strength at 20th:",registerList[18],"-",registerList[18]*20)
print("signal strength at 60th:",registerList[58],"-",registerList[58]*60)
print("signal strength at 100th:",registerList[98],"-",registerList[98]*100)
print("signal strength at 140th:",registerList[138], "-", registerList[138]*140)
print("signal strength at 180th:",registerList[178], "-", registerList[178]*180)
print("signal strength at 220th:",registerList[218],"-",registerList[218]*220)

print("result:", registerList[18]*20+registerList[58]*60+registerList[98]*100+registerList[138]*140+registerList[178]*180+registerList[218]*220)
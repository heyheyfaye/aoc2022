# The list of items for each rucksack is given as characters all on a single line. 
# the first half of the characters represent items in the first compartment
# while the second half of the characters represent items in the second compartment.
# Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

import string

alphabet_low = list(string.ascii_lowercase)
alphabet_up = list(string.ascii_uppercase)
alphabet = alphabet_low + alphabet_up
#print("lowercase", alphabet_low)
#print("uppercase", alphabet_up)
score = 0

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        #print(a_set & b_set)
        letter = next(iter(a_set & b_set))
        #print(alphabet.index(letter)+1)
        return alphabet.index(letter)+1
    else:
        print("No common elements")

with open("input3.txt", "r") as inputPuzzle3:
    liste = inputPuzzle3.read().split("\n")
#print("Liste: ", liste)
    
for i in liste:
    middle_index=int(len(i)/2)
    #print("middle_index", middle_index)
    secondHalf = i[middle_index:]
    firstHalf = i[:middle_index]
    #print("erste Hälfte: ", firstHalf)
    #print("zweite Hälfte: ", secondHalf)
    score += common_member(firstHalf, secondHalf)

print("score: ", score)
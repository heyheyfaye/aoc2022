def sliding_window(elements, window_size):
    if len(elements) == window_size:
        return elements
    
    for i in range(len(elements)):
        window = elements[i:i+window_size]
        duplicate = 0
        #count duplicates
        for character in window:
            duplicate += window.count(character)
        #if duplicate > window size: there are duplicates, not what we are searching for
        #if duplicate = window size: there are no duplicates in this window
        #part1, window size 4
        if duplicate == 4:
            print("window1:", elements[i:i+window_size])
            return i+window_size
        #part2, window size 14
        if duplicate == 14:
            print("window2:", elements[i:i+window_size])
            return i+window_size

with open("input6.txt", "r") as inputPuzzle6:
    liste = inputPuzzle6.read()
#print("Liste: ", liste)

print("part1:", sliding_window(liste,4))
print("part2:", sliding_window(liste,14))
# Data Import #
wordsearch = open("./input.txt", "r").read().splitlines()

# ------------- Part One -----------------#

#Neighbour Coordinates (defined as Y, X)
neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

def findXmas():
    totalFound = 0
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'X':
                # Start finding neighbouring M
                for neighbour in neighbours:
                    checkY = i + (neighbour[1])
                    checkX = j + (neighbour[0])
                    
                    if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                        if (wordsearch[checkY][checkX] == 'M'):
                            # Start finding neighbouring A
                            checkY = checkY + (neighbour[1])
                            checkX = checkX + (neighbour[0])
                
                            if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                                if (wordsearch[checkY][checkX] == 'A'):
                                    # Start finding neighbouring S
                                    checkY = checkY + (neighbour[1])
                                    checkX = checkX + (neighbour[0])
            
                                    if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                                        if (wordsearch[checkY][checkX] == 'S'):
                                            totalFound += 1
    return totalFound
                                    

partOneAnswer = findXmas()
print("Part One Answer: ",partOneAnswer)

# ------------- Part Two -----------------#

p2neighbours = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
p2opposites = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

def findStupidXmas():
    totalStupidFound = 0

    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'A':
                # Found A, consult neighbours for M
                for k in range(len(p2neighbours)):
                    checkY = i + (p2neighbours[k][1])
                    checkX = j + (p2neighbours[k][0])
                    unconsumed = []
                    
                    if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                        if (wordsearch[checkY][checkX] == 'M'):
                            # Found M, check defined opposite for S
                            checkY = i + (p2opposites[k][1])
                            checkX = j + (p2opposites[k][0])
                
                            if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                                if (wordsearch[checkY][checkX] == 'S'):
                                    #Found Diagonal MAS, initialise unconsumed coordinates

                                    for coords in p2neighbours:
                                        if coords != p2neighbours[k] and coords != p2opposites[k]:
                                            unconsumed.append(coords)

                                    #Check for MAS in unconsumed
                                    for n in range(len(unconsumed)):
                                        checkY = i + (unconsumed[n][1])
                                        checkX = j + (unconsumed[n][0])
                                        
                                        if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                                            if (wordsearch[checkY][checkX] == 'M'):
                                                # Found M, check defined opposite for S
                                                for m in range(len(unconsumed)):
                                                    checkY = i + (unconsumed[m][1])
                                                    checkX = j + (unconsumed[m][0])

                                                    if (-1 < checkY < len(wordsearch) and -1 < checkX < len(wordsearch[i])):
                                                        if (wordsearch[checkY][checkX] == 'S'):
                                                            totalStupidFound += 1
    return totalStupidFound

partTwoAnswer = findStupidXmas()
print("Part Two Answer: ",(partTwoAnswer/2))
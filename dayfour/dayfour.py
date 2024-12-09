# Data Import #
wordsearch = open("./input.txt", "r").read().splitlines()

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
print("Found: ",partOneAnswer)

#only use existing neighbour to maintain direction
data = open("./input.txt", "r").read().splitlines()
xbound = len(data[0]) - 1
ybound = len(data) - 1
heads = []
grid = []

for i in range(len(data)):
    res = [int(ele) for ele in list(data[i])]
    grid.append(res)

#part one
# def checkNext(x, y, z):
#     currentPosHeight = grid[y][x]
#     currentPosFullIndex = str(y) + str(x)
#     if currentPosHeight == 9:
#         fromTo = str(z) + currentPosFullIndex
#         if fromTo not in heads:
#             heads.append(fromTo)
#     elif currentPosHeight < 9:
#         #check north
#         if 0 <= y-1 <= ybound:
#             if grid[y-1][x] == currentPosHeight+1:
#                 checkNext(x, y-1, z)
#         #check south
#         if 0 <= y+1 <= ybound:
#             if grid[y+1][x] == currentPosHeight+1:
#                 checkNext(x, y+1, z)
#         #check east
#         if 0 <= x+1 <= xbound:
#             if grid[y][x+1] == currentPosHeight+1:
#                 checkNext(x+1, y, z)
#         #check west
#         if 0 <= x-1 <= xbound:
#             if grid[y][x-1] == currentPosHeight+1:
#                 checkNext(x-1, y, z)

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == 0:
#             fullIndex = str(i) + str(j)
#             print("Checking path starting from: ",fullIndex)
#             checkNext(j, i, fullIndex)

# print("Part One Answer: ",len(heads))
 

def checkNext(x, y, z):
    currentPosHeight = grid[y][x]
    if currentPosHeight == 9:
        heads.append(z)
    elif currentPosHeight < 9:
        #check north
        if 0 <= y-1 <= ybound:
            if grid[y-1][x] == currentPosHeight+1:
                checkNext(x, y-1, z)
        #check south
        if 0 <= y+1 <= ybound:
            if grid[y+1][x] == currentPosHeight+1:
                checkNext(x, y+1, z)
        #check east
        if 0 <= x+1 <= xbound:
            if grid[y][x+1] == currentPosHeight+1:
                checkNext(x+1, y, z)
        #check west
        if 0 <= x-1 <= xbound:
            if grid[y][x-1] == currentPosHeight+1:
                checkNext(x-1, y, z)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            fullIndex = str(i) + str(j)
            print("Checking path starting from: ",fullIndex)
            checkNext(j, i, fullIndex)

print("Part Two Answer: ",len(heads))

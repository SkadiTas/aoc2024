data = open("./input.txt", "r").read().split()
xbound = len(data[0]) - 1
ybound = len(data) - 1
totalVisited, regions = [], []
totalCost = 0

#x = xcoord | y = ycoord | z = plant | region = region
def checkNext(x, y, z, region):
            #check east
            if 0 <= x+1 <= xbound:
                if data[y][x+1] == z and [x+1, y] not in region:
                    totalVisited.append([x+1, y])
                    region.append([x+1, y])
                    checkNext(x+1, y, z, region)
            #check south
            if 0 <= y+1 <= ybound:
                if data[y+1][x] == z and [x, y+1] not in region:
                    totalVisited.append([x, y+1])
                    region.append([x, y+1])
                    checkNext(x, y+1, z, region)
            #check west
            if 0 <= x-1 <= xbound:
                if data[y][x-1] == z and [x-1, y] not in region:
                    totalVisited.append([x-1, y])
                    region.append([x-1, y])
                    checkNext(x-1, y, z, region)
            #check north
            if 0 <= y-1 <= ybound:
                if data[y-1][x] == z and [x, y-1] not in region:
                    totalVisited.append([x, y-1])
                    region.append([x, y-1])
                    checkNext(x, y-1, z, region)
            return region

# def checkSubRegion(sub):
#     for i in range(len(regions)):
#         if len(regions[i]) > 3 and regions[i] != sub:
#             region = Polygon(regions[i])
#             make_valid(region)
#             point = Point(sub[0])
#             if region.covers(point):
#                 perims[i] += evaluatePerimeter(sub)

def convertPerims(node):
    # convert each node to boundary where 0 = not perim and 1 = perim
    # north, east, south, west
    newNode = []
    x, y = node[0], node[1]
    z = data[y][x]
    #check north
    if 0 <= y-1 <= ybound: 
        if data[y-1][x] != z:
            newNode.append(1)
        else:
            newNode.append(0)
    else:
        newNode.append(1)
    #check east
    if 0 <= x+1 <= xbound:
        if data[y][x+1] != z:
            newNode.append(1)
        else:
            newNode.append(0)
    else:
        newNode.append(1)
    #check south
    if 0 <= y+1 <= ybound:
        if data[y+1][x] != z:
            newNode.append(1)
        else:
            newNode.append(0)
    else:
        newNode.append(1)
    #check west
    if 0 <= x-1 <= xbound:
        if data[y][x-1] != z:
            newNode.append(1)
        else:
            newNode.append(0)
    else:
        newNode.append(1)
    return newNode
                 
def evaluatePerimeter(region):
    perimeter = 0
    for i in range(len(region)):
        for j in range(len(region[i])):
            if region[i][j] == 1:
                perimeter += 1
    return perimeter

for i in range(len(data)):
    for j in range(len(data[i])):
        if [j, i] not in totalVisited:
            plant = data[i][j]
            region = []
            region.append([j, i])
            totalVisited.append([j, i])
            checkNext(j, i, plant, region)
            regions.append(region)

for region in regions:
    for i in range(len(region)):
        region[i] = convertPerims(region[i])
    print(region)
    print("Area: ", len(region))
    print("Perimeter: ", evaluatePerimeter(region))
    totalCost += (len(region) * evaluatePerimeter(region))

print(totalCost)
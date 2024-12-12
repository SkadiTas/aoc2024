from itertools import combinations as cb

data = open("./input.txt", "r").read().splitlines()
nodes = []
xbound = len(data[0]) - 1
ybound = len(data) - 1

def equateNodes(x1, y1, x2, y2):
    #need to determine the difference between point 1 and point 2 and subtract from point 1 and add to point 2
    n1x = x1 - (x2 - x1)
    n1y = y1 - (y2 - y1)
    n2x = x2 + (x2 - x1)
    n2y = y2 + (y2 - y1)

    #Check node by adding coords
    if 0 <= n1x <= xbound and 0 <= n1y <= ybound:
        if [n1x, n1y] not in nodes:
            print("Added Node: ", n1x, n1y)
            nodes.append([n1x, n1y])
    else:
        print("Node out of bounds: ", n1x, n1y)

    #Check node by subtracting coords
    if 0 <= n2x <= xbound and 0 <= n2y <= ybound:
        if [n2x, n2y] not in nodes:
            print("Added Node: ", n2x, n2y)
            nodes.append([n2x, n2y])
    else:
        print("Node out of bounds: ", n2x, n2y)

antennas = []
def findAntennas():
     for row in data:
        for point in row:
            if point != '.':
                y = data.index(row)
                x = row.index(point)
                antennas.append([x, y, point])

findAntennas()

char = antennas[0][2]
for antenna in antennas:
    for target in antennas:
        if target != antenna and antenna[2] == target[2]:
            x1 = antenna[0]
            y1 = antenna[1]
            x2 = target[0]
            y2 = target[1]
            print("Determining: ",antenna, target)
            equateNodes(x1, y1, x2, y2)

print("Part One Answer: ",len(nodes))

# ----------------- Part Two -------------- #
nodes2 = []
def equateMultiNodes(x1, y1, x2, y2):
    #need to determine the difference between point 1 and point 2 and subtract from point 1 and add to point 2
    xdiff = (x2-x1)
    ydiff = (y2-y1)

    n1x = x1 - xdiff
    n1y = y1 - ydiff
    n2x = x2 + xdiff
    n2y = y2 + ydiff

    #Check node by adding coords until out of bounds
    while 0 <= n1x <= xbound and 0 <= n1y <= ybound:
        if [n1x, n1y] not in nodes2:
            print("Added Node: ", n1x, n1y)
            nodes2.append([n1x, n1y])
        n1x = n1x - xdiff
        n1y = n1y - ydiff

    #Check node by subtracting coords
    while 0 <= n2x <= xbound and 0 <= n2y <= ybound:
        if [n2x, n2y] not in nodes2:
            print("Added Node: ", n2x, n2y)
            nodes2.append([n2x, n2y])
        n2x = n2x + xdiff
        n2y = n2y + ydiff

char = antennas[0][2]
for antenna in antennas:
    for target in antennas:
        if target != antenna and antenna[2] == target[2]:
            x1 = antenna[0]
            y1 = antenna[1]
            x2 = target[0]
            y2 = target[1]
            print("Determining: ",antenna, target)
            equateMultiNodes(x1, y1, x2, y2)
        if [x1,y1] not in nodes2:
            nodes2.append([x1, y1])
        if [x2,y2] not in nodes2:
            nodes2.append([x2, y2])


print("Part Two Answer: ",(len(nodes2)))

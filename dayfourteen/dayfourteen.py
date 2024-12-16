import re, math, time
data = open("./input.txt", "r").read()

pattern = r'\w=(-?\d+),(-?\d+)'
matches = re.findall(pattern, data)
bots, vels = [], []

for i in range(len(matches)):
    if i % 2 == 0:
        bots.append(matches[i])
    else:
        vels.append(matches[i])

def constructGrid(w, h):
    grid = []
    for y in range(0, h):
        grid.append([0])
        for x in range(0, w-1):
            grid[y].append(0)
    return grid

def evaluateGrid(grid, w, h):
    tl, tr, bl, br = 0, 0, 0, 0
    sliceX = math.floor(w/2)
    sliceY = math.floor(h/2)
    print(sliceY)

    #evaluate first quadrant /  top-left
    for y in range (0, sliceY):
        for x in range(0, sliceX):
            #print("Evaluating: [%i , %i]" % (x, y))
            if grid[y][x] != 0:
                tl += grid[y][x]
                #print("Found bot: ",grid[y][x])
    #print("End Top Left")
    #evaluate second quadrant /  top-right
    for y in range (0, sliceY):
        for x in range(sliceX+1, w):
            #print("Evaluating: [%i , %i]" % (x, y))
            if grid[y][x] != 0:
                tr += grid[y][x]
                #print("Found bot: ",grid[y][x])
    #print("End Top Right")
    #evaluate third quadrant /  bottom-right
    for y in range (sliceY+1, h):
        for x in range(sliceX+1, w):
            #print("Evaluating: [%i , %i]" % (x, y))
            if grid[y][x] != 0:
                br += grid[y][x]
                #print("Found bot: ",grid[y][x])
    #print("End Bottom Right")
    #evaluate fourth quadrant /  bottom-left
    for y in range (sliceY+1, h):
        for x in range(0, sliceX):
            #print("Evaluating: [%i , %i]" % (x, y))
            if grid[y][x] != 0:
                bl += grid[y][x]
                #print("Found bot: ",grid[y][x])
    #print("End Bottom Left")
    print("Results: TL: %i | TR: %i | BR: %i | BL: %i" %(tl, tr, bl, br))
    return (tl * tr * bl * br)
    

def placeBot(grid, bot):
    x = bot[0]
    y = bot[1]
    grid[y][x] += 1
    return grid

def iterateBotPos(bot, vel, maxW, maxH):
    curX, curY = int(bot[0]), int(bot[1])
    velX, velY = int(vel[0]), int(vel[1])
    newbot = [curX, curY]

    if velX >= 0:
        if curX + velX >= maxW:
            newbot[0] = (curX + velX) - maxW
        else:
            newbot[0] = curX + velX
    elif velX <= 0:
        if curX + velX < 0:
            newbot[0] = (curX + velX) + maxW
        else:
            newbot[0] = curX + velX

    if velY >= 0:
        if curY + velY >= maxH:
            newbot[1] = (curY + velY) - maxH
        else:
            newbot[1] = curY + velY
    elif velY <= 0:
        if curY + velY < 0:
            newbot[1] = (curY + velY) + maxH
        else:
            newbot[1] = curY + velY
    return newbot

# Part One #
# maxW = 11
# maxH = 7
# grid = constructGrid(maxW, maxH)

# for i in range(0, 100):
#     for j in range(len(bots)):
#         bots[j] = iterateBotPos(bots[j], vels[j], maxW, maxH)


# for i in range(len(bots)):
#     placeBot(grid, bots[i])

# for row in grid:
#     print(row)

# print("Safety Factor: ",evaluateGrid(grid, maxW, maxH))

# Part Two #
maxW = 101
maxH = 103

for i in range(0, 1000):
    grid = constructGrid(maxW, maxH)
    for j in range(len(bots)):
        bots[j] = iterateBotPos(bots[j], vels[j], maxW, maxH)
        placeBot(grid, bots[j])
    for row in grid:
        print(row)
    print("Seconds Elapsed: ", i)
    time.sleep(0.3)

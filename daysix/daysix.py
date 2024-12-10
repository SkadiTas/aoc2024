# Import data and format #
data = open("./input.txt", "r").read().splitlines()

guards = ['^', '>', 'v', '<']

#guard[0] = row/y-pos
#guard[1] = column/x-pos
#guard[2] = direction
#guard[3] = traversed
#guard[4] = Is the guard still on the map?
def findGuard():
    for y in range(len(data)):
        for x in range(len(data[y])):
            #Find guard
            if data[y][x] in guards:
                currentY = y
                currentX = x
                direction = guards.index(data[y][x])
    return [currentY, currentX, direction, 1, True]

guard = findGuard()

def goDir(guard):
    if guard[2] == 0:
        print("Up")
        #use the same x coordinate, check decreasing y coordinate until obstacle or edge
        for y in reversed(range(0, guard[0])):
            if data[y][guard[1]] == '#':
                dist = guard[0] - y
                guard[3] += (dist-1)
                guard[0] = y+1
                if guard[2] < 3:
                    guard[2] += 1
                else:
                    guard[2] = 0
                return guard
            elif data[y][guard[1]] == '.':
                continue
            else:
                print("Bounds reached, guard exiting")
                dist = guard[0]
                guard[3] += dist
                guard[4] = False
                return guard

    elif guard[2] == 1:
        print("Right")
        #use the same y coordinate, check increasing x coordinate until obstance or edge
        for x in range(guard[1], len(data[0])):
            if data[guard[0]][x] == '#':
                dist = x - guard[1]
                guard[3] += (dist-1)
                guard[1] = x-1
                if guard[2] < 3:
                    guard[2] += 1
                else:
                    guard[2] = 0
                return guard
            elif data[guard[0]][x] == '.':
                continue
            else:
                print("Bounds reached, guard exiting")
                dist = len(data[0]) - guard[1]
                guard[3] += dist
                guard[4] = False
                return guard

    elif guard[2] == 2:
        print("Down")
        #use the same x coordinate, check increasing y coordinate until obstacle or edge
        for y in range(guard[0], len(data)):
            if data[y][guard[1]] == '#':
                dist = y - guard[0]
                guard[3] += (dist-1)
                guard[0] = y-1
                if guard[2] < 3:
                    guard[2] += 1
                else:
                    guard[2] = 0
                return guard
            elif data[y][guard[1]] == '.':
                continue
            else:
                print("Bounds reached, guard exiting")
                dist = len(data) - guard[0]
                guard[3] += dist
                guard[4] = False
                return guard

    elif guard[2] == 3:
        print("Left")
        #use the same y coodinate, check decreasing x coordinate until obstacle or edge
        for x in reversed(range(0, len(data[0]))):
            if data[guard[0]][x] == '#':
                dist = guard[1] - x
                guard[3] += (dist-1)
                guard[1] = x+1
                if guard[2] < 3:
                    guard[2] += 1
                else:
                    guard[2] = 0
                return guard
            elif data[guard[0]][x] in ['.', '^']:
                continue
            elif x == len(data[0]):
                print("Bounds reached, guard exiting")
                dist = guard[1]
                guard[3] += dist
                guard[4] = False
                return guard
    return guard

while guard[4] == True:
    guard = goDir(guard)

print("Patrol complete, traversed distance: ", guard[3])
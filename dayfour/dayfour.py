# Data Import #
data = open("./input.txt", "r")
rows = []

for line in data:
    parsed = filter(None, line.split("\n"))
    rows.append(list(parsed))

# Grid-ify #
grid = []
for i in range(len(rows)):
    grid.append([list(row) for row in rows[i]])


#def findNextLetter(grid, ypos, xpos, goal):
#something something

currentLetter = None
foundCount = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        for k in range(len(grid[i][j])):
            currentLetter = grid[i][j][k]


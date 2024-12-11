# Input data and formatting #
data = open("./input.txt", "r").read().strip()

grid = data.split('\n')
rows = len(grid)
columns = len(grid[0])

p1 = 0
p2 = 0

for r in range(rows):
    for c in range(columns):
        if grid[r][c] == '^':
            startrow,startcol = r,c

for nrow in range(rows):
    for ncol in range(columns):
        r,c = startrow,startcol
        d = 0 #0 up 1 right 2 down 3 left
        seen = set()
        seendir = set()
        while True:
            if (r,c,d) in seendir:
                p2 += 1
                break
            seendir.add((r,c,d))
            seen.add((r,c))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<rows and 0<=cc<columns):
                if grid[nrow][ncol]=='#':
                    p1 = len(seen)
                break
            if grid[rr][cc]=='#' or rr==nrow and cc==ncol:
                d = (d+1)%4
            else:
                r = rr
                c = cc
print("Part One Answer: ",p1)
print("Part Two Answer: ",p2)
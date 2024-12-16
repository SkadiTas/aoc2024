import re, sys, sympy as sp

data = open("./input.txt", "r").read()

pattern = (
    r"Button A: X\+(\d+), Y\+(\d+)\n"
    r"Button B: X\+(\d+), Y\+(\d+)\n"
    r"Prize: X=(\d+), Y=(\d+)"
)

matches = re.findall(pattern, data)

ax = [int(match[0]) for match in matches]
ay = [int(match[1]) for match in matches]
bx = [int(match[2]) for match in matches]
by = [int(match[3]) for match in matches]
sum_x = [int(match[4]) for match in matches]
sum_y = [int(match[5]) for match in matches]
sum_x_pt2 = [(int(match[4]) + 10000000000000) for match in matches]
sum_y_pt2 = [(int(match[5]) + 10000000000000) for match in matches]

def evaluatePrize(adata, bdata, p):
    a, b = sp.symbols('a b')
    #unpack the bunttons n prize
    ax, ay = adata[0], adata[1] 
    bx, by = bdata[0], bdata[1]

    prizex, prizey = p[0], p[1]

    eq1 = sp.Eq(a * ax + b * bx, prizex)
    eq2 = sp.Eq(a * ay + b * by, prizey)

    solution = sp.solve((eq1, eq2), (a, b))

    if solution:
        founda = solution[a]
        foundb = solution[b]
        if founda.is_integer and foundb.is_integer:
            return ((founda * 3) + (foundb))
        else:
            return 0
    else:
        return 0

# Part One #
totalCost = 0
for i in range(len(matches)):
    btnA = [ax[i], ay[i]]
    btnB = [bx[i], by[i]]
    prize = [sum_x[i], sum_y[i]]
    totalCost += evaluatePrize(btnA, btnB, prize)
    sys.stdout.write("\r(Part One) Current Game: %i | Current Cost: %i" %(i, totalCost))
print("\nTotal Cost For All Possible Prizes (Part One): ", totalCost)

# Part Two #
totalCost = 0
for i in range(len(matches)):
    btnA = (ax[i], ay[i])
    btnB = (bx[i], by[i])
    prize = (sum_x_pt2[i], sum_y_pt2[i])
    totalCost += evaluatePrize(btnA, btnB, prize)
    sys.stdout.write("\r(Part Two) Current Game: %i | Current Cost: %i" %(i, totalCost))
print("\nTotal Cost For All Possible Prizes (Part Two): ", totalCost)
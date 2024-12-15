import re, sys, time
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

def sumArrays(a, b):
    sum = []
    for i in range(len(a)):
        sum.append(a[i] + b[i])
    return sum


def evaluatePrize(a, b, p, loops):
    cost = 0
    for i in range(1, loops):
        sa = [c * i for c in a]
        for j in range(1, loops):
            sb = [c * j for c in b]
            t = sumArrays(sa, sb)
            if t == p:
                if cost == 0:
                    #first found result
                    cost = ((3*i) + j)
                elif ((3*a)+b) < cost:
                    cost = ((3*i) + j)
            if t > p:
                break
    return cost

# Part One #
totalCost = 0
for i in range(len(matches)):
    btnA = [ax[i], ay[i]]
    btnB = [bx[i], by[i]]
    prize = [sum_x[i], sum_y[i]]
    totalCost += evaluatePrize(btnA, btnB, prize, 100)
print("Total Cost For All Possible Prizes (Part One): ", totalCost)

# Part Two #
totalCost = 0
maxgoal = (max(max(sum_x_pt2), max(sum_y_pt2)))
minmultiple = int(min(min(ax), min(ay), min(bx), min(by)))
loopMax = round(maxgoal / minmultiple)

for i in range(len(matches)):
    btnA = [ax[i], ay[i]]
    btnB = [bx[i], by[i]]
    prize = [sum_x_pt2[i], sum_y_pt2[i]]
    totalCost += evaluatePrize(btnA, btnB, prize, 100)
print("Total Cost For All Possible Prizes (Part Two): ", totalCost)
import itertools
# Import data and format #
data = open("./input.txt", "r").read().splitlines()
operators = ['+', '*', '||']
formatted = []
vals = []
sums = []
p1 = 0

for row in data:
    splitted = row.split(':')
    formatted.append(splitted)

for row in formatted:
    vals.append(int(row[0]))
    stripped = str(row[1]).strip()
    lsum = [int(n) for n in stripped.split(' ')]
    sums.append(lsum)


def evaluate(num1, num2, operator):
    if operator in ['*','+']:
        return eval(f"{num1} {operator} {num2}")
    else: 
        return int(str(num1) + str(num2))

for sublist in sums:
    goal = vals[sums.index(sublist)]
    found = False

    ops = [p for p in itertools.product(operators, repeat=(len(sublist)-1))]

    for combination in ops:
        if found == False:
            result = sublist[0]
            for i, op in enumerate(combination):
                result = evaluate(result, sublist[i+1], op)

            if result == goal:
                print("Successfully found: ", goal)
                p1 += result
                found = True
                break
        else:
            break

print(p1)

#Completed part 1 and part 2 (combined)
# To revert to p1 just remove the concat operator from the list of operators at the top
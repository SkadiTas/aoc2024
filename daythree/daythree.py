import re

data = open("./input.txt", "r")
string = data.read()

equations = re.findall("(?<=mul\()\d{1,3},\d{1,3}(?=\))", string)
vals = []
for pair in equations:
    pair = pair.split(",")
    vals.extend(pair)

numbers = [int(num) for num in vals]

evens = []
odds = []
for i in range(len(numbers)):
    if i % 2 == 0:
        evens.append(numbers[i])
    else:
        odds.append(numbers[i])

toCalc = []
for i in range(len(evens)):
    tot = evens[i] * odds[i]
    toCalc.append(tot)

print("Part One Answer: ",sum(toCalc))

#--------------------------------------------#

pt2list = re.findall("((?<=mul\()\d{1,3},\d{1,3}(?=\)))|(do\(\))|(don\'t\(\))", string)

go = True
vals2 = []

for i in range(len(pt2list)):
    if pt2list[i][1] == "do()":
        go = True
    elif pt2list[i][2] == "don't()":
        go = False

    if go == True:
        pair2 = pt2list[i][0].split(",")
        vals2.extend(pair2)
    elif go == False:
        continue

numbers2 = [int(num) for num in vals2 if num]

evens2 = []
odds2 = []
for i in range(len(numbers2)):
    if i % 2 == 0:
        evens2.append(numbers2[i])
    else:
        odds2.append(numbers2[i])

toCalc2 = []
for i in range(len(evens2)):
    tot2 = evens2[i] * odds2[i]
    toCalc2.append(tot2)

print("Part Two Answer: ",sum(toCalc2))
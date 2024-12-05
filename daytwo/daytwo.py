# Data Input & Sorting #
data = open("./input.txt", "r")
#data = open("./testinput.txt", "r")
rows = []

for line in data:
    parsed = filter(None, line.split("\n"))
    rows.append(list(parsed))

lists = [[int(num) for num in row[0].split()] for row in rows]

# Helper Functions #
def isSorted(report):
    sortedDesc = sorted(report, reverse=True)
    sortedAsc = sorted(report, reverse=False)
    return report == sortedAsc or report == sortedDesc

def isSafe(report):
    for i in range(len(report)-1):
        if 1 <= abs(report[i] - report[i+1]) <= 3:
            continue
        else:
            return False
    return True

def deleteForSafety(report):
    for i in range(len(report)):
        checkReport = report.copy()
        del checkReport[i]
        if isSorted(checkReport) and isSafe(checkReport):
            return True
        else:
            continue

# Part One #
safeSum = 0
for i in range(len(lists)):                     
    if isSorted(lists[i]) and isSafe(lists[i]):
        safeSum += 1

print("Part One Answer: ", safeSum)

#------------------------------------------#

# Part Two #
newSafeSum = 0

for i in range(len(lists)):
    if isSorted(lists[i]) and isSafe(lists[i]):
        newSafeSum += 1
    elif deleteForSafety(lists[i]):
        newSafeSum += 1

print("Part Two Answer: ", newSafeSum)
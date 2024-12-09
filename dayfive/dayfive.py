# Import data and format #
data = open("./input.txt", "r").read().splitlines()

rules = []
pageData = []
pages = []

for line in data:
    if '|' in line:
        rules.append(line)
    elif ',' in line:
        pageData.append(line)

for page in pageData:
    pages.append(page.split(','))

# Helper function for sum of middles #
def getSumFromList(safeList):
    totalSafeSum = 0
    for page in safeList:
        middle = len(page) // 2
        totalSafeSum += int(page[middle])
    return totalSafeSum

#-------- Part One --------#
befores = []
afters = []
for rule in rules:
    befores.append(rule[:2])
    afters.append(rule[3:])

def getSafeList():
    safeList = pages.copy()
    for i in range(len(pages)):
        for k in range(len(befores)):
            if befores[k] in pages[i] and afters[k] in pages[i]:
                beforeIndex = pages[i].index(befores[k])
                afterIndex = pages[i].index(afters[k])
                if beforeIndex > afterIndex and pages[i] in safeList:
                    del safeList[safeList.index(pages[i])]
    return safeList
        
safeList = getSafeList()
partOneAnswer = getSumFromList(safeList)
print("Part One Answer: ",partOneAnswer)

#-------- Part Two --------#
def findUnsafeList():
    unSafeList = pages.copy()
    for i in range(len(pages)):
        for k in range(len(befores)):
            if befores[k] in pages[i] and afters[k] in pages[i]:
                beforeIndex = pages[i].index(befores[k])
                afterIndex = pages[i].index(afters[k])
                if beforeIndex < afterIndex and pages[i] in unSafeList:
                    del unSafeList[unSafeList.index(pages[i])]
    return unSafeList

def makeToSafeList(unSafeList):
    for i in range(len(unSafeList)):
        for k in range(len(befores)):
            if befores[k] in unSafeList[i] and afters[k] in unSafeList[i]:
                beforeIndex = unSafeList[i].index(befores[k])
                afterIndex = unSafeList[i].index(afters[k])
                if beforeIndex > afterIndex:
                    unSafeList[i][afterIndex], unSafeList[i][beforeIndex] = unSafeList[i][beforeIndex], unSafeList[i][afterIndex]
    return unSafeList

unSafeList = findUnsafeList()
partTwoCheckList = makeToSafeList(unSafeList)
partTwoAnswer = getSumFromList(partTwoCheckList)
print("Part Two Answer: ",partTwoAnswer)





                
        
        



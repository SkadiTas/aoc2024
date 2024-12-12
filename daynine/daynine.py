data = open("./input.txt", "r").read()
nums = [int(d) for d in str(data)]

# ---------- Part One --------- #
datalist = []

# for i, num in enumerate(nums):
#     if i % 2 == 0:
#         for j in range(0, num):
#             datalist.append(round(i / 2))
#     else:
#         for j in range(0, num):
#             datalist.append('.')

# def getLastNum(index):
#     for i in reversed(range(len(datalist))):
#         if i == index:
#             return "Done"
#         elif datalist[i] != '.':
#             return i

# for i in range(len(datalist)):
#     if datalist[i] == '.':
#         toSwap = getLastNum(i)
#         if toSwap == "Done":
#             print("Stopped at index: ", i)
#             break
#         else:
#             datalist[i], datalist[toSwap] = datalist[toSwap], datalist[i]

# checksum = 0
# for i, id in enumerate(datalist):
#     if id != '.':
#         checksum += (i * int(id))


# ---------- Part Two --------- #
list2 = []

for i, num in enumerate(nums):
    if i % 2 == 0:
        for j in range(0, num):
            list2.append(round(i / 2))
    else:
        for j in range(0, num):
            list2.append('.')

#Returns the index of the first location where a swap for that data can occur
def getSpace(data, index):
    for i in range(len(list2)):
        if list2[i] == '.':
            index = i
            space = 0
            for j in range(data+1):
                if i + j < len(list2):
                    if list2[i+j] == '.':
                        space += 1
                        if space == data:
                            return index
                    else:
                        break

attempted = [list2[0]]
for i in range(len(list2)-1, 0, -1):
    if list2[i] != '.':
        char = list2[i]
        space = list2.count(list2[i])
        swapfrom = getSpace(space, i)
        
        if swapfrom != None:
            if char not in attempted and (i-j) > swapfrom+j:
                for j in range(0, space):
                    #print("Moving ",list2[i-j], " from index ", i-j, " to index ",swapfrom+j)
                    list2[i-j], list2[swapfrom+j] = list2[swapfrom+j], list2[i-j]
        attempted.append(char)


checksum = 0
for i, id in enumerate(list2):
    if id != '.':
        checksum += (i * int(id))
print(checksum)
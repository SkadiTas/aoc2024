import sys
data = open("./input.txt", "r").read().split()
nums = [int(d) for d in data]


def blink():
    newlist = []
    for i in range(len(nums)):
        #print("working on: ",nums[i])
        digits = len(str(nums[i]))
        if nums[i] == 0:
            #print("This number is zero: ",nums[i])
            newlist.append(1)
        elif (digits % 2) == 0:
            #print("This number has an even amount of digits: ",nums[i])
            split = round(digits / 2)
            num = str(nums[i])
            r1 = num[:split]
            r2 = num[split:]
            newlist.append(int(r1))
            newlist.append(int(r2))
        else:
            #print("This number will be multiplied by 2024: ",nums[i])
            newlist.append(int(nums[i]) * 2024)
    return newlist

for i in range(0, 75):
    nums = blink()
    sys.stdout.write("\rPart One Answer: %i | %i" %(len(nums),i))
import sys
data = open("./input.txt", "r").read().split()
nums = [int(d) for d in data]
tracking = {}

def blink(num, targetBlinks):
    if targetBlinks == 0:
        return 1
    if (num, targetBlinks) in tracking:
        return tracking[(num, targetBlinks)]
    digits = len(str(num))
    if num == 0:
        result = blink(1, targetBlinks-1)
    elif (digits % 2) == 0:
        split = round(digits / 2)
        num = str(num)
        r1 = int(num[:split])
        r2 = int(num[split:])
        result = blink(r1, targetBlinks-1)
        result += blink(r2, targetBlinks-1)
    else:
        result = blink(num * 2024, targetBlinks-1)
    tracking[(num, targetBlinks)] = result
    return result

targetBlinks = 75
answer = 0
for i in range(len(nums)):
    stones = blink(nums[i], targetBlinks)
    answer += stones

print("Part Two Answer: ", answer)
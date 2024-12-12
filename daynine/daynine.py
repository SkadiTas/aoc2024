data = open("./input.txt", "r").read()
nums = [int(d) for d in str(data)]

blocks = ''

for i, num in enumerate(nums):
    for k in range(0, num):
        if i % 2 == 0:
            blocks += str(round(i / 2))
        else:
            blocks += '.'

datalist = list(blocks)
dots = datalist.count('.')

for i in range(len(datalist) - dots):
    if datalist[i] == '.':
        last = i * -1
        datalist[i], datalist[last] = datalist[last], datalist[i]

print(''.join(datalist))
with open('./day2/day2.txt') as raw:
    data = [line.strip('\n').split('x') for line in raw.readlines()]
for idx, value in enumerate(data):
    data[idx] = [int(i) for i in value]

print(data)

# ribbon_length = []
# perimiter = []

# for l, w, h in data:
#     ribbon = sorted([l, w, h])
#     ribbon = 2 * (ribbon[0] + ribbon[1])

#     bow = l * w * h
#     total = ribbon + bow

#     ribbon_length.append(total)

# ribbon_length = sum(ribbon_length)

# print(ribbon_length)

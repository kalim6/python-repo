with open('./day2/day2.txt') as raw:
    data = [line.strip('\n').split('x') for line in raw.readlines()]
for idx, value in enumerate(data):
    data[idx] = [int(i) for i in value]

wp = []
for l, w, h in data:
    a = l*w
    b = w*h
    c = h*l
    total_paper = 2*a + 2*b + 2*c + min(a, b, c)

    wp.append(total_paper)
wp = sum(wp)
print(wp)

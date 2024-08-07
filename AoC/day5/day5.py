with open('./AoC/day5/day5.txt', 'r') as data:
    data = (data.read())


vowels = ['a', 'e', 'i', 'o', 'u']
not_this = ['ab', 'cd', 'pq', 'xy']
string = 'aaaaaxya'


condition1 = any(a in string for a in vowels)

condition2 = True
# for b in not_this:
#     if b in string:
#         condition2 = True

condition3 = any(c in string for c in not_this)


print(condition1, condition2, condition3)

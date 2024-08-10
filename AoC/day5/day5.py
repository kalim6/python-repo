# Reading the data from the file
with open('./AoC/day5/day5.txt', 'r') as raw:
    data = [line.strip() for line in raw.readlines()]

vowels = ['a', 'e', 'i', 'o', 'u']
not_this = ['ab', 'cd', 'pq', 'xy']

nice_strings_count = 0

for string in data:
    condition1 = sum(1 for char in string if char in vowels) >= 3

    condition2 = any(string[i] == string[i + 1]
                     for i in range(len(string) - 1))

    condition3 = not any(substring in string for substring in not_this)

    nice_strings_check = all([condition1, condition2, condition3])

    if nice_strings_check:
        nice_strings_count += 1

print(nice_strings_count)

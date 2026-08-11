numbers = [2, 4, 2, 5, 4, 2, 6, 5, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
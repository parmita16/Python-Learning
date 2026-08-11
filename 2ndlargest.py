numbers = [10, 25, 5, 40, 30, 40, 15]

largest = numbers[0]
second = None

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num

print("Largest:", largest)
print("Second Largest:", second)
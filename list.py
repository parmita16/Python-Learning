# ==========================
# PYTHON LISTS - COMPLETE DEMO
# ==========================

# 1. Creating a list
fruits = ["Apple", "Banana", "Mango"]
print("Original list:", fruits)

# --------------------------
# 2. Accessing elements
# --------------------------
print("\nAccessing Elements")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# --------------------------
# 3. Changing an element
# --------------------------
fruits[1] = "Orange"
print("\nAfter changing Banana to Orange:")
print(fruits)

# --------------------------
# 4. Adding elements
# --------------------------
fruits.append("Grapes")
print("\nAfter append():")
print(fruits)

fruits.insert(1, "Pineapple")
print("\nAfter insert():")
print(fruits)

# --------------------------
# 5. Removing elements
# --------------------------
fruits.remove("Orange")
print("\nAfter remove('Orange'):")
print(fruits)

removed = fruits.pop()
print("\nAfter pop():")
print("Removed:", removed)
print(fruits)

# --------------------------
# 6. Length
# --------------------------
print("\nLength of list:", len(fruits))

# --------------------------
# 7. Checking if item exists
# --------------------------
print("\nChecking items")
print("Apple" in fruits)
print("Banana" in fruits)

# --------------------------
# 8. Loop through list
# --------------------------
print("\nLooping through the list")

for fruit in fruits:
    print(fruit)

# --------------------------
# 9. Slicing
# --------------------------
numbers = [10, 20, 30, 40, 50, 60]

print("\nNumbers:", numbers)
print("First 3:", numbers[:3])
print("Last 3:", numbers[3:])
print("Middle:", numbers[1:5])

# --------------------------
# 10. Sorting
# --------------------------
scores = [85, 40, 95, 70, 60]

print("\nScores:", scores)

scores.sort()
print("Ascending:", scores)

scores.sort(reverse=True)
print("Descending:", scores)

# --------------------------
# 11. Reversing
# --------------------------
scores.reverse()
print("Reversed:", scores)

# --------------------------
# 12. Copying
# --------------------------
copy_scores = scores.copy()

print("\nCopied list:")
print(copy_scores)

# --------------------------
# 13. Built-in functions
# --------------------------
print("\nStatistics")
print("Max:", max(scores))
print("Min:", min(scores))
print("Sum:", sum(scores))
print("Average:", sum(scores) / len(scores))

# --------------------------
# 14. User input into a list
# --------------------------
print("\nEnter 5 numbers")

user_numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    user_numbers.append(num)

print("\nYour numbers:", user_numbers)

print("Largest:", max(user_numbers))
print("Smallest:", min(user_numbers))
print("Sum:", sum(user_numbers))
print("Average:", sum(user_numbers) / len(user_numbers))

# --------------------------
# 15. Clearing a list
# --------------------------
temp = [1, 2, 3]

print("\nBefore clear():", temp)

temp.clear()

print("After clear():", temp)

print("\n===== End of Program =====")
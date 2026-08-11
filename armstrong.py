number = 153

original = number
digits = len(str(number))
total = 0

while number > 0:
    digit = number % 10
    total += digit ** digits
    number //= 10

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
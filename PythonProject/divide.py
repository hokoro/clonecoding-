numbers = [0 for i in range(10)]

for i in  numbers:
    value = int(input())
    numbers.append(value%42)


numbers = set(numbers)

print(len(numbers))


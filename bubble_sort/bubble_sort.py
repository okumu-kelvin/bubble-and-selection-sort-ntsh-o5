numbers = [5, 4, 3, 2, 1, 0]

n = len(numbers)

for i in range(n - 1):  # Outer loop: runs n-1 times. On each pass, the biggest number "bubbles" to the end.
    for j in range(n - 1 - i):  # Inner loop: avoids already sorted part at the end.
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print(numbers)


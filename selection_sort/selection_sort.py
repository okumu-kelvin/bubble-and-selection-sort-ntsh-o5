numbers = [5, 4, 3, 2, 1, 0]

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    
print("Sorted list:", numbers)

# Matthew Lai
# 02/10/25
# Bubblesort Implementation in Python

nums = input("Enter a list of space seperated numbers:\n")
numbers = [int(x) for x in nums.split()]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
          
print("Sorted List")
print(numbers)



# 1
nums = [1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]
summ = 0
# print("Сумма списков: ")
# for i in range(3):
#     for j in range(4):
#         summ += nums[i][j]
#     print(summ)

# 2
#part1
for i in range(3):
    for j in range(4):
        summ += nums[i][j]
print("Сумма всех элементов массива:\n", summ)

#part2
for i in range(3):
    for j in range(4):
        summ += nums[i][j]
result = summ / 12
print("\nСреднее арифметическое:\n", result)

#part3
minNum = nums[0]
maxNum = nums[0]
for i in nums:
    if i < minNum:
        minNum = i
    else:
        if i > maxNum:
            maxNum = i

print("\nМинимальный элемент:", minNum)
print("Максимальный элемент:",maxNum)
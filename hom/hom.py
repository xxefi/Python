# 1
# list = [2, 2, 2, 2, 2, 4, 6, 8, 10, 12]
# result = list.count(2)
# print(result)


# 2
# list = int(input())
# summ = 0
# average = 1
# while list > 0:
#     digit = list % 10
#     summ = summ + digit
#     average = average * digit / 2
#     list = list // 10
# print("Сумма:", summ)
# print("Среднее арифметическое:", average)


# 3
# list = [2, -4, 6, 8, 1, -3, 7, -9]
# sum1 = 0
# sum2 = 0
# sum3 = 0
# sum4 = 0
# sum5 = 0
# i = 0
# while i < len(list):
#     if i > 0:
#         sum1 += list(i)
#     elif i > 2:
#         sum2 += list(i)
#     elif i > 3:
#         sum3 += list(i)
#     elif i > 1:
#         sum4 *= list(i)
#     i += 1
#
# print('Сумма отрицательных чисел:', sum1)
# print('Сумма четных чисел:', sum2)
# print('Сумма нечетных чисел:', sum3)
# print('Произведение элементов с индексами кратными 3:', sum4)
# print('Произведение элементов  диапазоне между минимальным и максимальным элементом:', sum5)
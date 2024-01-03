# 1
# def MinIndex(someList):
#     li = someList[0]
#     for i in range(len(someList)):
#         if li >= someList[i]:
#             li = someList[i]
#             print("Мин.Значение:", li)
#     return someList.index(li), someList

# li = [0, 1, 2, 3]
# MinIndex(li)
#
# def MaxIndex(someList):
#     li = someList[0]
#     for i in range(len(someList)):
#         if li <= someList[i]:
#             li = someList[i]
#             print("Макс.Значение:", li)
#     return someList.index(li), someList
# #
# li = [5, -3, 9, 12, 31, 53, -1]
# MaxIndex(li)

#3
# def OddNums(a, b):
#     li = []
#     result = 0
#     for i in range(a, b):
#         if i % 2 != 0:
#             li.append(i)
#     return li
#
# print(OddNums(1, 20))


#4
# def PrintLine(lineLength, isHorizontal, symbol):
#     for i in range(lineLength-1):
#         if isHorizontal == "p":
#             print(symbol, end="")
#         elif isHorizontal == "k":
#             print(symbol)
#         return symbol


#5
# def Sum(startDiapason, endDiapason):
#     count = 0
#     for i in range(startDiapason, endDiapason):
#         count += 1
#     return count
#
# print(Sum(1, 10))

#6
# def Factorial(number):
#     count = 1
#     for i in range(2, +1):
#         count *= i
#     return count
#
# print(Factorial(0))
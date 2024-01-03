# 1
# text = ("Cat runs. Dog runs. Cat jumps.").lower()
# print("Текст:", text.title().split())
# words = input("Введите слово, который хотите искать:").lower()
# words2 = input("Ещё один:").lower()
# words3 = input("И ещё один:").lower()
# result1 = text.count(words)
# result2 = text.count(words2)
# result3 = text.count(words3)
# print("\nПервый результат и повторений:", result1)
# print("Второй результат и повторений:", result2)
# print("Третий результат и повторений:", result3)
# quit("\n==================================================Программа завершена=======================================================\n")


# 2
# text = ("Cat runs. Dog runs. Cat jumps").lower()
# originalText = "Cat runs. Dog runs. Cat jumps."
# print("Текст:", text.title())
# me1 = input("Введите слово, который хотите искать:").lower()
# me2 = input("Введите второе слово, который хотите искать:").lower()
# result = text.count(me1)
# result2 = text.count(me2)
# print("\nПервый результат и повторений:", result)
# print("Второй результат и повторений:", result2)
#
# user1 = input("\nВведите слово, который хотите заменить:").lower()
# user2 = input("Введите слово на замену:")
# change1 = user1
# to1 = user2
# count1 = 2
# text = text.replace(change1, to1, count1)
# print(text)
#
# user3 = input("\nВведите второе слово, который хотите заменить:").lower()
# user4 = input("Введите слово на замену:")
# change2 = user3
# to2 = user4
# count2 = 1
# text = text.replace(change2, to2, count2)
# print(text.title())
# print(f"\nОригинальный текст: {originalText} "
#       f"\nТекст после замены: {text}"
#       f"\nСтатистика: {user2} - {count1} "
#       f"\n\t\t\t{user4} - {count2}")
# quit("\n==================================================Результаты=======================================================")
#
#3(1)
# li1 = [2, 5, 1, 7, 0]
# li2 = [1, 7, 0, 2, 4]
# li3 = [3, 5, 1, 0, 2]
# li4 = [0, 7, 5, 2, 1]
# li5 = (li1+li2+li3+li4)
# print("1.Список по убыванию:", li5[::-1])

#3(2)
# li1 = [2, 5, 1, 7, 0]
# li2 = [1, 7, 0, 2, 4]
# li3 = [3, 5, 1, 0, 2]
# li4 = [0, 7, 5, 2, 1]
# li5 = (li1+li2+li3+li4)
# NewLi = []
# for i in li5:
#     if i not in NewLi:
#         NewLi.append(i)
# print("2.Уникальные элементы:",NewLi)

#3(3)
# li1 = [2, 5, 1, 7, 0]
# li2 = [1, 7, 0, 2, 4]
# li3 = [3, 5, 1, 0, 2]
# li4 = [0, 7, 5, 2, 1]
# li5 = []
# list5 = []
# res = []
# for i in li1:
#     if i in li2:
#         list5.append(i)
# for i in li3:
#     if i in li4:
#         li5.append(i)
# for i in list5:
#     if i in li5:
#         res.append(i)
# print("3.Общие элементы:", res)
# #3(4)
# li1 = [2, 5, 1, 7, 0]
# li2 = [1, 7, 0, 2, 4]
# li3 = [3, 5, 1, 0, 2]
# li4 = [0, 7, 5, 2, 1]
# li5 = (li1+li2+li3+li4)
# Li = []
# lists = li5
# for i in lists:
#         for j in range(2, i):
#             if (i % j == 0):
#                 break
#             if (j == i-1):
#                 Li.append(i)
# print("4.Простые числа:", Li)
# Li1 = []
# for i in Li:
#     if Li.count(i) == 1:
#         Li1.append(i)
# print("5.Уникальное число из списка простых чисел:", Li1)
# quit("\n==================================================Программа завершена=======================================================")

#4
# num = input("Введите пример:")
# resLi = []
# res = ""
# for i in range(len(num)):
#     if num[i] != "+" and num[i] != "-":
#         res += num[i]
#     if num[i] == "+" or num[i] == "-" or i == len(num)-1:
#         resLi.append(res)
#         res = num[i]
#     count = 0
#     for j in range(len(resLi)):
#         resLi[j] = int(resLi[j])
#         count += resLi[j]
# print("Ответ решений:", count)
# quit("\n==================================================Программа завершена=======================================================")
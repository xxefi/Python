#1
# text = input("enter string:")
# letter = input("search letter:")
# length = len(text)
# count = 0
# for i in range(length):
#     if text[i] == letter:
#         count += 1
# print(count)
# print("END")

#2
# text = input("enter string:")
# reversedText = ""
# length = len(text)-1
# for i in range(length, -1, -1):
#     reversedText += text[i]
# if text == reversedText:
#     print("Yes")
# else:
#     print("no")

#3
# text = input("enter string:")
# length = len(text)
# countLow = 0
# countUp = 0
# for i in range(length):
#     if ord(text[i]) > 96 and ord(text[i]) < 123:
#         countLow += 1
#     elif ord(text[i]) > 96 and ord(text[i]) < 123:
#         countUp += 1
# if countLow > 0 and countUp > 0:
#     print("mIxED")
# elif countLow > 0 and countUp > 0:
#     print("lowercase")
# elif countLow > 0 and countUp > 0:
#     print("UPPERCASE")

#4
# text = input("enter string:")
# letter = input("search letter:")
# length = len(text)
# count = 0
# for i in range(length):
#     if text[i] == letter:
#         count += 1
#     else:
#         print("Количество символов:")
#         break
# print(count)
# print("END")

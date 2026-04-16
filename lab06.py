# # 1
# def checkIf(x, y):
#     for i in y:
#         if i == x:
#             return True
#     return False


# # 2
# def AtoB(x):
#     new = ""
#     for i in x:
#         if i == "a":
#             new += "b"
#         elif i == "A":
#             new += "B"
#         elif i == "b":
#             new += "a"
#         elif i == "B":
#             new += "A"
#         else:
#             new += i
#     return new


# # 3
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def wordCounter(x):
#     counter = 0
#     index = 0
#     lamp = 0
#     while index < length(x):
#         if x[index] != " " and lamp == 0:
#             counter += 1
#             lamp = 1
#         elif x[index] == " ":
#             lamp = 0
#         index += 1
#     return counter

# # 4
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def maxLength(x):
#     index = 0
#     leng = 0
#     max = 0
#     while index < length(x):
#         if x[index] != " ":
#             leng += 1
#         elif x[index] == " ":
#             if max < leng:
#                 max = leng
#             leng = 0
#         index += 1
#     return max


# # 5
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def initial(x):
#     index = 0
#     result1 = ""
#     result2 = ""
#     lamp = 0
#     elm = 0
#     while index < length(x):
#         if x[index] != " ":
#             if lamp == 0:
#                 result1 += x[index]
#             elif elm == 0 and "A" <= x[index] <= "Z":
#                 result2 += x[index] + "."
#                 elm = 1
#         else:
#             lamp = 1
#             elm = 0
#         index += 1
#     return result2 + " " + result1


#6
# address = input("file address: ")
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# index = 0
# result = ""
# while index < length(address):
#     if address[index] != "/":
#         result += ""
#     else:
#         print(result)
#         result = 0
#     index += 1



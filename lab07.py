# # 1
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
# for i in range(length(tuple)):
#     if tuple[i] == 24:
#         print(i, end=" ")


# # 2
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
# for i in range(length(tuple)):
#     if tuple[i] % 3 == 0:
#         print(tuple[i], end=" ")


# # 3
# list1 = []
# list2 = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     list1 += [num]
#     list2 += [num + 5]
#
# print(f"list1 = {list1} \n list2 = {list2}")


# # 4
# list1 = []
# list2 = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     list1 += [num]
#     if num % 2 == 1:
#         list2 += [num]
#
# print(f"list1 = {list1} \n list2 = {list2}")


# # 5
# import random
#
# lst = []
# for i in range(7):
#     lst += [random.randint(0, 10)]
#
#
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def summary(x):
#     sum = 0
#     for i in x:
#         sum += x
#     return sum
#
#
# def product(x):
#     pro = 1
#     for i in x:
#         pro *= i
#     return pro
#
#
# def mean(x):
#     return summary(x) / length(x)
#
#
# def maxNindex(x):
#     max = 0
#     index = 0
#     for i in range(length(x)):
#         if x[i] > max:
#             max = x[i]
#             index = i
#     return max, index
#
#
# def minNindex(x):
#     min = x[0]
#     index = 0
#     for i in range(length(x)):
#         if x[i] < min:
#             min = x[i]
#             index = i
#     return min, index
#
#
# print(f"List = {lst}")
# print(f"Cem = {summary(lst)} Hasil = {product(lst)} Ededi orta = {mean(lst)}")
# print(f"En boyuk eded ve indeksi: {maxNindex(lst)}")
# print(f"En kicik eded ve indeksi: {minNindex(lst)}")


# # 6
# import random
#
# lst = []
# under50 = []
# over50 = []
# for i in range(10):
#     num = random.randint(0, 10)
#     lst += [num]
#     if num < 50:
#         under50 += [num]
#     else:
#         over50 += [num]
#
#
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def summary(x):
#     sum = 0
#     for i in x:
#         sum += x
#     return sum
#
#
# def mean(x):
#     return summary(x) / length(x)
#
#
# print(f"List = {lst}")
# print(f"[0, 50] araliginda ededi orta: {mean(under50)}")
# print(f"[50,100] araliginda ededi orta: {mean(over50)}")


# # 7
# lst = []
# for i in range(1, 16):
#     lst += [i ** 2]
#
# print("ilk 5 element: ", end="")
# for i in range(5):
#     print(lst[i], end=" ")
#
# print("\n son 5 element: ", end="")
# for i in range(-5, 0):
#     print(lst[i], end=" ")


# # 8
# def ifSame(x, y):
#     for i in x:
#         for j in y:
#             if i == j:
#                 return True
#     return False


# # 9
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def theSame(x, y):
#     counter = 0
#     if length(x) < length(y):
#         num = length(x)
#     else:
#         num = length(y)
#     for i in range(num):
#         if x[i] == y[i]:
#             counter += 1
#             print(x[i], end=" ")
#     print("\n", counter)


# # 10
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def leftRigth(x):
#     new = []
#     for i in range(1, length(x)):
#         new += [x[i]]
#     return new + [x[0]]


# # 11
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def makeNew(lst1, lst2):
#     new = [] * length(lst1)
#     for i in range(length(lst1)):
#         lst = [lst1[i]] + [lst2[i]]
#         new[i] = lst
#     return new


# # 12
# def until(x):
#     summ = 0
#     for i in x:
#         if i % 2 == 1:
#             summ += i
#         else:
#             return summ
#     return summ


# # 13
# n = int(input("The length of list: "))
# import random
#
# lst = []
# for i in range(n):
#     lst += [random.randint(10, 50)]
# new = []
# for i in lst:
#     if i ** 0.5 == int(i ** 0.5):
#         new += [i]
#
# print(f"Listin olcusu: {n}")
# print(f"List: {lst}")
# print(f"yaradilmis list: {new}")


# # 14
# def check(x):
#     f = abs(x % 10 - x % 100 // 10)
#     c = x % 10 + x % 100 // 10
#     if f % 2 == 1 and c % 2 == 1:
#         return True
#     return False
#
#
# n = int(input("The length of list: "))
# import random
#
# lst = []
# for i in range(n):
#     lst += [random.randint(100, 999)]
# new = []
# for i in lst:
#     if check(i):
#         new += [i]
#
# print(f"Listin olcusu: {n}")
# print(f"List: {lst}")
# print(f"yaradilmis list: {new}")


# # 15
# def isPrime(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return True
#     return False
#
#
# n = int(input("The length of list: "))
# import random
#
# lst = []
# for i in range(n):
#     lst += [random.randint(0, 100)]
# new = []
# for i in lst:
#     if isPrime(i):
#         new += [i]
#
# print(f"Listin olcusu: {n}")
# print(f"List: {lst}")
# print(f"yaradilmis list: {new}")



##16
# import random
#
# lst = []
# for i in range(10):
#     lst += [random.randint(-10, 10)]
# new = []
# for i in lst:
#     if i % 2 == 0 or i < 0:
#         new += [i]
#
# print(f"List: {lst}")
# print(f"yaradilmis list: {new}")


# # 17
# lst = [1, 3, "aasf", 56, "33", "1", -76]
# new = []
# for i in lst:
#     try:
#         if i > 0:
#             new += [i]
#     except:
#         continue
# print(new)


# # 18
# number = int(input("Enter a number: "))
# lst = []
# for i in range(1, number + 1):
#     if number % i == 0:
#         lst += [i]
#
# print(lst)

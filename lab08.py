# # 1
# import random
#
# x = int(input)
# result = 0
# lamp = 0
# for i in range(5):
#     num = random.randint(0, 5)
#     if x == num:
#         lamp = 1
#         result += f"A[{i}] = {num}"
# if lamp == 1:
#     print(f"Tapildi: {result}")
# else:
#     print("Tapilmadi.")


# # 2
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def sumDigitsOfList(x):
#     new = []
#     for i in x:
#         sum = 0
#         while i > 0:
#             sum += i % 10
#             i //= 10
#         new += [sum]
#     return new
#
#
# def stoneSort(myList):
#     x = sumDigitsOfList(myList)
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] < x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#                 myList[j], myList[j + 1] = myList[j + 1], myList[j]
#     return myList
#
#
# print(stoneSort([387, 455, 6, 75, 10, 1]))

# # 3
# lst = []
# for i in range(5):
#     lst += [input()]
#
#
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def arrangeList(x):
#     for i in range(length(x)):
#         x[i] = x[i][2:]
#     return x
#
#
# def bubbleSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# print(bubbleSort(arrangeList(lst)))

# # 4
# lst = []
# while True:
#     element = input()
#     if element == " ":
#         break
#     lst += [element]
#
#
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def bubbleSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# print(bubbleSort(lst))


# # 5
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def decSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] < x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# def incSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# import random
#
# myList = []
# for i in range(10):
#     myList += [random.randint(-100, 100)]
#
# print(f'Unsorted = {myList}')
# print(f"Sorted_1 = {decSort(myList)}")
# print(f"Sorted_2 = {incSort(myList[:5]) + incSort(myList[5:])}")

# # 6
# import random
#
# lst = []
# natural = []
# non_natural = []
# for i in range(10):
#     choice = random.randint(-100, 100)
#     if choice > 0:
#         natural += [choice]
#     else:
#         non_natural += [choice]
#
#
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def decSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] < x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# def incSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# print(
#     f"Massiv: {lst} \n Netice: {incSort(non_natural) + decSort(natural)} \n Musbet ededlerinn sayi: {length(natural)}")


# # 7
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def bubbleSort(x):
#     n = length(x)
#     counter = 0
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#                 counter += 1
#     return counter
#
#
# def selection(x):
#     for i in range(length(x) - 1):
#         nMin = i
#         counter = 0
#         for j in range(i + 1, length(x)):
#             if x[j] < x[nMin]:
#                 nMin = j
#         if i != nMin:
#             x[i], x[nMin] = x[nMin], x[i]
#             counter += 1
#     return counter
#
#
# import random
#
# lst1 = []
# lst2 = []
# lst3 = []
# lst4 = []
# lst5 = []
# for i in range(1000):
#     lst1 += [random.randint(-1000, 1000)]
#     lst2 += [random.randint(-1000, 1000)]
#     lst3 += [random.randint(-1000, 1000)]
#     lst4 += [random.randint(-1000, 1000)]
#     lst5 += [random.randint(-1000, 1000)]
#
# sumBubble = bubbleSort(lst1) + bubbleSort(lst2) + bubbleSort(lst3) + bubbleSort(lst4) + bubbleSort(lst5)
# sumSelect = selection(lst1) + selection(lst2) + selection(lst3) + selection(lst4) + selection(lst5)
#
# print(f"Bubble: {sumBubble / 5} \n Selection: {sumSelect / 5}")


# # 8
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def incSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# import random
#
# lst = []
# for i in range(10):
#     lst += [random.randint(-100, 100)]
#
# print(f"Massiv: {lst}")
#
# lst = incSort(lst)
#
# print(f"After sorting: {lst}")
#
# x = int(input("Enter a number: "))
# counter = 0
# lamp = 0
# for i in lst:
#     counter += 1
#     if i == x:
#         lamp = 1
#         break
# if lamp == 1:
#     print(f"{x} has been found.")
# else:
#     print(f"{x} has not been found.")
#
# print(f"The number of comparisons: {counter}")

# #8(Binary)
# def bubble_sort(A):
#    N = len(A)
#    for i in range(N - 1):
#        for j in range(N - i - 1):
#            if A[j] > A[j + 1]:
#                A[j], A[j + 1] = A[j + 1], A[j]
#    return A
#
# def binary_search(A, target):
#    left = 0
#    right = len(A) - 1
#    count = 0
#    while left <= right:
#        mid = (left + right) // 2
#        count += 1
#        if target == A[mid]:
#            return mid, count
#        else:
#            if target > A[mid]:
#                left = mid + 1
#            else:
#                right = mid - 1
#    return -1
#
# arr = [1, 4, 7, 3, 9, 2, 4, 5, 2]
# print("Massiv:", end = "")
# for i in arr: print(i, end = " ")
# bubble_sort(arr)
# print("\nCheshidlenmeden sonra:", end = "")
# for i in arr: print(i, end = " ")
#
# X = int(input("\nX ededi daxil edin: "))
#
# count = binary_search(arr, X)[1]
# index = binary_search(arr, X)[0]
#
# if index == -1:
#    print("Tapilmadi")
# else:
#    print(f"Tapildi. A[{index}] = {X}")
#    print(f"Muqayise sayi: {count}")



# # 9
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def incSort(x):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 x[j], x[j + 1] = x[j + 1], x[j]
#     return x
#
#
# import random
#
# lst = []
# for i in range(10):
#     lst += [random.randint(-100, 100)]
#
# print(f"Massiv: {lst}")
#
# lst = incSort(lst)
#
# print(f"After sorting: {lst}")
#
# x = int(input("Enter a number: "))
# counter = 0
# for i in lst:
#     if i == x:
#         counter += 1
#
# if counter > 0:
#     print(f"{x} has been found {counter} times.")
# else:
#     print(f"{x} has not been found.")


# 10



# # 11
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def decSort(x, y):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] < x[j + 1]:
#                 y[j], y[j + 1] = y[j + 1], y[j]
#     return y
#
#
# def incSort(x, y):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 y[j], y[j + 1] = y[j + 1], y[j]
#     return y
#
#
# def oddCount(x):
#     counter = 0
#     while x > 0:
#         num = x % 10
#         x //= 10
#         if num % 2 == 1:
#             counter += 1
#     return counter
#
#
# def evenCount(x):
#     counter = 0
#     while x > 0:
#         num = x % 10
#         x //= 10
#         if num % 2 == 0:
#             counter += 1
#     return counter
#
#
# lst = [32343, 543, 6436, 3425, 7547, 87954, 1243, 8856]
# n = length(lst)
# lst1 = lst[:n // 2]
# lst2 = lst[n // 2:]
# print(f"List: {lst} \n First half: {lst1} \n Last half: {lst2}")
# lstOdd = []
# for i in lst1:
#     lstOdd += [oddCount(i)]
# lstEven = []
# for i in lst2:
#     lstEven += [evenCount(i)]
#
# print(f"Odd numbers counter(first half): {lstOdd} \n Even numbers counter(last half): {lstEven}")
# print(f"After shorting: {incSort(lstOdd, lst1) + decSort(lstEven, lst2)}")


# # 12
# def length(x):
#     counter = 0
#     for i in x:
#         counter += 1
#     return counter
#
#
# def decSort(x, y):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] < x[j + 1]:
#                 y[j], y[j + 1] = y[j + 1], y[j]
#     return y
#
#
# def incSort(x, y):
#     n = length(x)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if x[j] > x[j + 1]:
#                 y[j], y[j + 1] = y[j + 1], y[j]
#     return y
#
#
# def count_(x):
#     for i in range(length(x)):
#         counter = 0
#         while x > 0:
#             num = x % 10
#             x //= 10
#             if num > 0:
#                 counter += 1
#         x[i] = counter
#     return x
#
#
# lst = [1001, 11100, 6514, 9, 22, 124, 350, 12]
# n = length(lst) // 2
# lst1 = lst[n:]
# lst2 = lst[:n]
# print(f"input: {lst}")
# print(f"output: {incSort(count_(lst1), lst1) + decSort(count_(lst2), lst2)}")

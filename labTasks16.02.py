# # task1
# from random import choice
#
# number = 4
# while number <= 9:
#     number += 1
#     if number == 7 or number == 9:
#         continue
#     print(number)
#
# # task2
# summary = 0
# while True:
#     number = int(input("ededler daxl edin"))
#     if number == 0:
#         break
#     summary += number
#
# # task3
# summary = 0
# count = 0
# while True:
#     number = int(input())
#     if number == -1:
#         break
#     summary += number
#     count += 1
# if count > 0:
#     print(summary / count)
#
# # task4
# number = int(input("natural eded: "))
# summary = 0
# while number > 0:
#     lastNum = number % 10
#     number //= 10
#     summary += lastNum
# print(summary)
#
# # task5
# number = int(input("natural eded: "))
# usedNum = number
# reverseNum = 0
# while usedNum > 0:
#     lastNum = usedNum % 10
#     usedNum //= usedNum
#     reverseNum = reverseNum * 10 + lastNum
# if reverseNum == number:
#     print("polindrom")
# else:
#     print("polinrom deyil")
#
# # task6
# number = int(input("natural eded: "))
# check = number % 10
# lamp = 0
# while number > 0:
#     lastNum = number % 10
#     number //= 10
#     if lastNum == check:
#         lamp = 1
#         break
#     check = lastNum
# if lamp == 0:
#     print("yox")
# else:
#     print("var")
#
# # task7
# number = 100
# while number < 1000:
#     arm = 0
#     usedNum = number
#     while usedNum > 0:
#         lastNum = usedNum % 10
#         usedNum //= usedNum
#         arm = arm + lastNum ** 3
#     if arm == number:
#         print(number)
#     number += 1
#
# # task8
# number = int(input("natural eded daxil et: "))
# vuruq = 2
# while number > 1:
#     if number % vuruq == 0:
#         print(vuruq)
#         number //= vuruq
#     else:
#         vuruq += 1
#
# # task9
# binary = int(input("ikilikde eded daxil et: "))
# decimal = 0
# index = 0
# while binary > 0:
#     lastNum = binary % 10
#     binary //= 10
#     decimal = decimal + lastNum * 2 ** index
#     index += 1
# print(decimal)
#
# # task10
# decimal = int(input("onluq say sisteminde eded: "))
# binary = 0
# while decimal > 0:
#     number = decimal % 2
#     decimal //= 2
#     binary = binary * 10 + number
# print(binary)
#
# # task11
# fib1 = 1
# fib2 = 1
# fib3 = fib1 + fib2
# print(fib1, fib2, end=" ")
# while fib3 <= 50:
#     print(fib3, end=" ")
#     fib1 = fib2
#     fib2 = fib3
#     fib3 = fib1 + fib2
#
# # task12
# # A
# number = int(input("natural eded: "))
# index = number
# summary = 0
# while index >= 0:
#     summary += index / (1 + index ** 3) ** 0.5
#     index -= 1
# print("A: ", summary)
# # B
# index = 1
# summary = 0
# while index <= number:
#     summary += index ** index / index
#     index += 1
# print("B: ", summary)
#
# # task13
# number = int(input("natural eded: "))
# coice = int(input("secim et(1- reqemlerin cemi, 2-reqemlemrin hasili, 3-cixis): "))
# if choice == 1:
#     summary = 0
#     while number > 0:
#         lastNum = number % 10
#         number //= 10
#         summary += lastNum
#     print(summary)
# elif choice == 2:
#     hasil = 0
#     while number > 0:
#         lastNum = number % 10
#         number //= 10
#         hasil *= lastNum
#     print(hasil)
# elif choice == 3:
#     exit()
# else:
#     print("duzgun secim et")
#
# # task14
# number = int(input("natural eded: "))
# avt = 1
# while avt <= number:
#     if avt % 10 == (avt ** 2) % 10:
#         print(avt)
#     avt += 1
#
# # task15
# number = int(input("natural eded: "))
# while number > 0:
#     usedNum = number
#     lamp = 0
#     while usedNum > 0:
#         lastNum = usedNum % 10
#         usedNum //= usedNum
#         if number % lastNum != 0:
#             lamp = 1
#             break
#     if lamp == 0:
#         print(number)
#     number -= 1

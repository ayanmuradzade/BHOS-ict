# # task1
# def digits(x):
#     result = ""
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         result = str(lastNum) + " " + result
#     return result
#
#
# def sumDigits(x):
#     sum = 0
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         sum += lastNum
#     return sum
#
#
# def productDigits(x):
#     product = 1
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         product *= lastNum
#     return product
#
# def check(x):
#     nums = "1234567890"
#     for i in x[1:]:
#         if i not in nums:
#             return False
#     if x[0] == "-" or x[0] in nums:
#         return True
#     return False
#
#
# number = input("enter a number: ")
# if check(number):
#     number = abs(int(number))
#     print("Digits: ", digits(number))
#     print("Sum of digits: ", sumDigits(number))
#     print("Product of digits: ", productDigits(number))
# else:
#     print("enter only a number in integer type")


# # function
# x = float(input("enter x: "))
# y = float(input("enter y: "))
# if x < 0 and y > 0 and y > abs(x) - 1 and (x ** 2 + y ** 2 - 3) ** 3 - x ** 2 * y ** 3 < 0:
#     print("yes")
# elif (x ** 2 + y ** 2 - 3) ** 3 - x ** 2 * y ** 3 > 0 and y > abs(x) - 1 and (x - 2) ** 2 + (y - 1.5) ** 2 < 2:
#     print("yes")
# elif x > 0 and (x ** 2 + y ** 2 - 3) ** 3 - x ** 2 * y ** 3 < 0 and y < 0 and y < abs(x) - 1:
#     print("yes")
# else:
#     print("no")

# # coxboluneneded
# def lengthNum(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count
#
#
# def ifPolydivisible(number, length):
#     len = lengthNum(number) - 1
#     division = 1
#     lamp = 0
#     while len >= 0:
#         num = number // 10 ** len
#         print(num, "%", division, "=", num % division)
#         if num % division != 0:
#             lamp = 1
#         len -= 1
#         division += 1
#     if lamp == 0:
#         return True
#     return False
#
#
# number = int(input("natural eded: "))
# print(ifPolydivisible(number, lengthNum(number)))
# #1
# def check(x):
#     if x % 2 == 0:
#         return 'even'
#     return "odd"
#
#
# def sumNums():
#     sum = 0
#     while True:
#         num = int(input("enter a number"))
#         if num == -1:
#             return sum
#         sum += num
#
#
# print(check(sumNums()))


# # 2
# def check(x):
#     if x % 2 == 0:
#         return True
#     return False
#
#
# def find(x, y):
#     return x // y
#
#
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# print(check(find(a, b)))

# # 3
# def check(x, y):
#     if y ** y == x:
#         return True
#     return False
#
#
# n = int(input("enter n: "))
# k = int(input("enter k: "))
# print(check(n, k))

# # 4
# def check(x):
#     n = 1
#     while x > n:
#         if x / n == n + 1:
#           return "pronic"
#         n += 1
#     return "heteromecic"
#
#
# number = int(input("enter a number to check: "))
# print(check(number))

# # 5
# def countNum(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count
#
#
# number = abs(int(input("enter a number to count: ")))
# print(countNum(number))

# # 6
# def countNum(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count
#
#
# def ifDisarium(x):
#     count = countNum(x)
#     result = 0
#     usedNum = x
#     while usedNum > 0:
#         lastNum = usedNum % 10
#         usedNum //= 10
#         result = result + lastNum ** count
#         count -= 1
#     if x == result:
#         return True
#     return False
#
#
# number = int(input("enter a number to check if disarium: "))
# print(ifDisarium(number))

# # 7
# def ifCurzon(x):
#     if 2 * x + 1 % 2 * x + 1:
#         return True
#     return False
#
#
# number = int(input("enter a number to check if Curzon: "))
# print(ifCurzon(number))


# # 8
# def factorial(x):
#     fac = 1
#     for i in range(1, x + 1):
#         fac *= i
#     return fac
#
#
# def kempner(x):
#     result = 1
#     while factorial(result) % x != 0:
#         result += 1
#     return result
#
#
# number = int(input("enter a number: "))
# print(kempner(number))

# # 9
# def checkPrime(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % 1 == 0:
#             return True
#     return False
#
#
# def sumDigits(x):
#     sum = 0
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         sum += lastNum
#
#
# def ifMoran(x):
#     result = x // sumDigits(x)
#     if checkPrime(result):
#         return "Moran"
#     return "non-Moran"


# # 10
# def sumDigits(x):
#     lastNum = x % 10
#     while x > 9:
#         x //= 10
#     return (lastNum + x) ** 0.5
#
#
# def compare3(x):
#     if sumDigits(x) > 3:
#         return True
#     return False
#
#
# number = int(input("enter a number"))
# print(compare3(number))


# # 11
# def ebob(x, y):
#     while x != 0:
#         x, y = y, x % y
#         return x
#
#
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
#
#
# def check():
#     if ebob(a, b) == 1:
#         return True
#     return False
#
#
# print(check())


# # 12
# def checkPrime(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % 1 == 0:
#             return True
#     return False
#
#
# def hyperPrime(x):
#     if checkPrime(x) and checkPrime(x // 10):
#         return "hyper prime"
#     return "not hyper prime"
#
#
# number = int(input("enter a number: "))
# print(hyperPrime(number))

# # 13
# def ebob(x, y):
#     while x != 0:
#         x, y = y, x % y
#         return x
#
#
# def ekob(x, y):
#     ekob = x
#     while x % ekob != 0 and y % ekob != 0:
#         ekob += 1
#     return ekob
#
#
# number1 = int(input("enter a number: "))
# number2 = int(input("enter a number: "))
# print(f"ebob = {ebob(number1, number2)}, ekob = {ekob(number1, number2)}")

# # 14
# def incList(x, y, z):
#     if x > y:
#         if y > z:
#             return z, y, x
#         else:
#             return y, z, x
#     else:
#         if x > z:
#             return z, x, y
#         else:
#             return x, z, y
#
#
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# print(incList(num1, num2, num3))

# # 15
# def ebob(x, y):
#     while x != 0:
#         x, y = y, x % y
#         return x
#
#
# def makePrime(x, y):
#     num = ebob(x, y)
#     return f"{x // num} / {y // num}"
#
#
# top = int(input("enter the top: "))
# bottom = int(input("enter the bottom: "))
# print(makePrime(top, bottom))

# # 16
# def reverse(x):
#     result = 0
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         result = result * 10 + lastNum
#
#
# number = int(input("enter a number to reverse: "))
# print(reverse(number))

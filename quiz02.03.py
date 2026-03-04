# # task1
# def max_collatz(x):
#     compare = 0
#     while x != 1:
#         if x % 2 == 0:
#             x //= 2
#         else:
#             x = 3 * x + 1
#         if compare < x:
#             compare = x
#         print(x, end=" ")
#     return compare
#
#
# number = int(input("Enter a number (N > 0): "))
# print(f"\nMax number: {max_collatz(number)}")

# # task2
# def length_num(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count
#
#
# def is_weightedSym(x):
#     normal = 0
#     normalResult = ""#optional
#     reversed = 0
#     reversedResult = ""#optional
#     len = length_num(x)
#     index = 1
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         normal += len * lastNum
#         normalResult = str(len*lastNum) + " + " + normalResult
#         reversed += index * lastNum
#         reversedResult = str(index * lastNum) + " + " + reversedResult
#         len -= 1
#         index += 1
#     normalResult += "= " + str(normal)
#     reversedResult += "= " + str(reversed)
#     print(normalResult)
#     print(reversedResult)
#     if normal == reversed:
#         return True
#     return False
#
#
# number = int(input("Enter a number (N > 0): "))
# print(is_weightedSym(number))



# # task3
# def length_num(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count
#
#
# def look_and_say(x):
#     len = length_num(x)
#     result = ""
#     if len % 2 == 1:
#         return "invalid"
#     else:
#         while x > 0:
#             num = x % 100
#             first = num // 10
#             last = num % 10
#             result = first * str(last) + result
#             x //= 100
#         return result
#
#
# number = int(input("Enter a number (N > 0): "))
# print(look_and_say(number))

# # task4
# def is_Palindrome(x):
#     usedNum = x
#     reversed = 0
#     while usedNum > 0:
#         lastNum = usedNum % 10
#         usedNum //= 10
#         reversed = reversed * 10 + lastNum
#     if reversed == x:
#         return True
#     return False
#
#
# def to_Binary(x):
#     binary = 0
#     while x > 0:
#         num = x % 2
#         x //= 2
#         binary = binary * 10 + num
#     return binary
#
#
# def Palindrome_type(x):
#     if is_Palindrome(to_Binary(x)):
#         if is_Palindrome(x):
#             return "Palindrome type is Decimal and Binary."
#         else:
#             return "Palindrome type is only Binary."
#     elif is_Palindrome(x):
#         return "Palindrome type is only Decimal."
#     else:
#         return "Palindrome type is neither Decimal nor Binary."
#
#
# number = int(input("Enter a number (N > 0): "))
# print(Palindrome_type(number))

# # task5
# def length_num(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count
#
#
# def np_to_k(n, p):
#     len = length_num(n) - 1
#     sum = 0
#     usedNum = n
#     while usedNum > 0:
#         lastNum = usedNum % 10
#         usedNum //= 10
#         sum += lastNum ** (p + len)
#         len -= 1
#     if sum % n == 0:
#         return sum // n
#     return None
#
#
# number = int(input("Enter N: "))
# pos = int(input("Enter P: "))
# print(f"K: {np_to_k(number, pos)}")


# #task2(Old)
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
#         print(f"{num} % {division} = {num % division}")
#         if num % division != 0:
#             lamp = 1
#         len -= 1
#         division += 1
#     if lamp == 0:
#         return True
#     return False
#
#
# number = int(input("Enter a number (N > 0): "))
# print(ifPolydivisible(number, lengthNum(number)))

##task1
# def is_perfect_number(x):
#     sum = 0
#     for i in range(1, x):
#         if x % i == 0:
#             sum += i
#     if sum == x:
#         return True
#     return False
#
#
# start = int(input("Enter a start number: "))
# end = int(input("Enter an end number: "))
# for number in range(start, end + 1):
#     if is_perfect_number(number):
#         print(number)

##tas2
# def sum_digits(x):
#     sum = 0
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         sum += lastNum
#     return sum
#
#
# def harshad_chain(x):
#     index = 1
#     while x / sum_digits(x) != 1:
#         division = x % sum_digits(x)
#         if division == 0:
#             print(f'Step {index} : {x} / {sum_digits(x)} = {x / sum_digits(x)}')
#         else:
#             return 0
#         x = x / sum_digits(x)
#         index += 1
#     print(f"Total chain length: {index}")
#
#
# number = int(input("Enter a number (N > 0): "))
# harshad_chain(number)

##task3
# def max_digit(x):
#     number = 0
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         if number < lastNum:
#             number = lastNum
#     return number
#
#
# def count_binary_ones(x):
#     count = 0
#     while x > 0:
#         binaryNum = x % 2
#         x //= 2
#         if binaryNum == 1:
#             count += 1
#     return count
#
#
# def is_dominant_trip(x):
#     if max_digit(x) == count_binary_ones(x):
#         return True
#     return False
#
#
# number = int(input("Enter a number: "))
# print(f"max digit: {max_digit(number)}")
# print(f"max digit: {count_binary_ones(number)}")
# if is_dominant_trip(number):
#     print("Result: True. It is a Dominant Trip number.")
# else:
#     print("Result: False. It is not a Dominant Trip number.")


# #task4
# def is_prime(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     if x == 1:
#         return False
#     return True
#
#
# def is_perfect_number(x):
#     sum = 0
#     for i in range(1, x):
#         if x % i == 0:
#             sum += i
#     if sum == x:
#         return True
#     return False
#
#
# def rotate_number(x):
#     firstNum = 0
#     count = 0
#     while firstNum > 9:
#         firstNum //= 10
#         count += 1
#     return (x % 10 ** count) * 10 + firstNum
#
#
# def binary_weight_type(x):
#     count = 0
#     while x > 0:
#         binaryNum = x % 2
#         x //= 2
#         if binaryNum == 1:
#             count += 1
#     return count
#
#
# def analyze_complex_number(x):
#     print(f"Original: {x}")
#     print(f"Rotated: {rotate_number(x)}")
#     print(f"Binary weight type: {binary_weight_type(x)}")
#     if is_prime(x) and is_prime(rotate_number(x)):
#         print("Result: Category A")
#     elif is_prime(x) == False and binary_weight_type(x) == 2:
#         print("Result: Category B")
#     elif is_perfect_number(x):
#         print("Result: Category C")
#     else:
#         print(None)
#
#
# number = int(input("Enter a number (N>0): "))
# print(analyze_complex_number(number))


# # task5
# def factorial(x):
#     result = 1
#     for i in range(1, x + 1):
#         result *= i
#     return result
#
#
# def get_factorial_sum(x):
#     sum = 0
#     while x > 0:
#         lastNum = x % 10
#         x //= 10
#         sum += factorial(lastNum)
#     return sum
#
#
# def is_happy(x):
#     sum = 0
#     while sum != 1 and sum != 4:
#         while x > 0:
#             lastNum = x % 10
#             x //= 10
#             sum += lastNum ** 2
#         x = sum
#     if sum == 1:
#         return True
#     return False
#
#
# number = int(input("Enter a number: "))
# print(f"Faktorial cemi: {get_factorial_sum(number)}")
# print(f"is happy? {is_happy(number)}")

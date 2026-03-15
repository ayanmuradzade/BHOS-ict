#task1
x = float(input("x: "))
y = float(input("y: "))
if y > 0.5 and y > 6*x**2 and y > abs(2*x):
    print("in range")
else:
    print("not in range")


#task2
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    if x == 1:
        return False
    return True
sum = 0
while True:
    number = int(input("Enter a number: "))
    if is_prime(number):
        sum += number
    else:
        print(sum)
        break

#task3
def sum_digits(x):
    sum = 0
    while x>0:
        lastNum = x% 10
        x//=10
        sum += lastNum
    return sum
number = int(input("Enter a number: "))
while number > 9:
    number = sum_digits(number)
print(number)


#task4
def binary_weight_type(x):
    count = 0
    while x > 0:
        binaryNum = x % 2
        x //= 2
        if binaryNum == 1:
            count += 1
    return count
number = int(input("Enter a number: "))
if binary_weight_type(number) == number%10:
    print(True)
else:
    print("False")



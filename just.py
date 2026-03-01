def ebobFind(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


print("you will be asked to enter 10 numbers!")
number1 = int(input("enter a number: "))
compare = 1
for i in range(9):
    number2 = int(input("enter a number: "))
    ebob = ebobFind(number1, number2)
    if ebob > compare:
        compare = ebob
    number1 = number2
print(compare)

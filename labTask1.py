# #task1
# #sadece bu taskda basqa sey daxil etse meselesini nezere almamisam(bacarmadim sadece if else ile)
# letter = input("Enter a letter of the alphabet: ")
# letter = letter.lower()
# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#     print("Entered alphabet is a vowel!")
# elif letter == "y":
#     print("Sometimes it is a vowel, and sometimes it is a constant!")
# else:
#     print("Entered alphabet is a constant!")

# #task2
# try:
#     monthOrg = input("Enter name of the month: ")
#     day = int(input("Enter the day: "))
#     month = monthOrg.lower()
#     result = ""
#     lamp = 0
#     if month == "march":
#         if 0 < day < 20:
#             result = "Winter"
#         elif 20 <= day <= 31:
#             result = "Spring"
#     elif month == "june":
#         if 0 < day < 21:
#             result = "Spring"
#         elif 21 <= day <= 30:
#             result = "Summer"
#     elif month == "september":
#         if 0 < day < 22:
#             result = "Summer"
#         elif 22 <= day <= 30:
#             result = "Fall"
#     elif month == "december":
#         if 0 < day < 21:
#             result = "Fall"
#         elif 21 <= day <= 31:
#             result = "Winter"
#     elif month == "january" and 0 < day <= 31:
#         result = "Winter"
#     elif month == "february" and 0 < day <= 29:
#         result = "Winter"
#     elif month == "april" and 0 < day <= 30:
#         result = "Spring"
#     elif month == "may" and 0 < day <= 31:
#         result = "Spring"
#     elif month == "july" and 0 < day <= 31:
#         result = "Summer"
#     elif month == "august" and 0 < day <= 31:
#         result = "Summer"
#     elif month == "october" and 0 < day <= 31:
#         result = "Fall"
#     elif month == "november" and 0 < day <= 30:
#         result = "Fall"
#     else:
#         print("Write correct day or month!")
#         lamp = 1
#     if result != "":
#         print(monthOrg, day, "is", result)
#     elif lamp == 0:
#         print("Write correct day or month!")
# except:
#     print("Write a number as a day!")


# #task3
# try:
#     wavelength = int(input("Enter the wavelength in nm: "))
#     if 380 <= wavelength < 450:
#         print("Violet")
#     elif 450 <= wavelength < 495:
#         print("Blue")
#     elif 495 <= wavelength < 570:
#         print("Green")
#     elif 570 <= wavelength < 590:
#         print("Yellow")
#     elif 590 <= wavelength < 620:
#         print("Orange")
#     elif 620 <= wavelength < 750:
#         print("Red")
#     else:
#         print("Invalid input!")
# except:
#     print("Input a number as wavelength!")

# #task4
# try:
#     year = int(input("Enter the year: "))
#     difference = year - 2000
#     #asagidaki if-li hisse 2000den evvelki iller duz olsun deye var)
#     if difference < 0:
#         difference = 12 - abs(difference) % 12
#     remain = difference % 12
#     result = ""
#     if year > 0:
#         if remain == 0:
#             result = "Dragon"
#         elif remain == 1:
#             result = "Snake"
#         elif remain == 2:
#             result = "Horse"
#         elif remain == 3:
#             result = "Sheep"
#         elif remain == 4:
#             result = "Monkey"
#         elif remain == 5:
#             result = "Rooster"
#         elif remain == 6:
#             result = "Dog"
#         elif remain == 7:
#             result = "Pig"
#         elif remain == 8:
#             result = "Rat"
#         elif remain == 9:
#             result = "Ox"
#         elif remain == 10:
#             result = "Tiger"
#         else:
#             result = "Hare"
#         print(year, "is the year of the", result)
#     else:
#         print("Invalid year!")
# except:
#     print("Enter a number as a year!")

# #task5
# try:
#     monthOrg = input("Enter name of the month: ")
#     day = int(input("Enter the day: "))
#     month = monthOrg.lower()
#     result = ""
#     lamp = 0
#     if month == "march":
#         if 0 < day < 21:
#             result = "Pisces"
#         elif 21 <= day <= 31:
#             result = "Aries"
#     elif month == "april":
#         if 0 < day < 20:
#             result = "Aries"
#         elif 20 <= day <= 30:
#             result = "Taurus"
#     elif month == "may":
#         if 0 < day < 21:
#             result = "Taurus"
#         elif 21 <= day <= 31:
#             result = "Gemini"
#     elif month == "june":
#         if 0 < day < 21:
#             result = "Gemini"
#         elif 21 <= day <= 30:
#             result = "Cancer"
#     elif month == "july":
#         if 0 < day < 23:
#             result = "Cancer"
#         elif 23 <= day <= 31:
#             result = "Leo"
#     elif month == "august":
#         if 0 < day < 23:
#             result = "Leo"
#         elif 23 <= day <= 31:
#             result = "Virgo"
#     elif month == "september":
#         if 0 < day < 23:
#             result = "Virgo"
#         elif 23 <= day <= 30:
#             result = "Libra"
#     elif month == "october":
#         if 0 < day < 23:
#             result = "Libra"
#         elif 23 <= day <= 31:
#             result = "Scorpio"
#     elif month == "november":
#         if 0 < day < 22:
#             result = "Scorpio"
#         elif 22 <= day <= 30:
#             result = "Sagittarius"
#     elif month == "december":
#         if 0 < day < 22:
#             result = "Sagittarius"
#         elif 22 <= day <= 31:
#             result = "Capricorn"
#     elif month == "january":
#         if 0 < day < 21:
#             result = "Capricorn"
#         elif 21 <= day <= 31:
#             result = "Aquarius"
#     elif month == "february":
#         if 0 < day < 19:
#             result = "Aquarius"
#         elif 19 <= day <= 29:
#             result = "Pisces"
#     else:
#         print("Write correct day or month!")
#         lamp = 1
#     if result != "":
#         print("Your zodiac sign is", result)
#     elif lamp == 0:
#         print("Write correct day or month!")
# except:
#     print("Write a number as a day!")

# #task6
# try:
#     x = float(input("x: "))
#     y = float(input("y: "))
#     if x**2 + y**2 >= 4 and x <= 2 and y <= x and y >= 0:
#         print("The point is in the shaded area")
#     else:
#         print("The point is not in the shaded area")
# except:
#     print("Write a number!")

# #task7
# #bu sualin numunesinde sehv var mence > abs(y) x-dan boyuk olmalidir ki shaded area-ya dussun
# try:
#     x = float(input("x: "))
#     y = float(input("y: "))
#     if y >= (x-2)**2 - 3 and x <= abs(y):
#         print("The point is in the shaded area")
#     else:
#         print("The point is not in the shaded area")
# except:
#     print("Write a number!")

# #task8
# try:
#     x = float(input("x: "))
#     y = float(input("y: "))
#     if 0 < y <= x**2 and y >= 2 - x:
#         print("The point is in the shaded area")
#     else:
#         print("The point is not in the shaded area")
# except:
#     print("Write a number!")

# #task9
# try:
#     x = float(input("x: "))
#     y = float(input("y: "))
#     if x**2 + y**2 <= 1:
#         if (y >= -1*x and y >= x) or (y >= -1*x and y <= 0):
#             print("The point is in the shaded area")
#         elif y <= -1*x and y >= x and y <= 0:
#             print("The point is in the shaded area")
#         else:
#             print("The point is not in the shaded area")
#     else:
#         if y <= -1*x and y <= x:
#             print("The point is in the shaded area")
#         else:
#             print("The point is not in the shaded area")
# except:
#     print("Write a number!")

# #task10
# try:
#     x = float(input("x: "))
#     y = float(input("y: "))
#     if y >= x**2:
#         if x > 0 and y >= 4 - x**2:
#             print("The point is in the shaded area")
#         elif x < 0 and y <= 2 - x and y <= 4 - x**2:
#             print("The point is in the shaded area")
#         else:
#             print("The point is not in the shaded area")
#     else:
#         if y >= 0 and y <= 2 - x:
#             print("The point is in the shaded area")
#         elif y >= 2 - x:
#             print("The point is in the shaded area")
#         else:
#             print("The point is not in the shaded area")
# except:
#     print("Write a number!")

# #1.1
# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number == 0:
#     print("The number is zero.")
# else :
#     print("The number is negative.")

# #2.1
# choice = input("Do you choose the path to the left or right? ")

# if choice == "left":
#     print("You find a treasure chest!")
# elif choice == "right":
#     print("You encounter a dragon!")
# else:
#     print("Invalid choice!")
    
# #3.1
# num_1 = int(input("Enter number 1: "))
# num_2 = int(input("Enter number 2: "))
# num_3 = int(input("Enter number 3: "))

# max = 0

# if (num_1 >= num_2) and (num_1 >= num_3):
#     max = num_1
# elif (num_2 >= num_1) and (num_2 >= num_3):
#     max = num_2
# else:
#     max = num_3
    
# print("Largest number is: " + str(max)) #making the num a string to print
    
# #3.2 - would continue from the if statement above
# min = 0
# if (num_1 <= num_2) and (num_1 <= num_3):
#     min = num_1
# elif (num_2 <= num_1) and (num_2 <= num_3):
#     min = num_2
# else:
#     min = num_3
    
# print("Smallest number is: " + str(min)) #making the num a string to print

# #3.3 - would continue and include the if statements above

# if (num_1 == num_2) and (num_1 == num_3):
#     print("All numbers are equal")
# elif (num_2 == num_1) or (num_2 == num_3) or (num_1 == num_3):
#     print("Two numbers are equal and the largest is " + str(max))  
# else:
#     print("All numbers are different")
    
# #4.1

year = int(input("Enter a year: "))

if (year % 4 == 0):
    print("This is a leap year")
else:
    print("This is NOT a leap year")
    
#4.2

if(year % 100 == 0):
    print("This is a century year")
else:
    print("This is NOT a century year")   
    
#4.3

import datetime

current_date = datetime.datetime.now()
current_yr = int(current_date.strftime("%Y"))

if(year == current_yr):
    print("You inputted the current year")
elif(year < current_yr):
    print("You inputted a past year")
else:
    print("you inputted a future year")
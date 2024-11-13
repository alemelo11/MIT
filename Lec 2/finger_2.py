# Assume you are given a variable named number (has a numerical value).
# Write a piece of Python code that prints out one of the following strings: 
# num = int(input("enter a number: "))
# if num == 0:
#     print("zero")
# elif num > 0:
#     print("positive")
# else:
#     print("negative")
#######################################################################################

# Finger exercise: Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered. If
# no odd number was entered, it should print a message to that effect.
num_user = []
for i in range(10):
    num = int(input("enter a number: "))
    num_user.append(num)
max_odd = 0
for num in num_user:
    if num % 2 == 1 and num > max_odd:
        max_odd = num
if max_odd == 0:
    print("no odd number was entered")
else:
    print(max_odd)
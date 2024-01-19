'''Q1-Declare two variables, num1 and num2, with any integer values. Use these to calculate their sum and print the result. Understand how variables store numerical values and perform basic arithmetic in Python.'''

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
sum_result = num1 + num2
print("Sum of", num1, "and", num2, "is:", sum_result)

'''Q2-Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message. Explore basic string operations in Python.'''

message1 = input("Message: ")
message2 = input("Message: ")
message=message1+message2
print(message)

'''Q3-Declare a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. Learn to use boolean variables for decision-making in Python.'''

is_python_fun = True
if is_python_fun:
    print("Python is fun!")
else:
    print("Python is not fun.")

'''Create a list called fruits with at least three different fruit names. Print the list, add a new fruit, and then print the updated list. Understand the basics of working with lists in Python.'''

fruits = ['apple', 'banana', 'orange']
print("Fruits:", fruits)
fruits.append('grape')
print("Updated Fruits:", fruits)

'''Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values. Explore how to convert between different data types in Python.'''

price = 9.99
int_price = int(price)
print("Original Price:", price)
print("Converted Price:", int_price)

'''Create a dictionary named student_info with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary. Learn how to work with dictionaries, a versatile data structure in Python'''

student_info = {'name': 'John', 'age': 20, 'grade': 'A'}
print("Student Information:", student_info)

'''Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult"). Explore user interaction and conditional statements in Python.'''

user_age = int(input("Enter your age: "))
if user_age < 13:
    print("Child")
elif 13 <= user_age < 20:
    print("Teenager")
else:
    print("Adult")

'''Create a complex number variable, comp_num, with real and imaginary parts. Print both parts separately. Understand the representation of complex numbers in Python.'''

comp_num = 3 + 4j
print("Real Part:", comp_num.real)
print("Imaginary Part:", comp_num.imag)

'''Combine two strings using concatenation. Use string interpolation to include the length of the resulting string in a print statement. Explore different ways to manipulate strings in Python.'''

string1 = "Hello"
string2 = " World!"
combined_string = string1 + string2
print(f"Combined String: {combined_string}, Length: {len(combined_string)}")

'''Create a tuple named days_of_week with the names of the days. Access and print the third day of the week. Understand the basics of working with tuples in Python.'''

days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
third_day = days_of_week[2]
print("Third Day of the Week:", third_day)




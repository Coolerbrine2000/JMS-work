#                                    Sequences
Number1 = int(input("Enter your first number: "))
Number2 = int(input("Enter your second number: "))
Total_sum = Number1+Number2

print("your first number is " +str(Number1))
print("your second number is " +str(Number2))

print("The total sum of the two numbers is: " +str(Total_sum))
#                                     Selection
a = 200
b = 33

if b>a:
    print(" b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
#                                           Functions
def greet():
    print("Hello")

# call function
greet()

# Data Structures
P = {}  # Dictionaries - any data type, used to relate data
M = []  # Lists - any data type, used to store multiple inputs and data in one data structure - Variable
R = ()  # Tuples - any data type, used to store multiple inputs and data in one data structure - Fixed
print(type(P))
print(type(M))
print(type(R))

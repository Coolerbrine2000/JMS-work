# Q1
x = 5j
y = 3.542
v = "Monday"
z = 140

print(type(x))
print(type(y))
print(type(v))
print(type(z))
# End of 1

# Q2
print("Fruit list")
F1 = input("Please input Fruit NO.1: ")
F2 = input("Please input Fruit NO.2: ")
F3 = input("Please input Fruit NO.3: ")
F4 = input("Please input Fruit NO.4: ")
F5 = input("Please input Fruit NO.5: ")

print(
    "Your list of fruits: ",
    F1,
    F2,
    F3,
    F4,
    F5
)
# End of Q3

# Q3
Count = 5
while Count != 0:
    print(Count)
    Count-=1
print("this is pre-conditional loop")

print(Count)
if Count<5:
    print("Count is less than 5")
elif Count>5:
    print("Count is greater than 5")
print("this contains post-conditional processing")
# End of Q3

# Q4
# a)
print("Whole Number returner")
Num1 = float(input("Input number 1:"))
Num2 = float(input("Input number 2:"))
Answer = Num1%Num2
Answer2 = (Num1//Num2)
print("The whole number answer is: ",Answer2)
print("The remainder of the equations is: ",Answer)
# End of Q4

# Q5
print("Number Comparison")
Num1 = float(input("Please input number 1: "))
Num2 = float(input("Please input number 2: "))
if Num1>Num2:
    print(Num1, "iS greater than", Num2)
elif Num1==Num2:
    print(Num1, "is equal to", Num2)
elif Num1<Num2:
    print(Num1,"is smaller than", Num2)
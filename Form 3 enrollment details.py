#Progeram which captures enrollment details

import time
import sys
from time import sleep

# Variable initialization
F_name = str
L_name = str
age = int
Date_of_Birth = str
Guardian = str
City = str
No_subjects = int
Boarding = bool
Phone_no = int
Height = str
boardings = str
words = str

print("Good morning.")
print("welcome to the form 3 application program. ")
print("Please fill in all the information we ask for.")
F_name = input("Please type your your first name: ")
L_name = input("Please type your your last name: ")
age = input("Please type age: ")
Height = input("Please input your height: ")
Date_of_Birth = input("Please input your date of birth in the format DD/MM/YYYY: ")
City = input("Please state the city you live in: ")
No_subjects = input("How many subjects will you be doing?: ")
Boarding = input("Will you be boarding? Y/N: ")
Guardian = input("Are you under a guardian? Y/N: ")
Phone_no = input("Please input your phone number: ")

#Code for checking boarding status
if Boarding=="Y":
    boardings = "have"
else:
    boardings = "haven't"

time.sleep(0.7)
print(".")
time.sleep(0.7)
print("..")
time.sleep(0.7)
print("...")
time.sleep(1.5)

#letter of acceptance
words = "Dear prospective student: ", F_name, "\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words = "Your application has been accepted here at this school.\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words = "let us just confirm your information:\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words = "you have chosen to do ", No_subjects, " subjects here.\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words = "age: ", age, "\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words ="You ", boardings, " chosen to board\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words ="you have registered your location as ", City, ". Your phone number was input as: ", Phone_no, "\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)

words ="Congratulations on your acceptance into this prestigious position.\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)




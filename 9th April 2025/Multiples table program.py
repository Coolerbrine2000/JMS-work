# Multiple tables
Two_table = [2,4,6,8,10,12,14,16,18,20]
Seven_table = [7,14,21,28,35,42,49,56,63,70]
Eleven_table = [11,22,33,44,55,66,77,88,99,110]

No = int(input("Please input the number of multiples of 2 you want: "))
Counter = 0
while int(Counter) != No:
    print(Two_table[Counter])
    Counter += 1

No = int(input("Please input the number of multiples of 7 you want: "))
Counter = 0
while int(Counter) != No:
    print(Seven_table[Counter])
    Counter += 1

No = int(input("Please input the number of multiples of 11 you want: "))
Counter = 0
while int(Counter) != No:
    print(Eleven_table[Counter])
    Counter += 1
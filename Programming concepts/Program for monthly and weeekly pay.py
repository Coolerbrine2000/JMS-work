#                                         Task 1 (a) - Weekly & Monthly pay.

print("Hello \nWelcome to the payment allocator program. \nWe're gonna ask a few questions.")
Name = input("Please enter your full name: ")
Job_T = input("Enter either: Full time, Part time: ")
Hours = int(input("How many hours do you work a week: "))
Pay_h = 6
Pay_w = int(Hours*Pay_h)
Pay_m = int(Pay_w*4)
print("Your name is", Name, ".")
print("You are a", Job_T, "employee")
print("You have  ", Hours, "hours this week.\nYour pay per hour:", Pay_h)
print("YOur weekly pay is: ", Pay_w)
print("Your monthly pay is: ", Pay_m)

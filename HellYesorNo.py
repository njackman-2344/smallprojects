print("Hell Yes or Hell No")
print("Having an issue deciding?")

n = int(input('How many choices (2-4): '))

first = str(input("First choice?: "))
sec = str(input("Second choice?: "))
third = str(input("Third choice?: "))
four = str(input("Fourth?: "))
if (n ==1 or n < 1):
    print("Need some more")
elif (n == 2):
    first and sec and print("Now think about it.")
elif (n == 3):
    first and sec and third and print("Now think about it.")
elif (n == 4):
    first and sec and third and four and print("Now think about it.")
else:
    print("Holdup...Do it again")

print(first)
print(sec)
print(third)
print(four)
print("Which one of these is a Hell Yeah?! ;)")
    


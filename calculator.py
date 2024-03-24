import sys
print('''
Select the operation:
        1.Add
        2.Sub
        3.Multiply
''')
choice = int(input("Select the operation 1,2 or 3: "))
if choice not in  (1,2,3):
    print("Invalid input")
    SystemExit
a = int(input("Enter the number"))
b = int(input("Enter the number"))
if choice ==1:
    res = print(a+b)
elif choice == 2:
    res = print(a-b)
else:
    res = print(a*b)
res = print("result is: ",res)
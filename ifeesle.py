a = int(input("Enter the 1 number: "))
b = int(input("Enter the 2 number: "))

if a<0:
    print("Negative ",end="")
    if a%2==0:
     print("Even")
    else:
     print("Odd")
    
elif a>0:
    print("Positive ",end="")
    if a%2==0:
     print("Even")
    else:
     print("Odd")
    
else:
    print("Zero")

if a>b:
  print("a is greater")
elif b>a:
    print("b is greater")
else:
  print("a and b are same")
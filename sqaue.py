n = int(input("Enter the number of sqaures: "))
for x in range(n):
    for y in range(n):
        print("*",end=" ")
    print()
#pattern
for x in range(n):
    for y in range(x+1):
        print("x",end=" ")
    print()
#inverted *
for x in range(n):
    for y in range(n-x):
        print("*",end=" ")
    print()
#pyramid pattern
for x in range(n):
    for y in range(n-x-1):
        print(" ",end="")
    for z in range(2*x+1):
        print("*",end="")
    print()

for x in range(n):
    if x==0:
        print("* "*n)
    elif x==n-1:
        print("* "*n)
    else:
        print("* "+"  "*(n-2)+"*")

for x in range(n):
    if x ==0:
        print("*")
    elif x == n-1:
        print("* "*n)
    else:
        print("*"+' '*(x)+"*")


    
n = int(input("Enter the number: "))

if n <=1:
    print(n)
a = 0
b = 1
for i in range(2,n+1):
    c = a+b
    a,b=b,c

print(b)


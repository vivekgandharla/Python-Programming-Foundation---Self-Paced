a =int(input("Enter the number: "))
b = int(input("Enter the number: "))

small = min(a,b)
for x in range(1,small+1):
    if (a%x==0 and b%x==0):
        gcd = x
print(gcd)
#any number which divides both a and b 

a = int(input("Enter the number : "))
b = int(input("Enter  the number : "))
res = max(a,b)
# least common mutiple
while res<=a*b:
    if(res%a==0 and res%b==0):
        break
    res+=1
print(res)

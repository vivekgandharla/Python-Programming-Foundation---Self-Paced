def nFactorial(n):
    
    ans = 1
    
    for i in range(1,n+1):
        ans= ans *i
        print(ans)
    
    #Write your code below
    
    
n = int(input("enter the number: "))
    
nFactorial(n)
# n = int(input("Enter the number: "))

# for x in range(1,n+1):
#     if n%x==0:
#         print(x)

var = 10
for i in range(10):
    for j in range(2,10,1):
        if var%2==0:
            continue
            var+=1
            var+=1
        else:
            var+1
    print(var)
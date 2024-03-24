x = int(input("Enter the number: "))

res = 0
while x>0:
    x = x//10
    res += 1
print(res)
l = [10,16,17,18,19,15]
for x in l:
    if x%5==0:
        continue
    print(x)

for i in range(1,1*10+1,1):
    print(i,end=" ")
print()
for i in range(2,2*10+1,2):
    print(i,end=" ")
print()
for i in range(3,3*10+1,3):
    print(i,end=" ")
print()

for i in range(1,10+1):
    for j in range(i,i*11,i):
        print(j,end=" ")
    print()
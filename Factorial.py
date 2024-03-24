n = int(input("Enter the number: "))
res = 1
# while n>0:
#   res = res*n
#   n = n-1
# print(res)
# 1*4=4,4*3=12,12*2=24,24*1=24

for x in range(2,n+1):
  res = res*x
print(res)
# 1*2=2,2*3=6,2*6*4=24


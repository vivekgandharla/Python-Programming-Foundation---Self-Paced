a = 10
b = 20 
c = -30

# if(a>=10 and b < 40):
#     print("the values are greater")
# elif(b<a and a>c):
#     print("not valid ")
# else:
#     print("nil")

# if not a < b:
#     print("not operator")

list = [1,2,3,4,5]
list1 = [6,7,8,9]

for item in list:
    if item in list1:
        print("not overlapping")
    else:
        print("Overlapping")
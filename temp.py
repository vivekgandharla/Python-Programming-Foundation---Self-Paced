# #if_else
# if(10>5):
#     print("ture")
# print("end")

# age = int(input("Enter your age :"))
# if(age<=17):
#     print("not eligible")
# else:
#     print('eligible')

# #nested if example
# age = int(input("Enter your age :"))
# if(age<=13):
#     print("kid")
#     if(age>=14 & age<=18):
#         print("teenage")
#         if(age>=18):
#             print("adult")
#         else:
#             print("buddha")


# a = 1
# b = 2

# a,b = b,a      
# # temp = a
# # a = b
# # b = temp
        
# print(a,b)
# n = int(input("Enter the number"))
# while n!=0:
#     r = n % 10
#     print(r,end='')
#     n = n // 10
    
def multiply(num):
    num = int(input("Enter your number"))
    for i in range(1,11):
         print(num, 'x',i,'=',num*i)
multiply(num='')
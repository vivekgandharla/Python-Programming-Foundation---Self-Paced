# print("hey")
# print("below are the details\n 1.viv\n 2.shiv")
# print("learning python",end='')
# print("FROM GFG")

# val = input("enter your goodname\n")
# print(val)

# val2 = input("enter your age\n")
# print(val2)
# #typecast in str->int
# #typecast in int->str

# typec = (int(val2))
# print(val2)

# typeci = (str(val))
# print(type(typeci))
# # print(type(typec))

# n = int(input("Enter the size of the list : \n"))
# print(n)
# lst = list(map(int, input(
#     "Enter the integer elements of the list : ").split()
# ))[:n]
# print("the list is : ",lst)

#EG 1

#create a list.tuple,dict
a = ("hello","this is ","Vivek")
b = ["hello","this is ","Vivek"]
c = {"hello":1,"this is ":2,"Vivek":3} #dict uses key value pair otherwise its a set
print(type(a))
print(type(b))
print(type(c))

#EG 2

print(type({}) is dict)
print(type(()) is tuple)
print(type([]) is list)

#type_conversion
'''
    2 types:
        1.implicit 
        2.explicit
'''
x = 10
print("the type of ",type(x))


y = 10.22
print("the type of ",type(y))

z = x+y
print(type(z))

s = "10010"
print(type(s))

#int base2 converts ant datatype into int 
va1 = int(s,2)
print(type(va1))
#float

va2 = float(s)
print(va2,type(va2))

#ord(): char into int
a = '3'
print(type(a))
va3 = ord(a)
print(va3,type(va3))

#hex(): int to hexadecimal

a1 = 22
va4 = hex(a1)
print(va4,type(va4))

#oct(): int to  octadecimal 
va5 = oct(a1)
print(va5,type(va5))

# tuple, set and list 
name = "vivek"
va6 = tuple(name)
print("converting str to a tuple",va6)

va7 = set(name)
print("converting str to a set",va7)

va8 = list(name)
print("converting str to a list",va8)

#Dict,str,complex
a = 3
b = 2

tup = ('a',1),('b',2),('c',3)

#complex
va9 = complex(1,2)
print(type(va9),va9)

#str
va9 = str(a)
print(type(va9),va9)

#chr(number)->converts number to ASCII
va9 = chr(a)
print(type(va9),va9)

#Dict()
va9 = dict(tup)
print(type(va9),va9)
#[int(base,2),ord,int,float,complex,set,list,dict,hex,oct,str,chr]

#if,else & elif

if(a>b):
    print("true")
elif(a==b):
     print("barabar h")
else:
     print("b bada h ")
print("end")

#nested if :
name = input("name likho")
if name == "vivek":
     print('naam sahi h')
else:
     if name == 'pompom':
          print('gandu h kya ye koi naam h')
     else:
          print('kch sahi to likh le bhai')

#EG 1 
#let's see if you can vote
age = input("Enter your age")
if(age < 18):
     print("you're a teenager so can't vote")
elif age > 18:
     print("you're eligible to vote")
elif age > 80:
     print("dude can you even walk")
elif age>13 and age<18:
     print("abhi baccha h tu bada hoja")
else:
     print("")

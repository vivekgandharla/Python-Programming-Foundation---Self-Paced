def add():
    print("hey")
add()

def evedOdd(x):
    if x %2==0:
        print("Even")
    else:
        print("Odd")
evedOdd(5)
# Default Argument
def func(x,y=5):
    print("x: ",x)
    print("y: ",y)
func(4)
# Keywords args;

def name(firstname,lastname):
    print(firstname,lastname)
name(firstname='vivek',lastname='Gandharla')
name(lastname='vivek',firstname='Gandharla')

# variable len args:

def myFun(*args):
    for arg in args:
    
        print(arg)
myFun('hello','viv','here')

def myFunn(x):
    x[1] = 20
lst = [1,2,34,5,6,0]
myFunn(lst)

print(lst)

# pass by ref and val;
def myfunc(x , arr):
    print("Inside Funtion")
    x +=10
    print("value recieved",x,"id",id(x))

    arr[0] = 0
    print("List recieved",arr,"Id",id(arr))
x = 10
arr = [1,2,3,4]

print("Before calling function")
print("value passed",x,"Id",id(x))
print("Array passed",arr,"Id",id(arr))
print()

myfunc(x,arr)
print("after calling function")
print("value passed",x,"Id",id(x))
print("Array passed",arr,"Id",id(arr))


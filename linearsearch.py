# arr = eval(input("\nEnter array element: "))
# key = int(input("\n Enter an elemnet to be search: "))
# for i in range(len(arr)):
#     if key == arr[i]:
#         print(f"Element {key} is found at position {i}")
#         break
#     else:
#         print("\nElement not found")


#--------------------------------
# prog2
# insrt elem to sorted list
# lst = list(map(int, input("Enter the sorted list separated by spaces: ").split()))
# x = int(input("Enter an element to be inserted: "))

# for i in range(len(lst)):
#     if x < lst[i]:
#         lst.insert(i, x)
#         break
# else:
#     lst.append(x)

# print(lst)
# ------------------------------
# prog3
class A:
    z = 20
    def __init__(self,x) -> None:
        self._x= x
class B(A):
    def __init__(self, y) -> None:
             self._y = y
    def __add__(self,other):
        x = self._y+other._x
        return B(x)
    def __str__(self) -> str:
        return "({0},{1})".format(self._y,self.z)
    
obj1 = A(7)
obj2 = B(5)
print(obj2+obj1)




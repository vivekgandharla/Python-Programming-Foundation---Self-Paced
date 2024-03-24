# a = 5
# print("type of a : ",type(a))

# b = 5.0
# print("\nType of b : ",type(b))

# c = 2+4j
# print("\ntype of c : ",type(c))

# string1 = '''
# name 
# address 
# number
# '''

# print(string1)
# #a = input("fill the details: NAME: ")

string2 = "vivekGandharla"
#first character
print(string2[-3])
#LIST
list = []
print(list,type(list))

list1 = ['VivekGandharla']
print(list1,type(list1))

list2 = ['viv',9,44.3,'22','g']
print(list2[-2],type(list2[-3]))

#multi-dimentional-list
list3 = [['VivekGandharla'],['MCA'],['AMC']]
print(len(list3))

#tuple
tuple1 = ()
print("\nCreating empty tuple")
print(tuple1)

tuple2 = ("VivekGandharla")
print("\nCreating tuple containig str")
print(tuple2)

list4 = [1,2,2,3,4,5,6]

tuple3 = tuple(list4)
print("\nCreating tuple using list")
print(tuple3)

tuple4a = (tuple("viv"))
print(tuple4a)

tup1 = (9,4,7,9,0,6,8)

tup2 = ('viv','Gandharla')

tup3 = (tup1,tup2)
print(tup3[1])

print(type(True))

#SETS


set1 = set() 
print(type(set1))

set2 = set("VivekGandharla")
print(type(set2))

set3 = set([1,1,1,2,3,4,5,])
print(set3)

set4 = set(['viv',3,33.3,'g'])
print(set4)

#accessing sets

for i in set4:
    print(i,end="")
if "viv" in set4:
    print("ys")

#Dictionary
    
Dict = {}
print(type(Dict))

Dict1 = {'viv':1,'div': 2, 'mom': 3}
print(type(Dict1))
print(Dict1['viv'])

Dict2 = dict({1:'abc',2:'xyz'})
print(Dict2)

Dict3 = dict([(1, 'viv'),(2,'g')])
print(Dict3)

print(Dict3.get(1))
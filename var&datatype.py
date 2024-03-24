#how to define or declare a variable 
varname = "vivek"
varnum = 11
varfloat = 33.33
print(varfloat,varname,varnum)
#declaring and re-declaring 

Number = 100
print("initial number is : ",Number)
Number = 122
print("final number is : ",Number)

a = b = c = 10
print(a,b,c)

a,b,c = 10,'gfg',22.2
print(a,b,c)

#let's create different methonds of string 
string1 = "hii this is just a practise\n"
print("this is double quoted string declaration: \n",string1)

string1 = 'hii this is just a practise\n'
print("this is single quoted string declaration: \n",string1)

string1 = '''hii this is just a practise\n'''
print("this is triple quoted string declaration: \n",string1)

print(string1[2])
print(string1[-2])

#we'll see creation of list
List1 =  []
print(type(List1))
print("this is a empty list: ")

List1 = ['vivek']
print(type(List1))
print("single lined list")

List1 = ['hey','this','is','viv']
print(type(List1))
print("multivalued str")

List1 = [['multi','dimentional'],['list']]
print(List1[0])

#Tuple
Tuple1 = ()
print(Tuple1)
print(type(Tuple1))

Tuple1 = ('viv','here')
print(Tuple1)
print(type(Tuple1))

List1 = ['2','3','4','6']
print(len(List1))
Tuple1 = tuple(List1)
print(type(Tuple1))

Tuple1 = tuple('this is a tuple')
print(type(Tuple1))
print(Tuple1)

Tuple1 = (tuple(['2','3','4','6']))
print(type(Tuple1))

Tuple2 = ('vivek')

Tuple3 = (Tuple1,Tuple2)
print(Tuple3)

#Boolean
bool1 = print(type(True))

#SETS

set1 = set()
print(type(set1))

set1 = set('vivek')
print(set1)
print(type(set1))

set1 = set(['2','3','4','6','2'])
print(set1)
print(type(set1))

set1 = set([1,2,'viv',4,'bro',2,9])
print(set1)

for i in set1:
    print(i,end=" ")

print("viv" in set1)

#Dictionary

Dict1 = {}
print(Dict1)
print(type(Dict1))

Dict1 = {1:'viv',2:'gandarla',3:"learning py"}
print(Dict1)
print(type(Dict1))

Dict1 = {'name' : 'viv',3:'is my','Nad': 'just checking is caps on'}
print(Dict1)
print(type(Dict1))

Dict1 = dict({'hey':'ada',2:'2','dd':'dd'})
print(Dict1)
print(type(Dict1))

Dict1 = dict([('var','ds'),(2,'ddd')])
print(Dict1)
print(type(Dict1))

print(Dict1['var'])
print(Dict1.get(2))


# #input  

# i = input("hey you name?")
# print(i)

# j = int(input("ur no?"))
# print(j,type(j))

# print("his name is ",i,"and no is ",j)

import time

count_time = 3

for i in reversed(range(count_time+1)):
    if i > 0:
        print(i,end=">>>")
        time.sleep(1)
    else:
        print("Start")
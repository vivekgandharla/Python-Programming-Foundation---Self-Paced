a = "geeks for geeks"
print(len(a))

pos = a.find("geeks")
print(pos)
while pos>=0:
    print(pos)
    pos = a.find("geeks",pos+1)
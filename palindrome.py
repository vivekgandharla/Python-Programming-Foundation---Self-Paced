s = input("Entr the name: ")

low = 0
high = len(s)-1

while low<high:
    if s[low] != s[high]:
        print("No")
        break
    low = low+1
    high = high-1
else:
    print("Yes")
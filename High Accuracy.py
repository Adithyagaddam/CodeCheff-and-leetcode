import math
for i in range(int(input())):
    a=int(input())
    s=math.ceil(a/3)
    k=math.floor(a/3)
    if a%3==0:
        print(a%3)
    elif a%3!=0:
        print(3-a%3)

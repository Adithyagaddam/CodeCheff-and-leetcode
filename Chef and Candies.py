import math
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if a>=b:
        print(math.ceil((a-b)/4))
    else:print(0)

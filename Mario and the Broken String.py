import math
for i in range(int(input())):
    s=int(input())
    k=input()
    a,b=k[:len(k)//2],k[len(k)//2:]
    if a==b:
        print("YES")
    else: print("NO")

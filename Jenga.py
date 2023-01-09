# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if b%a==0:
        print("YES")
    else:
        print("NO")

# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if (a+b)%2==0 :
        print(int((a+b)/2))
    else:print(-1)

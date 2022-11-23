for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    count=0
    while a>2:
        a=a/2
        count+=1
    print(((count+1)*b)+(count*c))

t=int(input())
while(t>0):
    t-=1 
    n,a,b= map(int,input().split())
    arr= list(map(int,input().strip().split()))
    x,y=0,0
    for i in arr:
        if(i==a):
            x+=1 
        if(i==b):
            y+=1 
    print((x/n)*(y/n))

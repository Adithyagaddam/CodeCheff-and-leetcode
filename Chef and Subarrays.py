import math
t= int(input())
while(t>0):
    t-=1 
    n=int(input())
    arr=list(map(int,input().strip().split()))
    count=0
    for i in range(0,n):
        temp=[]
        for j in range(i,n):
            temp.append(arr[j])
            product=1
            for x in temp:
                product*=x 
            if(sum(temp)==product):
                count+=1
    print(count)

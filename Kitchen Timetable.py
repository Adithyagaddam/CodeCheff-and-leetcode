n=int(input())
for i in range(n):
    s=int(input())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    c=[a[0]]
    count=0
    for i in range(s-1):
        k=a[i+1]-a[i]
        c.append(k)
    for i in range(s):
        if c[i]>=b[i]:
            count+=1 
    print(count)
    

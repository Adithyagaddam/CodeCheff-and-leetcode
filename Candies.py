# cook your dish here
for i in range(int(input())):
    s=int(input())
    p=2*s
    a=list(map(int,input().strip().split()))
    k=a[:s]
    r=a[s:]
    t=[]
    for i in range(len(r)):
        for j in range(len(k)):
            if k[i]==r[j]:
                t.append("NO")
                
            else:
                t.append("YES")
    if "NO" in t:
        print("NO")
    else:
        print("YES")

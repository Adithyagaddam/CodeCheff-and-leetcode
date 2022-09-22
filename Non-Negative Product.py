n=int(input())
for i in range(n):
    s=int(input())
    k=1
    list1 = [int(n) for n in input().split()]
    for i in list1:
        k=k*i
        
    if k<0:
        print(1)
    else:print(0)

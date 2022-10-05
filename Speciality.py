n=int(input())
for i in range(n):
    a,b,c=map(int,input().strip().split())
    k=max(a,b,c)
    if k==a:
        print("Setter")
    elif k==b:
        print("Tester")
    else:
        print("Editorialist")

# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    if (b*1+c*2)>=a:
        print("Qualify")
    else:
        print("NotQualify")

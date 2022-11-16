for i in range(int(input())):
    a,b=map(int,input().strip().split())
    if(a+b>1):
        for i in range(2,a+b):
            if (a+b)%i==0:
                print("Bob")
            else:
                print("Alice")

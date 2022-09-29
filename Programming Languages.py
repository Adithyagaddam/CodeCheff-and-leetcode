t=int(input())
for i in range(t):
    A,B,c,d,e,f=map(int,input().split())
    if( d==A and c==B ):
        print(1)
    elif( d==B and c==A):
        print(1)
    elif( f==A and e==B):
        print(2)
    elif( f==B and e==A):
        print(2)
    else:
        print(0)

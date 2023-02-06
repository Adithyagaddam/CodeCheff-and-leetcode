for i in range(int(input())):
    a,b,c=map(int,input().strip().split())
    if min(a,b,c)==a:
        print("ALICE")
    elif min(a,b,c)==b:
        print("BOB")
    elif min(a,b,c)==c:
        print("CHARLIE")

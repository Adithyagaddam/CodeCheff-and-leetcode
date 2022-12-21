for i in range(int(input())):
    a=int(input())
    b=str(input())
    c=str(input())
    if b.count("1")==c.count("1") and b.count("0")==c.count("0"):
        print("YES")
    else:
        print("NO")

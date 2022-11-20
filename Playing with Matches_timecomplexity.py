for i in range(int(input())):
    a,b=map(int,input().strip().split())
    s=a+b
    c=str(s)
    count=0
    for i in range(len(c)):
        if c[i]=='1':
            count=count+2
        elif c[i]=='7':
            count=count+3
        elif c[i]=='4':
            count+=4
        elif c[i]=='2' or c[i]=='3' or c[i]=='5':
            count+=5
        elif c[i]=='0' or c[i]=='6' or c[i]=='9':
            count+=6
        else:
            count+=7
    print(count)

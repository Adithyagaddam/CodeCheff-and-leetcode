for _ in range(int(input())):
    t = int(input())
    s=''
    for i in range(t):
        if(t%4==0):
            if i%4==0 or (i+1)%4==0:
                s=s+'0'
            else:
                s=s+'1'
        else:
            if i ==0 or i==t-1:
                s=s+'0'
            else:
                s=s+'1'
    print(s)
            

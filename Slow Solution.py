t = int(input())
for i in range(t):
    maxt, maxn, sumn = map(int, input().split())
    d = sumn//maxn
    r = sumn%maxn
    wc = 0
    if(d+1 <= maxt):
        wc = d*(maxn**2) + r**2
    elif(d <= maxt):
        wc = d*(maxn**2)
    else:
        wc = maxt*(maxn**2)
    print(wc)

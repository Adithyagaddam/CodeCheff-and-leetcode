#Economics Class
#Problem
#Alice has recently learned in her economics class that the market is said to be in equilibrium when the supply is equal to the demand.
n=int(input())
for TC in range(n):
    s=int(input())
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    count=0
    for i in range(s):
        if a[i]==b[i]:
           count +=1
    print(count)
    
#RCB and Playoffs
#Team RCB has earned XX points in the games it has played so far in this year's IPL. To qualify for the playoffs they must earn at least a total of YY points. They currently have ZZ games left, in each game they earn 22 points for a win, 11 point for a draw, and no points for a loss.
T=int(input())
for i in range(T):
    x,y,z=map(int,input().split())
    a=y-x
    z*=2
    if(a<=z):
        print("Yes")
    else:
        print("No")
#Lazy Chef
#Chef is a very lazy person. Whatever work is supposed to be finished in xx units of time, he finishes it in m * xm∗x units of time. But there is always a limit to laziness, so he delays the work by at max dd units of time. Given x, m, dx,m,d, find the maximum time taken by Chef to complete the work.
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    s=a*b 
    r=a+c 
    print(min(s,r))
#Hardest Problem Bet
#There are 33 problems in a contest namely A, B, CA,B,C respectively. Alice bets Bob that problem CC is the hardest while Bob says that problem BB will be the hardest.
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    s=min(a,b,c)
    if s==a:
        print("Draw")
    elif s==b:
        print("Bob")
    elif s==c:
        print("Alice")

#Wordle
#Problem
#Chef invented a modified wordle.There is a hidden word SS and a guess word TT, both of length 55.Chef defines a string MM to determine the correctness of the guess word. For the i^{th}ith index:
n=int(input())
for i in range(n):
    a=list(input())
    b=list(input())
    for i in range(len(a)):
        if a[i]==b[i]:
            print("G",end='')
        else:
            print("B",end='')
    print('')
 
#Complete the credits
#In Uttu's college, a semester is said to be a:Overload semester if the number of credits taken \gt 65>65.Underload semester if the number of credits taken \lt 35<35.Normal semester otherwise Given the number of credits XX taken by Uttu, determine whether the semester is Overload, Underload or Normal.
n=int(input())
for i in range(n):
    s=int(input())
    if s>65:
        print("Overload")
    elif s>=35 and s<=65:
        print("Normal")
    else:
        print("Underload")
#Gross Salary
#In a company an emplopyee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary.If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary.
n=int(input())
for i in range(n):
    s=int(input())
    if s<1500:
        hr=(s/100)*10 
        da=(s/100)*90
        print(s+hr+da)
    else:
        hr=500 
        da=(s/100)*98
        print(s+hr+da)

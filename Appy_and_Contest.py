t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    n=(a/b)+a/c
    if(n>=d):
        print("Win")
    else:
        print("Lose")
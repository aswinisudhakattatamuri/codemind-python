def perfect_num(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if(n==s):
        return True
    return False
    
n=int(input())
res=perfect_num(n)
print(res)
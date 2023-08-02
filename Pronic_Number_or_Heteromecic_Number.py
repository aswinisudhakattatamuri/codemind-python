def pronic_num(n):
    for i in range(1,n):
        if i*(i+1)==n:
            return True
    return False
n=int(input())
res=pronic_num(n)
if res==True:
    print("YES")
else:
    print("NO")
    
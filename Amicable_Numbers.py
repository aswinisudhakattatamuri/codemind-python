def sum_of_divisors(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
a=int(input())
b=int(input())
res1=sum_of_divisors(a)
res2=sum_of_divisors(b)
if(res1==b and res2==a):
    print("Amicable")
else:
    print("Not Amicable")
#spy number
num=int(input())
temp=num
s=0
while(num>0):
    r=num%10
    s=s+r
    num=num//10
p=1
while(temp>0):
    r=temp%10
    p=p*r
    temp=temp//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
#neon number
num=int(input())
temp=num
sq=num*num
s=0
while(sq>0):
    r=sq%10
    s=s+r
    sq=sq//10
if temp==s:
    print("Neon Number")
else:
    print("Not Neon Number")
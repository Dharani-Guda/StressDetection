l=list(map(int,input().split()))
print(l)
b=sum(l)
if(b>=11 and b<=19):
    ToSCTotal=11
elif(b>=20 and b<=28):
    ToSCTotal=16
elif(b>=29 and b<=38):
    ToSCTotal=22
elif(b>=39 and b<=48):
    ToSCTotal=27
elif(b<=49 and b>=58):
    ToSCTotal=34
elif(b<=59 and b>=67):
    ToSCTotal=39
else:
    ToSCTotal=46
print(ToSCTotal)
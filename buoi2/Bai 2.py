#Bai 2
a=int(input())
b=int(input())
print(" a + b =",a+b)
print(" a - b =",a-b)
print(" a * b =",a*b)
print(" a / b =",a//b)
print(" a chia du b =",a%b)
print(" a mu b =",a**b)
if a>b:
    print("So",a," lon hon so",b)
    print("So",b," nho hon so",a)
elif b>a:
    print("So",b," lon hon so",a)
    print("So",a," nho hon so",b)
else:
    print("Hai so bang nhau")
Tam=(a>0) and (b>0)
print(Tam)
D=(a<1) or (b>10)
print(D)
F=(a>2) ^ (b<1)
print(F)
K=not(a==b)
print(K)
print(a>>1)
print(a<<1)


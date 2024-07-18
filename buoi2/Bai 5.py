print("Nhap so n:")
n=int(input())
a=n
sum=0
while n>0:
    socuoi=n%10
    sum=sum+socuoi**3
    n//=10
if sum==a:
    print("La so armstrong")
else:
    print("Khong la so armtrong")
#Bài 1 ý b
print("Moi ban nhap so nguyen duong n:")
n=int(input())
Tong=1
while n<0:
    print("Moi ban nhap lai so nguyen duong n>0:")
for i in range(2,n+1,1):
    if(n%i==0):
        print(i)
        Tong+=i
print(Tong)
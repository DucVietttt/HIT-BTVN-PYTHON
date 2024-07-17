#Bài 1 ý a
n=int(input())
while n<0:
    print("Moi ban nhap lai n>0: ")
    n=int(input())
Tong=0
while n>0:
    socuoi=n%10
    Tong+=socuoi
    n//=10
print(Tong)
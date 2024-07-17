#Bài 1 ý c
print("Moi ban nhap 3 canh cua tam giac:")
a=int(input())
b=int(input())
c=int(input())
while a<0 and b<0 and c<0:
    print("Moi ban nhap lai 3 canh cua tam giac a,b va c >0:")
    a=int(input())
    b=int(input())
    c=int(input())
print("La tam giac") if a+b>c and b+c>a and a+c>b else print("Khong phai la tam giac")
if a==b or b==c:
    print("Day la tam giac can")
elif a==b and b==c and a==c:
    print("Day la tam giac deu")
elif a*a==b*b + c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print("Day la tam giac vuong")
elif a*a>b*b + c*c or b*b>a*a+c*c or c*c>a*a+b*b:
    print("Day la tam giac tu")
else:
    print("Day la tam giac nhon")

#Bai 3 
n=int(input())
Tong=1
for i in range(1,n+1,1):
    Tong=Tong-2*i+(2*i+1)
print("Tong 1-2+3-4+5+...+2*n+1 la",Tong)
Sum=0
for i in range(1,n+1,1):
    Sum+=1/i
print("Tong 1+1/2+1/3+1/4+...+1/i la:",Sum)
print("Nhap he so a,b,c:")
a=float(input())
b=float(input())
c=float(input())
Denta=b*b-4*a*c
if Denta>0:
    print("PT bac 2 1 an co hai nghiem")
    x1=(-b+(Denta**1/2))/2*a
    x2=(-b-(Denta**1/2))/2*a
    print("x1 = ",x1," x2 = ",x2)
elif Denta==0:
    print("PT bac 2 1 an co 1 nghiem kep")
    print("x=",-b/2*a)
else:
    print("PT bac 2 1 an  vo nghiem")

print("Nhap so n:")
n=int(input())
f0=0
f1=1
f2=1
print("n so fib dau tien la:")
print(f0,f1,f2)
for i in range(n,2,-1):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3, end=' ')
print()
print("So thu ",n ,"trong day la: ",f3)
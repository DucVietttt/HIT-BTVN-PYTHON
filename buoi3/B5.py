N=int(input("Nhap n:"))
while N<1 and N>100:
    N=int(input("Nhap n:"))
L=[int(input()) for _ in range(N)]
Dem=0
L1=[]
for i in range(N):
    s=L[i]%10
    if s%2!=0:
        Dem+=1
        L1.append(L[i])
print(Dem)
print(L1)
    
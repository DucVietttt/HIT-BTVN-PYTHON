def Giaithua(n):
    if n==0 or n==1 :
        return 1;
    else:
        return n*Giaithua(n-1)
def Tohop(n,k):
    return int(Giaithua(n)/(Giaithua(n-k)*Giaithua(k)))
print("Nhap n:")
n=int(input())
for i in range(0,n+1):
    for j in range(0,n-i+1):
        print("",end = " ")
    for j in range(0, i + 1):
        print(" {:<3}".format(Tohop(i, j)), end="")
 
    print("")

#B2
k=int(input("Nhap so phan tu cua list"))
lst = [int(input()) for _ in range(k)]  
n=int(input("Nhap  so dong ma tran:"))
m=int(input("Nhap so cot cua ma tran:"))
Matran=[]
if n*m>k:
     print("NO")
else:
    for i in range(n):
        row = lst[i * m:(i + 1) * m]
        Matran.append(row)
    for row in Matran:
        print(row)

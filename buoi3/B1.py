import math
#Bài 1 ý a
n=int(input())
a=[int(input()) for _ in range(n)]
X=int(input())
print(a.count(X))
#Bài 1 ý b
a[2:7]=[8,5,4,0,1,3]
print(a)
#Bài 1 ý c và d
print("Gía trị lớn nhất trong list là:", max(a))
print("Gía trị nhỏ nhất trong list là:", min(a))
#Bài 1 ý e f
Y=int(input())
a[:0]=[Y]
print(a)
KTtang=True
KTgiam=False
for i in range(len(a)-1):
    if a[i]<a[i+1]:
       KTgiam=False
       break
    if a[i]>a[i+1]:
        KTtang=False
        break
if KTtang:
    print("TANG")
elif KTgiam:
    print("GIAM")
else:
    print("NO")
#Bài 1 ý g 
sum=0
for i in range(1,len(a)):
    sum+=a[i]
N=int(input())
L=[]
for i in range(N):
    L.append(sum)
print(L)
#Bài 1 ý h
L1=[94,39,49,6,-55,-37,1,-23,-31,1000]
L1.sort(reverse=False)
print("Chuỗi sắp xếp tăng dần là:", L1)
TTD= list(map(abs,L1))
TTD.sort(reverse=False)
print("Chuỗi sắp xếp tăng dần theo giá trị tuyệt đối là:", TTD)


a = int(input())
Set = {int(input()) for i in range(a)}
print(Set)
b = int(input())
L=[]
Sum=0
for x in Set:
    Sum+=x
    if Sum <= b:
        L.append(x)
Set2=set(L)
print(Set2)
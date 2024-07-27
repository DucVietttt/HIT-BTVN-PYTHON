s1=input("Nhap chuoi s1: ")
s2=input("Nhap chuoi s2: ")
dao_nguoc=s1[::-1]
print(dao_nguoc)
print("Nhap hai so nguyen a va b:")
a=int(input())
b=int(input())
while a<1 or b<1 or a>len(s2) or b>len(s2) :
    a=int(input())
    b=int(input())
doan_dau_s2=s2[:a]
dao_nguoc_s2 = s2[b:a-1:-1]
doan_sau_s2=s2[b+1:]
print(doan_dau_s2 + dao_nguoc_s2 + doan_sau_s2)
#Xóa các phần tử ở vị trí chẵn
s3=""
for i in range(len(s1)):
    if i%2!=0:
        s3+=s1[i]
print(s3)
#Ghép hai chuỗi xen kẽ
s4 = ""
do_dai_ngan_hon_hai_chuoi = min(len(s1), len(s2))

for i in range(do_dai_ngan_hon_hai_chuoi):
    s4 += s1[i] + s2[i]
if len(s1) > len(s2):
    s4 += s1[do_dai_ngan_hon_hai_chuoi:]
else:
    s4 += s2[do_dai_ngan_hon_hai_chuoi:]
print(s4)
                
               
#a= int(input()) #NhAP VAO MOT SO NGUYEN
#s= str(input('Nhap chuoi vao') ) #Kieu string Python
#List la kieu du lieu 
#kiem tra bien vua khai bao la kieu gi :
#print(type(1))
#list1 = [1,2,3,4,5] #list co  the thay doi duoc
#print(list1[1]) #truy cap pan tu trong list
#tuple_pt=('t','u','p')
#my_dict = {
    #"ten":"Viet",
    #"gioi tinh":"Nam",
    #"Nam sinh": 2005
#}
#
# print(type(my_dict))
a=5
b=4
print('a = ',a)
print('{} {}'.format(a,b))
print(f'{a} +{b} ={a+b}')
print(a+b)
print(a**b) #toan tu mũ
print(a/b) #toan tu chia
print(a%b) #toan tu chia lay du
print(a//b) #toan tu chia lay phần nguyên hay còn gọi là làm tròn
#toan tu logic and(giống &&),or(giống ||),not(nếu biểu thức là true thì nó sẽ trả về false và ngược lại)
x=5
print(x<6 and x<10)
print(x<6 or x<10)
print(not(x<6 and x<10))
x=[1,2,3]
print(a in x)
#Toan tu nhan dang is
#toan tu bitwise Operators dich bit
#if trong python
#vong lap
for i in range(1,6,2):
    print(i,end=' ')
print()
 l=[1,2,3,4]
# print (l[-2])
# print(l[2])
for i in l:
    print(i,end=' ')
#vong lap while
print()
y=10
while y>5:
    print(y,end=' ')
    y-=1
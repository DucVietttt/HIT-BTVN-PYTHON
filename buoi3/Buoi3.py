#my_string='Hello'
#my_string="Hello"
#my_string='''Hello'''
# my_string='''Hello world
# helo python
# '''
# s="Hệ nhị phân của {0}" 
# print(my_string)
# s= "Một phần ba: {0:.3f}".format(1/3)
# print(s)
# s1=bin(11)
# print(s1)
# a='HIT PYTHON'
# for i in range(len(a)):
#     print(a[i],end=' ')
# print(a[-2])
# print()
# print(a[0:3:2])
# b='stt'
# b=b.lower()
# print(b);
#b=b.upper()
#print(b)
#s1='stt'
# print(b==s1)
# count=0
#print(len(input().split()))
#list danh sách
# l=[1,2,3,[3,4,5],6]
# print(l[3][1])
# print(l[2])
# l1=[x for x in range(10)]
#print(l1)
#l2=[int(input()) for _ in range(5)]
# print(l2)
# vector = [[1,2,3],[4,5,6],[7,8,9]]
# L=[]
# for list in vector:
#     for num in list:
#         L.append(num)
# print(L)
L1=[x for x in range(10) if x%2==0]
print(L1)
l3=L1[1:3]
print(l3)
a=[int(input()) for _ in range(5)]
b=[int(input()) for _ in range(5)]
a.sort()
print(a)
b=b*2
b.reverse()
c=a+b
print(c)

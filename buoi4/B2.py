x = int(input("Nhập số lượng sinh viên đăng ký tại bàn 1: "))
Ban1 = {input(f"Nhập mã sinh viên {i+1}: ") for i in range(x)}
y = int(input("Nhập số lượng sinh viên đăng ký tại bàn 2: "))
Ban2 = {input(f"Nhập mã sinh viên {i+1}: ") for i in range(y)}
KT = Ban1.intersection(Ban2)
if KT:
   print("Sinh viên đăng ký học tại cả hai bàn:", KT)
else:
   print("Không có sinh viên nào đăng ký học tại cả hai bàn.")
KT2=Ban1.union(Ban2)
print("Danh sách tổng hợp sinh viện đăng ký cả hai bàn là",KT2)
KT3=Ban1.difference(Ban2)
print("Danh sách sinh viên đăng kí 1 mà không đăng kí bàn 2: ",KT3)


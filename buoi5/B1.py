Tu_dien = {}
Dem = 0
so_SV = int(input("Nhập số lượng sinh viên: "))
for _ in range(so_SV):
    Ma_SV = input("Mời bạn nhập mã sinh viên: ")
    Diem = float(input("Mời bạn nhập điểm tổng kết: "))
    Tu_dien[Ma_SV] = Diem

print("Danh sách sinh viên ban đầu:")
for key, value in Tu_dien.items():
    print(f'Mã sinh viên: {key} - Điểm: {value}')

for value in Tu_dien.values():
    if 3.0 <= value <= 3.5:
        Dem += 1

print(f'Số lượng sinh viên có điểm tổng kết từ 3.0 đến 3.5: {Dem}')

Them_SV = int(input("Nhập số sinh viên bạn cần thêm: "))
for _ in range(Them_SV):
    Ma_SV_them = input("Nhập mã sinh viên thêm: ")
    Diem_them = float(input("Nhập điểm tổng kết: "))
    Tu_dien[Ma_SV_them] = Diem_them

print("Danh sách sinh viên sau khi thêm:")
for key, value in Tu_dien.items():
    print(f'Mã sinh viên: {key} - Điểm: {value}')
Tu_dien = {k: v for k, v in Tu_dien.items() if v >= 2.0}
print("Toàn bộ từ điển sinh viên sau khi xóa:")
for key, value in Tu_dien.items():
    print(f'Mã sinh viên: {key} - Điểm tổng kết: {value}')

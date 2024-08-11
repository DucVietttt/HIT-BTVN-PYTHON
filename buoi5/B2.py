chuoi = input("Nhập chuỗi: ")
dict_ky_tu = {}
for ky_tu in chuoi:
    if ky_tu in dict_ky_tu:
        dict_ky_tu[ky_tu] += 1
    else:
        dict_ky_tu[ky_tu] = 1
print("Số lần xuất hiện của các ký tự trong chuỗi:")
for key, value in dict_ky_tu.items():
    print(f'Ký tự: {key} - Số lần xuất hiện: {value}')

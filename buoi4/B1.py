n = int(input("Nhập số lượng phần tử: "))
tuple_p = tuple(str(input(f"Nhập chuỗi thứ {i+1}: ")) for i in range(n)) 
Tuple = tuple(int(x) for x in tuple_p)
Trungbinh = sum(Tuple)/len(Tuple)
print(f"Giá trị trung bình là: {Trungbinh}")
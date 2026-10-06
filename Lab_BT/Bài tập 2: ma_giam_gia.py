name = input("Nhập họ tên: ")
year = input("Nhập năm sinh: ")

words = name.split()
last = words[-1]
code = last[0:3].upper()

print(f"{code}-{year}-VIP")

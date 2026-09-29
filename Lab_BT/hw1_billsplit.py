X = float(input("Nhập tổng hóa đơn X: "))
Y = float(input("Nhập % tip Y: "))
N = int(input("Nhập số người N: "))

tip = X * Y / 100
tong = X + tip
moi_nguoi = tong / N

print("Mỗi người phải trả:", round(moi_nguoi), "đồng")

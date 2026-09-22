# Bài tập 2: Tính hóa đơn bán lẻ thương mại điện tử
print("=== HỆ THỐNG TÍNH HÓA ĐƠN ===")

# 1. Nhận dữ liệu đầu vào từ bàn phím
ten_san_pham = input("Nhập tên sản phẩm: ").strip()
so_luong_input = input("Nhập số lượng: ")
don_gia_input = input("Nhập đơn giá (VND): ")

# 2. Ép kiểu dữ liệu
# Số lượng -> số nguyên (int), Đơn giá -> số thực (float)
so_luong = int(so_luong_input)
don_gia = float(don_gia_input)

# 3. Tính toán hóa đơn
tong_tien_hang = so_luong * don_gia
thue_vat = tong_tien_hang * 0.08
tong_thanh_toan = tong_tien_hang + thue_vat

# 4. In hóa đơn bằng F-string
# Dùng :,.0f để hiển thị số tiền có dấu phân cách hàng nghìn
print("\n" + "=" * 40)
print("       HÓA ĐƠN BÁN HÀNG")
print("=" * 40)
print(f"Tên sản phẩm    : {ten_san_pham}")
print(f"Số lượng        : {so_luong}")
print(f"Đơn giá         : {don_gia:,.0f} VND")
print(f"Tổng tiền hàng  : {tong_tien_hang:,.0f} VND")
print(f"Thuế VAT (8%)   : {thue_vat:,.0f} VND")
print(f"Tổng thanh toán : {tong_thanh_toan:,.0f} VND")
print("=" * 40)
print("Cảm ơn quý khách đã mua hàng!")

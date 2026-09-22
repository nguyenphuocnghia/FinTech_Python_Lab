# Bài tập 1: Mở ví điện tử ban đầu
print("=== HỆ THỐNG MỞ VÍ ĐIỆN TỬ ===")

# 1. Nhận dữ liệu đầu vào từ bàn phím
ho_ten_raw = input("Nhập họ và tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd_raw = input("Nhập số Căn cước công dân (CCCD): ")
so_tien_input = input("Nhập số tiền nạp ban đầu vào ví (VND): ")

# 2. Chuẩn hóa dữ liệu
# .strip() để bỏ khoảng trắng thừa, .upper() để in hoa toàn bộ họ tên
ho_ten_chuan = ho_ten_raw.strip().upper()

# Cắt chuỗi để lấy 4 số cuối của CCCD
cccd_chuan = cccd_raw.strip()
cccd_4so_cuoi = cccd_chuan[-4:]

# Đổi số tiền nạp từ chuỗi (string) sang số nguyên (int)
so_tien_nap = int(so_tien_input)

# 3. Tính phí mở ví và số dư khả dụng thực tế
phi_mo_vi = 50000
so_du = so_tien_nap - phi_mo_vi

# 4. In biên lai khởi tạo ví bằng F-string
print("\n" + "=" * 40)
print("     BIÊN LAI MỞ VÍ ĐIỆN TỬ")
print("=" * 40)
print(f"Họ và tên      : {ho_ten_chuan}")
print(f"Số điện thoại  : {so_dien_thoai}")
print(f"CCCD           : ***{cccd_4so_cuoi}")
print(f"Số tiền nạp    : {so_tien_nap} VND")
print(f"Phí mở ví      : {phi_mo_vi} VND")
print(f"Số dư khả dụng : {so_du} VND")
print("=" * 40)
print("Cảm ơn quý khách đã mở ví điện tử!")


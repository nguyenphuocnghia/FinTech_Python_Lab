email = input("Nhập email: ")
ten_dang_nhap, ten_mien = email.split("@")
ba_ky_tu_dau = ten_dang_nhap[0:3]
ket_qua = ba_ky_tu_dau + "***@" + ten_mien
print(ket_qua)

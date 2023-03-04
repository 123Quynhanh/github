GiaNiemYet=float(input('nhap gia niem yet'))
ChietKhau=float(input('nhap chiet khau'))
VAT=(GiaNiemYet- ChietKhau)*0.01
GiaBan=GiaNiemYet - ChietKhau + VAT
print('Gia ban:', GiaBan)
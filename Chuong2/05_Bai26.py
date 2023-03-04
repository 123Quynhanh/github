HoTen=input('Ho ten:')
SoNgay=int(input('So ngay cong:'))
DonGia=float(input('Don gia ngay cong:'))
PhuCap=float(input('He so phu cap:'))
TamUng=int(input('Tam ung:'))
Luong=DonGia*SoNgay*PhuCap
ThucLinh=Luong-TamUng
print('Nhan vien', HoTen,end=',',)
print(' Co tien Luong=',Luong,end=',',sep='')
print(' Tam ung=',TamUng,end=' va',sep='')
print(' Thuc linh=',ThucLinh,sep='')
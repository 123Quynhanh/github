a=float(input('Tieu thu='))
if a<=100:
    Tien=a*550
elif a<=150:
    Tien=100*550+(a-100)*750
elif a<=200:
    Tien=100*550+50*750+(a-150)*950
else:
    Tien=100*550+50*750+50*950+(a-200)*1350
VAT=0.1
ThanhTien=Tien+VAT*Tien
print('Phai tra=',round(ThanhTien,1),sep='')
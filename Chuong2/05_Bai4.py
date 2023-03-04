import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
S=(a+b+c)/2
DienTich=math.sqrt(S*(S-a)*(S-b)*(S-c))
print('Dien tich',DienTich)
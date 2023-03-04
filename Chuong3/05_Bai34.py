t=float(input(''))
l=float(input(''))
h=float(input(''))
DTB=(t*2+l*3+h)/6
if DTB <3:
    print('Kem')
elif DTB<5:
    print('Yeu')
elif DTB<6:
    print('Trung binh')
elif DTB<7:
    print('Trung binh kha')
elif DTB<8:   
    print('Kha')
elif DTB<9:
    print('Gioi')
else:
    print('Xuat sac')
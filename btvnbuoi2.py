# bài 1:
thang = int(input("Nhập vào tháng = "))
nam = int(input("Nhập vào năm = "))
if(nam >= 0 and thang >= 1 and thang <= 12):
    if(nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
            print('có 31 ngày')
        elif(thang == 4 or thang == 6 or thang == 9 or thang == 11):
            print('có 30 ngày')
        else: print('có 29 ngày')
    else:
        if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
            print('có 31 ngày')
        elif(thang == 4 or thang == 6 or thang == 9 or thang == 11):
            print('có 30 ngày')
        else: print('có 28 ngày')
else: print('INVALID')
# bài 2
luong = int(input('Nhập vào lương của bạn = '))
thue = int()
tien = int()
if(luong >= 15000000):
    thue = luong * 0.3
    tien = luong - thue
    print('Thuế = ', thue, 'Thu nhập = ', tien)
elif(luong >= 7000000 and luong < 15000000):
    thue = luong * 0.2
    tien = luong - thue
    print('Thuế = ', thue, 'Thu nhập = ', tien)
else:
    thue = luong * 0.1
    tien = luong - thue
    print('Thuế = ', thue, 'Thu nhập = ', tien)
# bài 3:
so = int(input("Nhập vào một số: "))
tong = 0
dem = 0
while so != 0:
    tong += so % 10
    so //= 10
    dem += 1
print('Tổng các chữ số = ', tong, 'Số chữ số = ', dem)
# bài 4:
xu = int(input('Nhập vào số xu của bạn: '))
vochai = xu // 28
votang = vochai // 3
print("Số chai bia = ", vochai + votang)
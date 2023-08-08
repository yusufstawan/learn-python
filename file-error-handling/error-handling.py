# a = 10
# b = 0
# try:
#     hasil = a / b
#     print(hasil)
# except:
#     print('terjadi kesalahan saat perhitungan')

# multiple except
a = 10
b = 0
try:
    hasil = a / b
    print(hasil)
except TypeError:
    print("Kesalahan pada unit perhitungan")
except ZeroDivisionError:
    print("Membagi dengan nilai 0")
except:
    print('Error yang tidak diketahui')
else:
    print("Sukses")
finally:
    print("Program dimatikan")

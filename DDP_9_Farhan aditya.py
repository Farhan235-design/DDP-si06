print("\n====== no 1 ==========")
print("\ncelcius ke fahrenheit")
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print("\n===== no 2 =====")
print("\nmencari bilangan genap")
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print("\n===== no 3 =====")
print("\nketerangan lulus dan tidak lulus")
# rata" nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print("lulus")
    else:
        print("gagal")
skor(80)
skor(60)

print("\n===== no 4 =====")
print("\nmencetak bilangan ganjil")
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i)
bil_ganjil(20)
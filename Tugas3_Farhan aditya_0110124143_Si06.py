nama = "Farhan aditya"
nim = "0110124143"
kelas = "Si06"
no_telp = "083806481336"
alamat = "kp.sudimampir,bojong gede,bogor"

print("nama saya:", nama)
print("nim saya:", nim)
print("kelas saya:", kelas)
print("no telp saya:", no_telp)
print("alamat saya:", alamat)

print("=====================================")

nama = "adam al muharrom sholeh"
nim = "0110124017"
kelas = "Si05"
no_telp = "083836911935"
alamat = "kp.kebon kopi,citeureup,kab bogor"

print("nama saya:", nama)
print("nim saya:", nim)
print("kelas saya:", kelas)
print("no telp saya:", no_telp)
print("alamat saya:", alamat)

print("=====================================")

TB = int(input("masukkan tinggi badan:"))

BB_ideal = (TB-100) - (TB-100) * 0,1 
print("berat badan ideal untuk mu:", BB_ideal)

print("===================================")

celcius = float(input("masukan nilai celcius"))
fahrenheit = 9/5*celcius +32
print(f"suhu dalam fahrenheit adalah:{fahrenheit:.2f}")

print("===================================")

r = int(input("masukan jari jari :"))
t = int(input("masukan tinggi :"))
la = int(input("masuka luas alas :"))
ka = int(input("masukan keliling alas :"))
phii = 22/7 

luas = (2 * la) + (ka + t)
keliling = phii * phii * r 

print("luas tabung adalah :", luas)
print("keliling tabuhg adalah:", keliling)

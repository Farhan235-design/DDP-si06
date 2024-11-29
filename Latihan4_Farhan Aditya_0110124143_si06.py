
angka = int(input("masukan bilangan bulat"))
ganjil = "Bilangan ganjil"
genap = "Bilangan genap"

if angka % 2 == 0:
   print(genap)
elif not (angka % 2 == 0):
   print (ganjil)
else :
 print("input tidak valid")
 
print("==============================")

nilai = int(input("masukkan nilai ujian"))
if nilai >=75:
  print("lulus")
else:
  print("tidak lulus")
  
print()
print("===============================")
print()
#usia
usia = int(input("masukkan usia"))
if usia >=18:
  print("dewasa")
elif usia < 18 and usia > 13:
  print("Remaja")
else :
  print("anak-anak")
print()
print("================================")
print()
#status keanggotaan
# 1: Minta input dari pengguna
status = input("Masukkan status keanggotaan (gold, silver, bronze): ").lower()

#  2: Cek status menggunakan if
if status == "gold" or status == "silver":
    # 3 Cetak pesan diskon
    print("Selamat! Anda mendapatkan diskon.")
else:
    print("Terima kasih atas partisipasi Anda.")
print("================================")
# Meminta pengguna memasukkan jumlah pembelian
jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))

# Menghitung total harga dengan diskon jika memenuhi syarat
diskon = 0.10 if jumlah_pembelian > 100 else 0
total_harga = jumlah_pembelian * (1 - diskon)

# Mencetak total harga
print(f"Total harga setelah diskon (jika ada): {total_harga:.2f}")
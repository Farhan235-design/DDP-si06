print("====No 01======")
kendaraan = ['ThunderBlade 250', 'Sepeda motor sport', '250cc', 'Hitam doff dengan aksen merah', '2']
print(kendaraan)

# Menambahkan data tambahan
kendaraan.append("Sportbike")
kendaraan.append('60 juta')
print(kendaraan)

# Menambahkan Yamaha R25 setelah elemen 'Sepeda motor sport'
index_of_type = kendaraan.index('Sepeda motor sport')
kendaraan.insert(index_of_type + 1, 'Yamaha R25')
print(kendaraan)
print("===============")


pilih =int(input("""selamat datang di aplikasi menghitung
1.menghitung luas persegi
2.menghitung luas lingkaran
3.menghitung luas segitiga \n"""))

match pilih :
   case 1 :
     print("kamu memilih 1 untuk menghitung luas persegi")
     sisi = int(input("masukan sisi persegi :"))
     luaspsg = sisi * sisi
     print("luas persegi yang sisinya",sisi,"adalah",luaspsg )
   case 2 :
      print("kamu memilih 2 untuk menghitung luas lingkaran")
      jari2 = int(input("masukan jari jari :"))
      luaslkr= 3.14 * jari2 * jari2
      print("luas lingkaran yang jari jarinya ",jari2,"adalah",luaslkr)
   case 3 :
      print("kamu memilih 3 untuk menghitung luas segitiga")
      alas= int(input("masukan alas segitiga :"))
      tinggi=int(input("masukan tinggi segitiga:"))
      luassegitiga = 0,5 * alas * tinggi 
      print("luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah",luassegitiga)
   case _:
      print("anda salah pilih")
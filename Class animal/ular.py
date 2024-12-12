from animal import *
print()
class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
     super().__init__(nama, makanan, hidup, berkembang_biak)
     self.warna = warna
     self.jenis = jenis

    def cetak_ular(self):
        super().cetak()
        print(f'hewan ini berwarna : {self.warna}')
        print(f'hewan ini berjenis :{self.jenis}')
sawah = ular('ular sawah', 'daging','darat', 'bertelur', 'brown', 'tidak berbisa')
sawah.cetak_ular()
print()
cobra = ular('ular cobra',  'daging', 'darat', 'bertelur', 'black', 'berbisa')
cobra.cetak_ular()
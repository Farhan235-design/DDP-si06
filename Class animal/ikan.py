from animal import *
print()
class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
     super().__init__(nama, makanan, hidup, berkembang_biak)
     self.warna_ikan = warna_ikan
     self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'hewan ini berwarna : {self.warna_ikan} dan hewan ini berjenis :{self.jenis_ikan}')

cupang = ikan('ikan cupang', 'cacing rambut','air', 'bertelur', 'white', 'air tawar')
cupang.cetak_ikan()
print()
travis = ikan('ikan travis', 'plankton','air', 'bertelur', 'blue and green', 'air asin')
travis.cetak_ikan()
class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak (self):
        print(f'Hewan : {self.nama}')
        print(f'hewan ini memakan : {self.makanan}')
        print(f'hewan ini hidup : {self.hidup}')
        print(f'hewan ini berkembang biak dengan cara : {self.berkembang_biak}')
        
C1 = Animal('buaya', 'daging', 'amphibi', 'bertelur')
C1.cetak()    
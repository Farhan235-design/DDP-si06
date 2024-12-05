from Gempa import *

#membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa("banten", 1.2)
gempa2 = Gempa("palu", 6.1)
gempa3 = Gempa("cianjur", 5.6)
gempa4 = Gempa("jaya pura", 3.3)
gempa5 = Gempa("garut", 4.0)
#info gempa
print("## Gempa Bumi info ##")
print()
gempa1.dampak()#memanggil method dampak
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()

"""     RUMUS

TBA = Tinggi badan ayah
TBI = Tinggi badan ibu

Laki-laki : (TBA + TBI + 13cm / 2)
Perempuan : (TBA + TBI - 13cm / 2)

Min : hasil - 8.5cm
Max : hasil + 8.5cm

Source : https://vt.tiktok.com/ZGJByMPxH/
"""
def tLaki(tba, tbi):
    hasil = (tba + tbi + 13) / 2
    min   = int(hasil - 8.5)
    max   = int(hasil + 8.5)
    print(f"\nTinggi Badan Anak Laki-Laki :\nMin : {min} cm\nMax : {max} cm")
    pass

def tPerempuan(tba, tbi):
    hasil = (tba + tbi - 13) / 2
    min   = int(hasil - 8.5)
    max   = int(hasil + 8.5)
    print(f"\nTinggi Badan Anak Perempuan :\nMin : {min} cm\nMax : {max} cm")
    pass
tba = int(input('Tinggi Badan Ayah : '))
tbi = int(input('Tinggi Badan Ibu  : '))
tLaki(tba, tbi)
tPerempuan(tba, tbi)

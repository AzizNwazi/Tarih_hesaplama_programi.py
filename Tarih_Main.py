from Tarih_Modul import *

print("ilk tarihi girin: ") # kullanıcıdan ilk gün, ay ve yıl tarihi al

gun1 = int(input("Gun : ")) 
ay1 = int(input("Ay : "))
yil1 = int(input("Yil : "))

print("Ikinci tarihi girin: ") # kullanıcıdan ikinci gün, ay ve yıl tarihi al

gun2 = int(input("Gun : ")) 
ay2 = int(input("Ay : "))
yil2 = int(input("Yil : "))


tarih1 = [gun1, ay1, yil1] # Tarihleri listelere kaydet
tarih2 = [gun2, ay2, yil2]

# Kullanıcıya girdiği tarih aralığını göster
print("\n",f"{yil1}-{ay1}-{gun1}",f" {yil2}-{ay2}-{gun2}","Tarihleri arsinda")

# fonksiyonları çağırarak gün ve hafta sayısını hesapla

gun_sayisi = gun_sayisi_hesapla(tarih1,tarih2)

hafta_sayisi_hesapla(gun_sayisi)



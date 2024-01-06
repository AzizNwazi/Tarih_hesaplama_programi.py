def gun_sayisi_hesapla(tarih1,tarih2): # iki tarih arasındaki gün sayısını hesaplamak için kullanılan fonksiyon

    gun_farki = abs((tarih2[0] - tarih1[0]) + # iki tarih arasındaki gün farkını hesapla
                    (tarih2[1] - tarih1[1])*30 + 
                    (tarih2[2] - tarih1[2])*365  )

    print("Gun farki: \n",gun_farki) # iki tarih arasındaki gün farkını yazdır

    return gun_farki
    



def hafta_sayisi_hesapla(gun_farki): # iki tarih arasındaki hafta sayısını hesaplamak için kullanılan fonksiyon

    hafta_sayisi = gun_farki //7  # iki tarih arasındaki hafta sayısını hesapla

    print("Hafta farki : \n",hafta_sayisi) # hafta fark sayısını ekrana yazdır

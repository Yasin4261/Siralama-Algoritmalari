sayılar = ["1","2","3","4","5","6","7","8","9"]

print(sayılar,"Düzensiz\n")
islem = True
i = 0
while True:
        if sayılar[i] < sayılar[i+1]:
                sayılar[i], sayılar[i+1] = sayılar[i+1], sayılar[i]
                i += 1
                print(sayılar)
        else:
                i += 1
        if i == 8:
                i = 0
#Ufak bir hata var sonsuz döngüden çıkartamadım.Üstünde durmam gereken başka iler var bunla takılı kalamam :P ... 
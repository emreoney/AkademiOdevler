


dersSayisi = int(input("Ders Sayisi: "))
kalanDers = 0
gecilenDers = 0

gecilenDersler = []
kalanDersler = []



for i in range(dersSayisi):
    print(f"{i+1}. ders Sinav Sonuclari")
    vizeNot = float(input("Vize Notu: "))
    finalNot = float(input("Final Not: "))
    ortalama = (vizeNot*0.4 + finalNot*0.6)
    if(ortalama<50):
        kalanDers+=1
        kalanDersler.append(ortalama)
    else:
        gecilenDers+=1
        gecilenDersler.append(ortalama)

print(f"Toplam Geçilen Ders: {gecilenDers} , Toplam Kalinan Ders: {kalanDers}")
print(f"Geçilen Derslerin Ortalamasi: {gecilenDersler} , Kalan Derslerin Ortalamasi: {kalanDersler}")


        



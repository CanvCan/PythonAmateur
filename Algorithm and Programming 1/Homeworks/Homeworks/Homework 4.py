brut = int(input('Lütfen maaşınızın brüt halini giriniz '))

sayac_dusuk = 0

sayac_orta = 0

sayac_yuksek = 0

sayac_ellibin = 0

top_vergi = 0

top_net_maas = 0

top_brut = 0

kisi_sayi = 0

vergi_oran = 0
# döngü


while brut != 0:

    if brut <= 10000:

        vergi_oran = 15

        sayac_dusuk += 1

    elif 10000 < brut < 25000:

        vergi_oran = 20

        sayac_orta += 1

    elif 25000 <= brut <= 50000:

        vergi_oran = 25

        sayac_yuksek += 1

    elif brut > 50000:

        sayac_yuksek += 1

        sayac_ellibin += 1

    kisi_sayi += 1

    net = brut - (brut * vergi_oran / 100)

    vergi = brut - net

    top_net_maas += net

    top_brut += brut

    top_vergi += vergi

    print('net maaşınız: ', net)

    print('devlete ödeyeceğiniz gelir vergisi miktarı: ', vergi)

    brut = int(input('lütfen maaşınızın brüt halini giriniz '))

# çıktılar

print('brüt maaş miktarı düşük seviyede olan satış temsilcisi sayısı: ', sayac_dusuk)

print('brüt maaş miktarı orta seviyede olan satış temsilcisi sayısı: ', sayac_orta)

print('brüt maaş miktarı yüksek seviyede olan satış temsilcisi sayısı: ', sayac_yuksek)

# hesaplamalı değişkenler


oran_1 = sayac_ellibin / sayac_yuksek * 100

oran_2 = top_net_maas / kisi_sayı

oran_3 = top_vergi / top_brut * 100

print(
    f"brüt maaş miktarı 50.000 TL üzerinde olan satış temsilcilerinin, brüt maaş miktarı yüksek seviyede olan satış temsilcisi içindeki yüzdesi: %{oran_1:,.2f}")

print(f"tüm satış temsilcilerinin net maaş tutarlarının ortalaması: {oran_2:,.2f}")

print(f"devlete ödenecek toplam vergi miktarı: {top_vergi:,.2f}", 've',
      f"devlete ödenen toplam vergi miktarının toplam brüt maaş içindeki oranı: %{oran_3:,.2f}")

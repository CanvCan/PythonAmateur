"""Girilen bilye ağırlıklarının birbirine göre karşılaştırılması ve farklı olan bilyenin bulunmasını sağlayan
algoritma şu şekilde kurulmuştur:
1. İlk olarak alınan ilk üç değer c,k ve z adlı üç değişkene atanmıştır.
2. Daha sonra bu değişkenler kendi aralarında karşılaştırılarak farklı olan değerler(dif_value1, dif_value2 vb.) ve olmayan
değerler (base_value4, base_value1 vb.) bulunmuştur.
3. Ağırlık farkı ve yüzdesi gibi diğer değerler bulunmuştur.

* "#print('......')" şeklindeki commentler olası bir hata durumunda hata tespitini kolaylaştırmak için konmuştur.
(yazar burada kodu okuyanın kendisi gibi debugging bilmediğini varsaymaktadır :)

"""

cevap_v1 = 'e'
cevap_v2 = 0
cevap_v3 = 0
yanlis = 0
print_onay = True
value = 0
iade_kutu_sayi = 0
top_kutu_sayi = 0
iade_kutu_sayi_yuzde = 0
iade_bilye_sayi = 0
kabul_bilye_sayi = 0
top_bilye_sayi = 0
esit_kutu_sayi = 0
agir_kutu_sayi = 0
hafif_kutu_sayi = 0
top_agirlik_farki_agir = 0
top_agirlik_farki_hafif = 0
top_agirlik_yuzde_agir = 0
top_agirlik_yuzde_hafif = 0
max_bilye_sayi_esit_kutu = 0
max_bilye_agirlik_esit_kutu = 0
max_agirlik_fark = 0
min_agirlik_fark = 10000

while cevap_v1 == 'e' or cevap_v1 == 'E':
    kutu_bilye_sayi = int(input('Lütfen kutuda bulunan bilye sayısını giriniz (gireceğiniz değer ondan küçük '
                                'olmamalıdır): '))
    while kutu_bilye_sayi < 10:
        kutu_bilye_sayi = int(input('Lütfen kutuda bulunan bilye sayısını ondan küçük olmayacak şekilde giriniz: '))
    top_bilye_sayi += kutu_bilye_sayi
    for i in range(1, kutu_bilye_sayi + 1):
        bilye_agirlik = int(input('Lütfen bilyenin ağırlığını giriniz (gireceğiniz değer sıfırdan büyük ve mg '
                                  'biriminde olmalıdır): '))
        while bilye_agirlik <= 0:
            bilye_agirlik = int(input('Lütfen bilyenin ağırlığını giriniz (gireceğiniz değer sıfırdan büyük ve mg '
                                      'biriminde olmalıdır): '))
        if i == 1:
            c = bilye_agirlik  # ilk girdiye atanan sabit
        if i == 2:
            k = bilye_agirlik  # ikinci girdiye atanan sabit
        if i == 3:
            z = bilye_agirlik  # üçüncü girdiye atanan sabit, ve ilk üç girdiyi aldıktan sonra ilk üç girdiyi kendi
            # arasında karşılaştıran ve dif_value ve base_value belirleyen birinci kısım algoritma
            if c == k and k == z:
                base_value1 = c
            elif c == k and c != z:
                base_value2 = c
                yanlis += 1
                dif_value2 = z
                if dif_value2 > c:
                    value = 'ağırdır.'
                else:
                    value = 'hafiftir.'
                agirlik_fark = abs(c - z)
                agirlik_yuzde = (agirlik_fark / base_value2) * 100
            #   print('base_value2',yanlis)
            elif c == z and c != k:
                base_value3 = z
                yanlis += 1
                dif_value3 = k
                if dif_value3 > c:
                    value = 'ağırdır.'
                else:
                    value = 'hafiftir.'
                agirlik_fark = abs(c - k)
                agirlik_yuzde = (agirlik_fark / base_value3) * 100
            #   print('base_value3',yanlis)
            elif k == z and k != c:
                base_value4 = k
                yanlis += 1
                dif_value4 = c
                if dif_value4 > k:
                    value = 'ağırdır.'
                else:
                    value = 'hafiftir.'
                agirlik_fark = abs(k - c)
                agirlik_yuzde = (agirlik_fark / base_value4) * 100
            #   print('base_value4',yanlis)
            elif c != k and c != z and k != z:
                print('Kutu iade edilecektir... ')
                cevap_v2 = 1
                iade_kutu_sayi += 1
                iade_bilye_sayi += kutu_bilye_sayi

        if cevap_v2 == 1:
            break

        if i > 3:  # ilk üç girdiden sonra girilen diğer değerleri ilk üç girdide belirlenen dif_value ve base_value
            # değerlerine göre karşılaştıran ve yanlış sayısına göre for döngüsünden çıkan veya çıkmayan ikinci kısım
            # kod
            if c == k and k == z and base_value1 != bilye_agirlik:
                yanlis += \
                    1
                dif_value1 = bilye_agirlik
                if dif_value1 > c:
                    value = 'ağırdır.'
                else:
                    value = 'hafiftir.'
                agirlik_fark = abs(c - bilye_agirlik)
                agirlik_yuzde = (agirlik_fark / base_value1) * 100
                # print('base_value1 v2',yanlis)
            elif c == k and c != z and base_value2 != bilye_agirlik:
                yanlis += 1
                # print('base_value2 v2',yanlis)
            elif c == z and c != k and base_value3 != bilye_agirlik:
                yanlis += 1
                # print('base_value3 v2',yanlis)
            elif k == z and k != c and base_value4 != bilye_agirlik:
                yanlis += 1
                # print('base_value4 v2',yanlis)
            if yanlis > 1:
                print('Kutu iade edilecektir... ')
                cevap_v3 = 1
                iade_kutu_sayi += 1
                iade_bilye_sayi += kutu_bilye_sayi
        if cevap_v3 == 1:
            break
        if i == kutu_bilye_sayi:  # for döngüsü bitiminde istenen ilk birkaç çıktı için boolean tipi değişkenlerle
            # kontrol edilerek yazdırılacak olan ilk kısım print
            if value != 0:
                print_onay = False
            if print_onay:
                print('Tüm bilyeler eşit ağırlıktadır. ')
                esit_kutu_sayi += 1  # en çok bilye olan kutudaki bilye sayısı ve ağırlığı ile en ağır bilye olan
                # kutudaki bilye sayısı ve ağırlığını hesaplayan üçüncü kısım kod
                bilye_sayi_esit_kutu = kutu_bilye_sayi
                bilye_agirlik_esit_kutu = bilye_agirlik
                if bilye_sayi_esit_kutu > max_bilye_sayi_esit_kutu:
                    max_bilye_sayi_esit_kutu = bilye_sayi_esit_kutu
                    cok_bilye_agirlik_esit_kutu = bilye_agirlik_esit_kutu
                if bilye_agirlik_esit_kutu > max_bilye_agirlik_esit_kutu:
                    max_bilye_agirlik_esit_kutu = bilye_agirlik_esit_kutu
                    agir_bilye_sayi_esit_kutu = bilye_sayi_esit_kutu
                break
            print_onay = True  # değişkenleri ilk haline çevirme 1

            if value != 0:  # diğer birtakım istenen çıktılar için hesaplamalar yapan dördüncü kısım kod
                if value == 'ağırdır.':
                    agir_kutu_sayi += 1
                    top_agirlik_farki_agir += agirlik_fark
                    top_agirlik_yuzde_agir += agirlik_yuzde
                elif value == 'hafiftir.':
                    hafif_kutu_sayi += 1
                    top_agirlik_farki_hafif += agirlik_fark
                    top_agirlik_yuzde_hafif += agirlik_yuzde
                    # for döngüsü sonunda istenen birtakım çıktılar için yazdırılacak olan ikinci kısım printler
                print('Farklı ağırlıktaki bilye diğer bilyelerden', value)
                print('Farklı olan bilyenin ağırlık farkı değeri: ', agirlik_fark, f"ve yüzdesi: %{agirlik_yuzde:,.2f}")

                # diğer birtakım istenen çıktılar için hesaplamalar yapan beşinci kısım kod
                if agirlik_fark > max_agirlik_fark:
                    max_agirlik_fark = agirlik_fark
                    max_agirlik_yuzde = agirlik_yuzde
                    if value == 'ağırdır.':
                        isaret1 = '+ (ağırdır)'
                    else:
                        isaret1 = '- (hafiftir)'

                if agirlik_fark < min_agirlik_fark:
                    min_agirlik_fark = agirlik_fark
                    min_agirlik_yuzde = agirlik_yuzde
                    if value == 'ağırdır.':
                        isaret2 = '+ (ağırdır)'
                    else:
                        isaret2 = '- (hafiftir)'

    # değişkenleri ilk haline çevirme 2
    value = 0
    yanlis = 0
    cevap_v2 = 0
    cevap_v3 = 0
    top_kutu_sayi += 1
    kabul_bilye_sayi = top_bilye_sayi - iade_bilye_sayi
    cevap_v1 = input('Başka kutu var mı ? [e/E/h/H]: ')

# while döngüsünden çıkıp istenen son çıktılar için hesaplamalar yapan ve print ile yazdıran son kısım kod
iade_kutu_sayi_yuzde = (iade_kutu_sayi / top_kutu_sayi) * 100
kabul_kutu_sayi = top_kutu_sayi - iade_kutu_sayi
esit_kutu_sayi_yuzde = (esit_kutu_sayi / kabul_kutu_sayi) * 100
agir_kutu_sayi_yuzde = (agir_kutu_sayi / kabul_kutu_sayi) * 100
hafif_kutu_sayi_yuzde = (hafif_kutu_sayi / kabul_kutu_sayi) * 100
agirlik_farki_ortalama_agir = top_agirlik_farki_agir / agir_kutu_sayi
agirlik_farki_ortalama_hafif = top_agirlik_farki_hafif / hafif_kutu_sayi
agirlik_yuzde_ortalama_agir = top_agirlik_yuzde_agir / agir_kutu_sayi
agirlik_yuzde_ortalama_hafif = top_agirlik_yuzde_hafif / hafif_kutu_sayi

print('İade edilen kutu sayısı: ', iade_kutu_sayi,
      f"ve toplam kutu sayısı içerisindeki yüzdesi: %{iade_kutu_sayi_yuzde:,.2f}")
print('\n')
print('İade edilen bilye sayısı: ', iade_bilye_sayi, 've kabul edilen bilye sayısı: ', kabul_bilye_sayi)
print('\n')
print('İçindeki bilyelerin ağırlığı eşit olan kutu sayısı: ', esit_kutu_sayi,
      f"ve üretim hatasız kutular arasındaki yüzdesi: %{esit_kutu_sayi_yuzde:,.2f}")
print('\n')
print('İçindeki bilyelerden biri ağır olan kutu sayısı: ', agir_kutu_sayi,
      f"ve üretim hatasız kutular arasındaki yüzdesi: %{agir_kutu_sayi_yuzde:,.2f}")
print('\n')
print('İçindeki bilyelerden biri hafif olan kutu sayısı: ', hafif_kutu_sayi,
      f"ve üretim hatasız kutular arasındaki yüzdesi: %{hafif_kutu_sayi_yuzde:,.2f}")
print('\n')
print(
    f"Farklı bilyenin diğerlerinden ağır olduğu kutulardaki ağırlık farkı ortalaması: {agirlik_farki_ortalama_agir:,.2f}"
    f" ve ağırlık farkı yüzdesini ortalaması: %{agirlik_yuzde_ortalama_agir:,.2f}")
print('\n')
print(
    f"Farklı bilyenin diğerlerinden hafif olduğu kutulardaki ağırlık farkı ortalaması: {agirlik_farki_ortalama_hafif:,.2f} "
    f"ve ağırlık farkı yüzdesini ortalaması: %{agirlik_yuzde_ortalama_hafif:,.2f}")
print('\n')
print('Tüm bilyelerin eşit ağırlıkta olduğu kutular arasından bilye sayısı en çok olan kutudaki bilye sayısı: ',
      max_bilye_sayi_esit_kutu, 've bu kutudaki bir bilyenin ağırlığı: ', cok_bilye_agirlik_esit_kutu)
print('\n')
print('Tüm bilyelerin eşit ağırlıkta olduğu kutular arasından içinde en ağır bilye olan kutudaki bilye sayısı: ',
      agir_bilye_sayi_esit_kutu, ' ve bu kutudaki bir bilyenin ağırlığı: ', max_bilye_agirlik_esit_kutu)
print('\n')
print('Ağırlık farkı değerinin en büyük olduğu değer: ', max_agirlik_fark, f"yüzdesi: %{max_agirlik_yuzde:,.2f}",
      'işareti: ', isaret1)
print('\n')
print('Ağırlık farkı değerinin en küçük olduğu değer: ', min_agirlik_fark, f"yüzdesi: %{min_agirlik_yuzde:,.2f}",
      'işareti: ', isaret2)

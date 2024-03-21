"""
Buna göre, kullanıcıdan yarışmaya katılan sporcu sayısını, her sporcunun ad-soyad bilgisini,
sıralama atışlarında verilecek atış hakkı (atış turu) sayısını ve sporcuların atış turlarında yaptıkları
her atışta elde ettikleri puanları (10 puan ise ayrıca X bölgesine isabet edip etmediğini (e/h)) alan ve
sıralama atışları sonucunda oluşan sıralamayı aşağıdakine benzer şekilde ekrana yazdıran bir
algoritma ve program yazınız.

"""


def istatistikler(sporcu_sayi, atis_hakki, ad_soyad_list, puan_list, on_list, x_list):
    for yarismaci_sira in range(sporcu_sayi):
        ad_soyad = input('Lütfen ad ve soyadınızı giriniz: ')
        ad_soyad_list.append(ad_soyad)

    for atis in range(atis_hakki):
        for yarismaci_sira in range(sporcu_sayi):
            puan = int(input('Lütfen aldığınız puanı giriniz: '))
            puan_list[yarismaci_sira] += puan
            if puan == 10:
                on_list[yarismaci_sira] += 1
                x = input('Atışınız X bölgesine isabet etti mi? [e,E,h,H]')
                if x in ['e', 'E']:
                    x_list[yarismaci_sira] += 1


def yazdir(sporcu_sayi, ad_soyad_list, puan_list, on_list, x_list):
    print('Sıra Ad-Soyad          Puan    10 Sayısı    X Sayısı')
    print('.... ........          ....    .........    ........')
    print()

    for sira in range(sporcu_sayi + 1):

        max_puan_sira = 0
        for yarismaci_sira in range(1, sporcu_sayi):

            if puan_list[yarismaci_sira] > puan_list[max_puan_sira]:
                max_puan_sira = yarismaci_sira

            elif puan_list[yarismaci_sira] == puan_list[max_puan_sira]:

                if on_list[yarismaci_sira] > on_list[max_puan_sira]:
                    max_puan_sira = yarismaci_sira

                elif on_list[yarismaci_sira] == on_list[max_puan_sira]:

                    if x_list[yarismaci_sira] > x_list[max_puan_sira]:
                        max_puan_sira = yarismaci_sira

        print(
            f"{sira:4^}        {ad_soyad_list[max_puan_sira]:8}     {puan_list[max_puan_sira]:4} {on_list[max_puan_sira]:9}    {x_list[max_puan_sira]:8}")
        puan_list[max_puan_sira] = -1


def main():
    sporcu_sayi = int(input('Lütfen sporcu sayısını giriniz: '))
    while sporcu_sayi < 8:
        sporcu_sayi = int(input('Lütfen sporcu sayısını sekizden az olmayacak şekilde giriniz: '))

    atis_hakki = int(input('Lütfen atış hakkı sayısını giriniz: '))
    while atis_hakki < 1:
        atis_hakki = int(input('Lütfen atış hakkı sayısını birden küçük olmayacak şekilde giriniz: '))

    ad_soyad_list = []
    puan_list = [0] * sporcu_sayi
    on_list = [0] * sporcu_sayi
    x_list = [0] * sporcu_sayi

    istatistikler(sporcu_sayi, atis_hakki, ad_soyad_list, puan_list, on_list, x_list)
    yazdir(sporcu_sayi, ad_soyad_list, puan_list, on_list, x_list)


main()

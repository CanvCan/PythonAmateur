"""
Buna göre, kullanıcıdan yarışmaya katılan okçu sayısını, okçulara verilecek atış hakkı (atış turu)
sayısını ve okçuların atış turlarında yaptıkları her atışta elde ettikleri puanları (ıska ise ayrıca o
sırada esen rüzgarın adını (Yıldız, Poyraz, Gündoğusu, Keşişleme, Kıble, Lodos, Günbatısı,
Karayel)) alan ve yarışma sonucunda her okçunun yaptığı atışların puanlara göre sayısal dağılımını
(adet) ve elde ettiği toplam puanı, tüm okçuların yaptıkları atışların puanlara göre oransal dağılımını
(%), ayrıca da tüm ıska atışların rüzgar türlerine göre oransal dağılımını (%) bulan ve aşağıdakine
benzer şekilde ekrana yazdıran bir algoritma ve program yazınız.
"""


def istatistikler(okcu_sayi, atis_hakki, sira_no, sira_list, puan_dict, ruzgar_dict, puan_list1, puan_list2,
                  toplam_puan_list, a, b, toplam_tekil, toplam_tekil_yuzde, puan_dict2, ruzgar_dict2):
    try:
        for okcu in range(okcu_sayi):
            for atis in range(atis_hakki):
                puan = int(input('Lütfen puanınızı giriniz: '))
                puan_dict[puan] += 1
                puan_dict2[puan] += 1
                if puan == 0:
                    ruzgar_ad = input('Lütfen rüzgar adını giriniz (baş harfin büyük olmasına dikkat ediniz): ')
                    ruzgar_dict[ruzgar_ad] += 1
                    ruzgar_dict2[ruzgar_ad] += 1

            sira_no += 1
            sira_list.append(sira_no)
            puan_list1 += list(puan_dict.values())
            puan_list2 += list(puan_dict.keys())
            toplam_puan = 0
            c = puan_list1[a:b]
            k = puan_list2[a:b]
            for i in range(11):
                x = c[i] * k[i]
                toplam_puan += x

            toplam_puan_list.append(toplam_puan)
            a += 11
            b += 11

            puan_dict = {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
            ruzgar_dict = {"Yıldız": 0, "Poyraz": 0, "Gündoğusu": 0, "Keşişleme": 0, "Kıble": 0, "Lodos": 0,
                           "Günbatısı": 0, "Karayel": 0}

        for j in range(11):
            toplam_tekil[j] += puan_dict2[j]

        toplam_tum_tekil = sum(puan_dict2.values())

        for h in range(11):
            toplam_tekil_yuzde[h] += (toplam_tekil[h] / toplam_tum_tekil) * 100

    except IndexError as error:
        print(error)
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyError as error:
        print(error)
    except:
        print('Bilinmeyen bir hata oluştu.')


def yazdir(ruzgar_dict2, puan_list1, okcu_sayi, sira_list, toplam_puan_list, c, k, toplam_tekil_yuzde):
    try:
        toplam_tekil_yuzde.reverse()
        round_list = [round(item, 2) for item in toplam_tekil_yuzde]
        ruzgar_list = list(ruzgar_dict2.values())
        toplam_ruzgar_sayi = sum(ruzgar_dict2.values())
        iska_oran_list = [0] * 8
        ruzgar_ad_list = ["Yıldız", "Poyraz", "Gündoğusu", "Keşişleme", "Kıble", "Lodos", "Günbatısı", "Karayel"]
        for i in range(8):
            iska_oran_list[i] = (ruzgar_list[i] / toplam_ruzgar_sayi) * 100

        print("Okçu Kayıt No.  10p    9p    8p    7p    6p    5p    4p    3p    2p    1p    0p   Toplam Puan")
        print("--------------  ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   -----------")
        for veri in range(okcu_sayi):
            print(f" {sira_list[veri]:^13}", end="  ")
            print(f" {'     '.join(str(x) for x in puan_list1[c:k]):^48}", end="   ")
            print(f" {toplam_puan_list[veri]:^11}")
            c += 11
            k += 11
        print(f"Tüm Okçular(%) {'  '.join(str(x) for x in round_list):}")

        print()
        print("Rüzgar Adı     Iska Atış Oranı")
        print("----------     ---------------")
        for ad_oran in range(8):
            print(f" {ruzgar_ad_list[ad_oran]:^10} {iska_oran_list[ad_oran]:^20,.2f}")

    except TypeError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)
    except:
        print('Bilinmeyen bir hata oluştu.')


def main():
    try:
        okcu_sayi = int(input('Lütfen yarışmaya katılan okçu sayısını giriniz: '))
        atis_hakki = int(input('Lütfen okçuların atış hakkını giriniz giriniz: '))

        puan_dict = {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
        ruzgar_dict = {"Yıldız": 0, "Poyraz": 0, "Gündoğusu": 0, "Keşişleme": 0, "Kıble": 0, "Lodos": 0, "Günbatısı": 0,
                       "Karayel": 0}
        puan_dict2 = {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
        ruzgar_dict2 = {"Yıldız": 0, "Poyraz": 0, "Gündoğusu": 0, "Keşişleme": 0, "Kıble": 0, "Lodos": 0,
                        "Günbatısı": 0,
                        "Karayel": 0}

        puan_list1 = []
        puan_list2 = []
        toplam_puan_list = []
        toplam_tekil = [0] * 11
        toplam_tekil_yuzde = [0] * 11
        sira_no = 0
        sira_list = []

        a = 0
        b = 11
        c = 0
        k = 11

        istatistikler(okcu_sayi, atis_hakki, sira_no, sira_list, puan_dict, ruzgar_dict, puan_list1, puan_list2,
                      toplam_puan_list, a, b,
                      toplam_tekil, toplam_tekil_yuzde, puan_dict2, ruzgar_dict2)

        yazdir(ruzgar_dict2, puan_list1, okcu_sayi, sira_list, toplam_puan_list, c, k, toplam_tekil_yuzde)

    except ValueError as error:
        print(error)


main()

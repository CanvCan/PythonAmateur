def yazdir(oyun_boyutu, board_list, harf_list, sayi_list):  # bu fonksiyon oyun tahtasını yazdırmaya yarar.

    for a in range(oyun_boyutu):
        print(f"   {harf_list[a]} ", end="")

    print()
    print(f"  {'-' * (oyun_boyutu * 4 + 1)}")

    for b in range(oyun_boyutu):
        print(sayi_list[b], end=" ")
        for c in range(oyun_boyutu):
            print(f"{'|'}", end=" ")
            print(board_list[b][c], end=" ")

        print(f"{'|'}", end=" ")
        print(sayi_list[b], end=" ")
        print()
        print(f"  {'-' * (oyun_boyutu * 4 + 1)}")

    for c in range(oyun_boyutu):
        print(f"   {harf_list[c]} ", end="")
    print()


def yer_degistir(oyuncu_karakter1, oyuncu_karakter2, oyun_boyutu, board_list, harf_list, sayi_list,
                 harf_dict):  # bu fonksiyon oyuncu hamlelerini gerçekleştirir.

    sira = 1
    cevap = "E"
    while cevap == "E":
        if sira == 1:
            print(f"Sıra oyuncu {oyuncu_karakter1}'de, lütfen oynayınız")
            karakter = oyuncu_karakter1
        else:
            print(f"Sıra oyuncu {oyuncu_karakter2}'de, lütfen oynayınız")
            karakter = oyuncu_karakter2
            sira = 0

        konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
        konum_list = konum.split()
        mevcut_sayi = int(konum_list[0][0])
        mevcut_harf = konum_list[0][1]
        hedef_sayi = int(konum_list[1][0])
        hedef_harf = konum_list[1][1]

        hata_yaz(sira, board_list, harf_dict, oyuncu_karakter1, oyuncu_karakter2, konum_list, mevcut_sayi, mevcut_harf,
                 hedef_sayi, hedef_harf)

        board_list[hedef_sayi - 1][harf_dict[hedef_harf]] = karakter
        board_list[mevcut_sayi - 1][harf_dict[mevcut_harf]] = " "

        eleme(hedef_sayi, hedef_harf, board_list, harf_dict, oyun_boyutu)
        eleme_kose(board_list, oyun_boyutu, harf_list)
        yazdir(oyun_boyutu, board_list, harf_list, sayi_list)
        # sayac_1 = 0
        # sayac_2 = 0
        #
        # for i in range(oyun_boyutu):
        #     for j in range(oyun_boyutu):
        #         if board_list[i][j] != " ":
        #             if oyuncu_karakter1 == board_list[i][j]:
        #                 sayac_1 += 1
        #             if oyuncu_karakter2 == board_list[i][j]:
        #                 sayac_2 += 1
        #
        # if sayac_1 != 0 and sayac_2 < 2:
        #     print(f"Kazanan oyuncu {oyuncu_karakter1}")
        #     cevap = input("Tekrar oynamak ister misiniz? [E/H] ")
        # if sayac_2 != 0 and sayac_1 < 2:
        #     print(f"Kazanan oyuncu {oyuncu_karakter2}")
        #     cevap = input("Tekrar oynamak ister misiniz? [E/H] ")

        kazanan_belirleme(board_list, oyun_boyutu, oyuncu_karakter1, oyuncu_karakter2)
        konum_list.clear()
        sira += 1


def eleme(hedef_sayi, hedef_harf, board_list, harf_dict,
          oyun_boyutu):  # bu fonksiyon oyuncu hamlelerine göre taş kilitleme işlevini yapar.

    base_main = board_list[hedef_sayi - 1][harf_dict[hedef_harf]]
    ust = True
    alt = True
    sol = True
    sag = True

    if oyun_boyutu - hedef_sayi in [0, 1]:
        alt = False
    if hedef_sayi - 1 in [0, 1]:
        ust = False
    if harf_dict[hedef_harf] in [0, 1]:
        sol = False
    if (oyun_boyutu - 1) - harf_dict[hedef_harf] in [0, 1]:
        sag = False

    if ust:
        base_dikey_ust = board_list[hedef_sayi - 2][harf_dict[hedef_harf]]
        scope_du = board_list[hedef_sayi - 3][harf_dict[hedef_harf]]
        if scope_du == base_main and base_dikey_ust != base_main:
            board_list[hedef_sayi - 2][harf_dict[hedef_harf]] = " "
            info = str(hedef_sayi - 1) + str(hedef_harf)
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if alt:
        base_dikey_alt = board_list[hedef_sayi][harf_dict[hedef_harf]]
        scope_da = board_list[hedef_sayi + 1][harf_dict[hedef_harf]]
        if scope_da == base_main and base_dikey_alt != base_main:
            board_list[hedef_sayi][harf_dict[hedef_harf]] = " "
            info = str(hedef_sayi + 1) + str(hedef_harf)
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if sol:
        base_yatay_sol = board_list[hedef_sayi - 1][harf_dict[hedef_harf] - 1]
        scope_yso = board_list[hedef_sayi - 1][harf_dict[hedef_harf] - 2]
        if scope_yso == base_main and base_yatay_sol != base_main:
            board_list[hedef_sayi - 1][harf_dict[hedef_harf] - 1] = " "
            info = str(hedef_sayi) + str(hedef_harf)
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if sag:
        base_yatay_sag = board_list[hedef_sayi - 1][harf_dict[hedef_harf] + 1]
        scope_ysa = board_list[hedef_sayi - 1][harf_dict[hedef_harf] + 2]
        if scope_ysa == base_main and base_yatay_sag != base_main:
            board_list[hedef_sayi - 1][harf_dict[hedef_harf] + 1] = " "
            info = str(hedef_sayi) + str(hedef_harf)
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")


def eleme_kose(board_list, oyun_boyutu,
               harf_list):  # bu fonksiyon oyuncu hamlelerine göre köşelerdeki taş kilitleme işlevlerini yapar.

    if board_list[0][0] != " ":
        main_cha = board_list[0][0]
        sag_cha = board_list[0][1]
        alt_cha = board_list[1][0]
        if sag_cha == alt_cha and sag_cha != " " and alt_cha != " " and sag_cha != main_cha:
            board_list[0][0] = " "
            info = "1A"
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if board_list[oyun_boyutu - 1][0] != " ":
        main_cha = board_list[oyun_boyutu - 1][0]
        sol_cha = board_list[oyun_boyutu - 1][1]
        ust_cha = board_list[oyun_boyutu - 2][0]
        if sol_cha == ust_cha and sol_cha != " " and ust_cha != " " and sol_cha != main_cha:
            board_list[oyun_boyutu - 1][0] = " "
            info = str(oyun_boyutu) + "A"
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if board_list[0][oyun_boyutu - 1] != " ":
        main_cha = board_list[0][oyun_boyutu - 1]
        sol_cha = board_list[0][oyun_boyutu - 2]
        alt_cha = board_list[1][oyun_boyutu - 1]
        if sol_cha == alt_cha and sol_cha != " " and alt_cha != " " and sol_cha != main_cha:
            board_list[0][oyun_boyutu - 1] = " "
            info = "1" + str(harf_list[oyun_boyutu - 1])
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if board_list[oyun_boyutu - 1][oyun_boyutu - 1] != " ":
        main_cha = board_list[oyun_boyutu - 1][oyun_boyutu - 1]
        sag_cha = board_list[oyun_boyutu - 1][oyun_boyutu - 2]
        ust_cha = board_list[oyun_boyutu - 2][oyun_boyutu - 1]
        if sag_cha == ust_cha and sag_cha != " " and ust_cha != " " and sag_cha != main_cha:
            board_list[oyun_boyutu - 1][oyun_boyutu - 1] = " "
            info = str(oyun_boyutu) + str(harf_list[oyun_boyutu - 1])
            print(f"{info} konumundaki taş kilitlendi ve dışarı çıkarıldı.")


def kazanan_belirleme(board_list, oyun_boyutu, oyuncu_karakter1, oyuncu_karakter2):  # bu fonksiyon kazananı belirler.

    sayac_1 = 0
    sayac_2 = 0

    for i in range(oyun_boyutu):
        for j in range(oyun_boyutu):
            if board_list[i][j] != " ":
                if oyuncu_karakter1 == board_list[i][j]:
                    sayac_1 += 1
                if oyuncu_karakter2 == board_list[i][j]:
                    sayac_2 += 1

    if sayac_1 != 0 and sayac_2 < 2:
        print(f"Kazanan oyuncu {oyuncu_karakter1}")
        cevap = input("Tekrar oynamak ister misiniz? [E/H] ")
    if sayac_2 != 0 and sayac_1 < 2:
        print(f"Kazanan oyuncu {oyuncu_karakter2}")
        cevap = input("Tekrar oynamak ister misiniz? [E/H] ")


def hata_yaz(sira, board_list, harf_dict, oyuncu_karakter1, oyuncu_karakter2, konum_list, mevcut_sayi, mevcut_harf,
             hedef_sayi, hedef_harf):  # bu fonksiyon oluşabilecek birtakım hataları düzenler.

    control_2 = True
    control_3 = True
    control_4 = False
    while control_3:
        if sira == 1:
            while board_list[mevcut_sayi - 1][harf_dict[mevcut_harf]] != oyuncu_karakter1:
                info = "Rakibinizin taşları ile oynayamazsınız !!!"
                if board_list[mevcut_sayi - 1][harf_dict[mevcut_harf]] == " ":
                    info = "Boş alan seçemezsiniz !!!"
                print(f"{info}")
                konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
                konum_list = konum.split()
                mevcut_sayi = int(konum_list[0][0])
                mevcut_harf = konum_list[0][1]
                hedef_sayi = int(konum_list[1][0])
                hedef_harf = konum_list[1][1]
                control_4 = True
        else:
            while board_list[mevcut_sayi - 1][harf_dict[mevcut_harf]] != oyuncu_karakter2:
                print("Rakibinizin taşları ile oynayamazsınız !!!")
                konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
                konum_list = konum.split()
                mevcut_sayi = int(konum_list[0][0])
                mevcut_harf = konum_list[0][1]
                hedef_sayi = int(konum_list[1][0])
                hedef_harf = konum_list[1][1]
                control_4 = True

        if konum_list[0] == konum_list[1]:
            print("Lütfen hedef konumunuzu bulunduğunuz konumdan farklı seçiniz !!!")
            konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
            konum_list = konum.split()
            mevcut_sayi = int(konum_list[0][0])
            mevcut_harf = konum_list[0][1]
            hedef_sayi = int(konum_list[1][0])
            hedef_harf = konum_list[1][1]
            control_4 = True

        if board_list[hedef_sayi - 1][harf_dict[hedef_harf]] != " ":
            konum = input(
                "Hareket edeceğiniz konum boş olmalıdır, lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
            konum_list = konum.split()
            mevcut_sayi = int(konum_list[0][0])
            mevcut_harf = konum_list[0][1]
            hedef_sayi = int(konum_list[1][0])
            hedef_harf = konum_list[1][1]
            control_4 = True

        if mevcut_harf != hedef_harf and mevcut_sayi != hedef_sayi:
            print("Lütfen oyunun taş hareket ettirme kurallarına uyunuz !!!")
            konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
            konum_list = konum.split()
            mevcut_sayi = int(konum_list[0][0])
            mevcut_harf = konum_list[0][1]
            hedef_sayi = int(konum_list[1][0])
            hedef_harf = konum_list[1][1]
            control_4 = True

        if mevcut_sayi == hedef_sayi and control_2:
            if harf_dict[mevcut_harf] + 1 < harf_dict[hedef_harf]:
                for i in range(harf_dict[hedef_harf] + 1, harf_dict[mevcut_harf]):
                    while board_list[mevcut_sayi - 1][i] != " ":
                        print("Başka bir taşın üzerinden atlayamazsınız !!!")
                        konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
                        konum_list = konum.split()
                        mevcut_sayi = int(konum_list[0][0])
                        mevcut_harf = konum_list[0][1]
                        hedef_sayi = int(konum_list[1][0])
                        hedef_harf = konum_list[1][1]
                        control_4 = True
                control_2 = False

            else:
                for i in range(harf_dict[mevcut_harf], harf_dict[hedef_harf] + 1):
                    while board_list[mevcut_sayi - 1][i] != " ":
                        print("Başka bir taşın üzerinden atlayamazsınız !!!")
                        konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
                        konum_list = konum.split()
                        mevcut_sayi = int(konum_list[0][0])
                        mevcut_harf = konum_list[0][1]
                        hedef_sayi = int(konum_list[1][0])
                        hedef_harf = konum_list[1][1]
                        control_4 = True
                control_2 = False

        if mevcut_harf == hedef_harf and control_2:
            if mevcut_sayi < (hedef_sayi - 1):
                for i in range(mevcut_sayi, hedef_sayi - 1):
                    while board_list[i][harf_dict[mevcut_harf]] != " ":
                        print("Başka bir taşın üzerinden atlayamazsınız !!!")
                        konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
                        konum_list = konum.split()
                        mevcut_sayi = int(konum_list[0][0])
                        mevcut_harf = konum_list[0][1]
                        hedef_sayi = int(konum_list[1][0])
                        hedef_harf = konum_list[1][1]
                        control_4 = True
                control_2 = False

            else:
                for i in range(hedef_sayi + 1, mevcut_sayi):
                    while board_list[i - 1][harf_dict[mevcut_harf]] != " ":
                        print("Başka bir taşın üzerinden atlayamazsınız !!!")
                        konum = input("Lütfen mevcut konumunuzu ve geçmek istediğininiz konumu giriniz: ").upper()
                        konum_list = konum.split()
                        mevcut_sayi = int(konum_list[0][0])
                        mevcut_harf = konum_list[0][1]
                        hedef_sayi = int(konum_list[1][0])
                        hedef_harf = konum_list[1][1]
                        control_4 = True
                control_2 = False

            if not control_4:
                control_3 = False


def main():
    try:
        board_list = []
        harf_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        sayi_list = [1, 2, 3, 4, 5, 6, 7, 8]
        harf_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

        oyun_boyutu = int(input("Lütfen oyun boyutunu giriniz [4-8]: "))
        while oyun_boyutu not in range(4, 8):
            oyun_boyutu = int(input("Lütfen oyun boyutunu aralıkta giriniz !!!  [4-8]: "))

        oyuncu_karakter1 = input("Lütfen kullanacağınız karakteri seçiniz (tek karakter): ")
        while len(oyuncu_karakter1) != 1:
            print("Lütfen tek karakter giriniz !!!")
            oyuncu_karakter1 = input("Lütfen kullanacağınız karakteri seçiniz (tek karakter): ")

        oyuncu_karakter2 = input("Lütfen kullanacağınız karakteri seçiniz (tek karakter): ")
        while len(oyuncu_karakter2) != 1:
            print("Lütfen tek karakter giriniz !!!")
            oyuncu_karakter2 = input("Lütfen kullanacağınız karakteri seçiniz (tek karakter): ")

        while oyuncu_karakter1 == oyuncu_karakter2:
            print("Lütfen ilk oyuncudan farklı karakter seçiniz !!!")
            oyuncu_karakter2 = input("Lütfen kullanacağınız karakteri seçiniz (tek karakter): ")

        for i in range(oyun_boyutu):
            taslar = [" "] * oyun_boyutu
            board_list.append(taslar)

        for j in range(oyun_boyutu):
            board_list[0][j] = oyuncu_karakter1
            board_list[oyun_boyutu - 1][j] = oyuncu_karakter2

        yazdir(oyun_boyutu, board_list, harf_list, sayi_list)
        yer_degistir(oyuncu_karakter1, oyuncu_karakter2, oyun_boyutu, board_list, harf_list, sayi_list, harf_dict)
        print("Bizi oynadığınız için teşekkür ederiz :) ")

    except ValueError as error:
        print(error)
    except KeyError as error:
        print(error)
    except IndexError as error:
        print(error)


main()

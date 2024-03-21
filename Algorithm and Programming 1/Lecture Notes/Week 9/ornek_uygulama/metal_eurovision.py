max_puan = -1
try:
    eurovision_file = open("metal_eurovision.txt", "r")
    ulke_adi = eurovision_file.readline()
    while ulke_adi != '':
        sarkici_adi = eurovision_file.readline()
        sarki_adi = eurovision_file.readline()
        print(ulke_adi, sarkici_adi, sarki_adi)
        puan = int(input("bu yarismacinin puanini giriniz:"))
        while puan < 0:
            puan = int(input("bu yarismacinin puanini giriniz:"))
        if puan > max_puan:
            max_puan = puan
            max_puan_ulke = ulke_adi
            max_puan_sarkici = sarkici_adi
            max_puan_sarki = sarki_adi
        ulke_adi = eurovision_file.readline()
    eurovision_file.close()
except IOError:
    print("Dosya acilamadi!")
except ValueError:
    print("Hatali sayisal veri girisi!")
except:
    print("Bir hata olustu!")
else:
    print("Kazanan yarismaci:")
    print(max_puan_ulke, max_puan_sarkici, max_puan_sarki, max_puan)

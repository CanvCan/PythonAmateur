# hesaplanmayan girdiler

ogrenci_no = input('lütfen öğrenci numaranızı giriniz ')

ad_soyad = input('lütfen ad ve soyadınızı giriniz ')

# sayı girdileri

ilk_ders_t = int(input('lütfen aldığınız ilk dersin teorik ders saatini yazın '))

ilk_ders_u = int(input('lütfen aldığınız ilk dersin uygulama ders saatini yazın '))

ilk_ders_akts = int(input('lütfen ilk dersinizin AKTS değerini girin  '))

ilk_ders_not = float(input('lütfen ilk dersinizn dönem sonu notu giriniz '))

ikinci_ders_t = int(input('lütfen aldığınız ikinci dersin teorik ders saatini yazın '))

ikinci_ders_u = int(input('lütfen aldığınız ikinci dersin uygulama ders saatini yazın '))

ikinci_ders_akts = int(input('lütfen ikinci dersinizin AKTS değerini girin '))

ikinci_ders_not = float(input('lütfen dersinizin dönem sonu notunu giriniz '))

# hesaplamalı girdiler

ilk_ders_yerel = (ilk_ders_t + ilk_ders_u) / 2

ikinci_ders_yerel = (ikinci_ders_t + ikinci_ders_u) / 2

toplam_yerel = ilk_ders_yerel + ikinci_ders_yerel

toplam_akts = ilk_ders_akts + ikinci_ders_akts

yerel_agno = ((ilk_ders_not * ilk_ders_yerel) + (ikinci_ders_not * ikinci_ders_yerel)) / (
            ilk_ders_yerel + ikinci_ders_yerel)

akts_agno = ((ilk_ders_not * ilk_ders_akts) + (ikinci_ders_not * ikinci_ders_akts)) / (ilk_ders_akts + ikinci_ders_akts)

print(ogrenci_no, ad_soyad, toplam_yerel, toplam_akts, format(yerel_agno, '.2f'), format(akts_agno, '.2f'))

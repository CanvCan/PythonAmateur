# kullanıcıdan alınan girdiler


yaş = int(input('Lütfen yaşınızı giriniz: '))

son_yıllık = int(input('Lütfen son yıllık ücretinizi giriniz: '))

nsezon_sonu = int(input('Lütfen takımınızın sezon sonu sırasını giriniz: '))  # normal sezon sonu sırası

# sezon sonu sırasına göre oynanan toplam maçı bulan algoritma


if nsezon_sonu <= 8:

    playoff = int(input('Lütfen takımınızın playoff sezonda oynadığı toplam maç sayısını giriniz: '))

    toplam_maç = 26 + playoff

else:

    toplam_maç = 26

maliyet = son_yıllık / toplam_maç

print(f"Takıma maç başı maliyetiniz:{maliyet:,.2f} TL ")

# girilen yaş değerine göre hesaplanan serbest kalma bedelini bulan algoritma


if yaş < 22:

    print('Serbest kalma hakkınız bulunmamaktadır')

elif yaş == 22:

    print('Serbest kalma hakkınız bulunmaktadır, serbest kalma bedeliniz: ', format(son_yıllık * 2, ',.2f'), 'TL')

elif yaş == 23:

    print('Serbest kalma hakkınız bulunmaktadır, serbest kalma bedeliniz: ', format(son_yıllık, ',.2f'), 'TL')

elif yaş == 24:

    print('Serbest kalma hakkınız bulunmaktadır, serbest kalma bedeliniz: ', format(son_yıllık / 2, ',.2f'), 'TL')

else:

    print('Serbest kalma hakkınız bulunmaktadır, serbest kalma bedeliniz: 0.00 TL')

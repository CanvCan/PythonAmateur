# Problem:
# 100’lük not sisteminin kullanıldığı ve dönem sonu notu hesabına laboratuvar
# notunun %20, arasınav notunun %30 ve final sınavı notunun %50 oranda katıldığı
# bir dersi alan bir öğrencinin öğrenci_no ve ad_soyad bilgileri ile laboratuvar,
# arasınav ve final sınavı notlarını kullanıcıdan alarak öğrencinin o derse ilişkin
# dönem sonu notunu bulan ve öğrencinin tüm bilgilerini ekrana yazdıran
# bir program yazınız.


# Algoritma:
# ogr_no=input()
# ad_soyad=input()
# lab_notu=input()
# arasinav_notu=input()
# final_notu=input()

# donem_sonu_notu=lab_notu*0.2+arasinav_notu*0.3+final_notu*0.5

# print(ogr_no,ad_soyad)
# print(lab_notu,arasinav_notu,final_notu)
# print(donem_sonu_notu)


# Program:
LAB_KATSAYISI = 0.2
ARASINAV_KATSAYISI = 0.3
FINAL_KATSAYISI = 0.5

ogr_no = input('öğrenci numaranızı giriniz:')
ad_soyad = input('adınızı ve soyadınızı giriniz:')
lab_notu = int(input('lab notunuzu giriniz:'))
arasinav_notu = int(input('arasinav notunuzu giriniz:'))
final_notu = int(input('final sinavi notunuzu giriniz:'))

donem_sonu_notu = lab_notu * LAB_KATSAYISI + arasinav_notu * ARASINAV_KATSAYISI + final_notu * FINAL_KATSAYISI
# Dikkat: 100'luk sistemde, dönem sonu notu tam sayı olmalıdır!

# donem_sonu_notu=round(lab_notu*LAB_KATSAYISI+arasinav_notu*ARASINAV_KATSAYISI+final_notu*FINAL_KATSAYISI)
# #round, tamsayıya (int) yuvarlıyor

# donem_sonu_notu=round(lab_notu*LAB_KATSAYISI+arasinav_notu*ARASINAV_KATSAYISI+final_notu*FINAL_KATSAYISI,0)
# #round, ondalık basamak sayısı verilen reel sayıya (float) yuvarlıyor

print(f'Sayin {ogr_no} ' + f'numaralı {ad_soyad};')
print(f"Lab notunuz: {lab_notu}")
print("Arasinav notunuz:", arasinav_notu)
print("Final sinavi notunuz:", final_notu)
# print(f"Donem sonu notunuz: {donem_sonu_notu}") #donem_sonu_notu'nun tipi int ise bunu kullan
print(f"Donem sonu notunuz: {donem_sonu_notu:.0f}")  # donem_sonu_notu'nun tipi float ise bunu kullan

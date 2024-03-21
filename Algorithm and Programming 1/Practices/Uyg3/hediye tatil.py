# Problem:
# Bir yazılım şirketi her yılbaşında o yıl içerisinde hiç izin kullanmayan ve en az bir kez ayın elemanı
# seçilen çalışanlarına ünvanı stajer ise Türkiye’de, uzman ise Avrupa’da, takım lideri ise Uzak Doğu’da,
# müdür ise Amerika’da şirketteki çalışma süresi 2 yıldan az ise 3 gün, 2 yıl veya üstü 5 yıldan az ise 4 gün,
# 5 yıl veya üstü 10 yıldan az ise 5 gün, 10 yıl veya üstü ise 1 hafta süreli tatil paketi hediye etmektedir.
# Buna göre bir çalışanın ünvanını (s:stajer, u:uzman, l:takım lideri, m:müdür), şirketteki çalışma süresini (yıl),
# o yıl içerisinde kullandığı toplam izin günü sayısını, hiç ayın elemanı seçilip seçilmediğini (e/h) kullanıcıdan
# alan ve çalışanın hediye tatil paketi kazanıp kazanmadığını, kazandıysa yerini ve gün sayısını ekrana yazdıran
# bir algoritma ve program yazınız.
# (Burak Değirmencioğlu (2021-22) isimli öğrencinin gönderdiği sorudan uyarlanmıştır.)


# Algoritma:
# unvan = input()
# calistigi_yil_say=input()
# izin_gun_say=input()
# ayin_elemani_secilmis_mi = input()
# 
# if izin_gun_say>0 or ayin_elemani_secilmis_mi=='h':
#     print("Tatil paketi kazanamadiniz.")
# else:
#     if unvan=="s":
#         tatil_yeri="Turkiye"
#     elif unvan=="u":
#         tatil_yeri="Avrupa"
#     elif unvan=="l":
#         tatil_yeri="Uzak Dogu"
#     else:
#         tatil_yeri="Amerika"
# 
#     if calistigi_yil_say<2:
#         tatil_gun_say=3
#     elif calistigi_yil_say<5:
#         tatil_gun_say=4
#     elif calistigi_yil_say<10:
#         tatil_gun_say=5
#     else:
#         tatil_gun_say=7
# 
#     print("Tatil paketi kazandiniz!",tatil_yeri,tatil_gun_say,"gun")


# Program:
unvan = input('Unvaninizi giriniz (s:stajer, u:uzman, l:takım lideri, m:müdür):')
calistigi_yil_say = int(input('Calistiginiz yil sayisini giriniz:'))
izin_gun_say = int(input('Bu yil kullandiginiz toplam izin gunu sayisini giriniz:'))
ayin_elemani_secilmis_mi = input('Bu yil hic ayin elemani secildiniz mi? (e/h)')

if izin_gun_say > 0 or ayin_elemani_secilmis_mi == 'h':
    print("Uzgunum, hediye tatil paketi kazanamadiniz.")
else:
    if unvan == "s":
        tatil_yeri = "Turkiye"
    elif unvan == "u":
        tatil_yeri = "Avrupa"
    elif unvan == "l":
        tatil_yeri = "Uzak Dogu"
    else:
        tatil_yeri = "Amerika"

    if calistigi_yil_say < 2:
        tatil_gun_say = 3
    elif calistigi_yil_say < 5:
        tatil_gun_say = 4
    elif calistigi_yil_say < 10:
        tatil_gun_say = 5
    else:
        tatil_gun_say = 7

    print(f"Tebrikler!, {tatil_gun_say} gunluk {tatil_yeri} tatili kazandiniz.")

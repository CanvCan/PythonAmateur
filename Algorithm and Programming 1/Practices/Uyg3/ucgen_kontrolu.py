# Problem:
# Kullanıcıdan bir üçgenin önce en uzun kenarının,
# daha sonra kısa kenarlarının uzunluklarını (tamsayı) alan ve
# üçgenin tipini ("üçgen değil", "dik üçgen", "geniş açılı üçgen",
# "dar açılı üçgen" şeklinde) belirleyen bir algoritma ve program yazınız.


# Algoritma:
# uzun_kenar=input()
# kisa_kenar1=input()
# kisa_kenar2=input()
#
# if uzun_kenar>=kisa_kenar1+kisa_kenar2:
#    print("üçgen değil")
# else:
#    uzun_kenar_kare=uzun_kenar**2
#    kisa_kenarlarin_kareler_toplami=kisa_kenar1**2+kisa_kenar2**2
#    if uzun_kenar_kare==kisa_kenarlarin_kareler_toplami:
#        print("dik üçgen")
#    elif uzun_kenar_kare>kisa_kenarlarin_kareler_toplami:
#        print("geniş açılı üçgen")
#    else:
#        print("dar açılı üçgen")


# Program:
uzun_kenar = int(input("Üçgenin en uzun kenarının uzunluğunu giriniz:"))
kisa_kenar1 = int(input("Üçgenin diğer bir kenarının uzunluğunu giriniz:"))
kisa_kenar2 = int(input("Üçgenin diğer kenarının uzunluğunu giriniz:"))

if uzun_kenar >= kisa_kenar1 + kisa_kenar2:
    print("Girilen sayılar bir üçgen oluşturmuyor!")
else:
    uzun_kenar_kare = uzun_kenar ** 2
    kisa_kenarlarin_kareler_toplami = kisa_kenar1 ** 2 + kisa_kenar2 ** 2
    if uzun_kenar_kare == kisa_kenarlarin_kareler_toplami:
        print("Bu üçgen, bir dik üçgendir")
    elif uzun_kenar_kare > kisa_kenarlarin_kareler_toplami:
        print("Bu üçgen, geniş açılı bir üçgendir")
    else:
        print("Bu üçgen, dar açılı bir üçgendir")

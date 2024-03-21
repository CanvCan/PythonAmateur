# Problem:
# Asal sayılar, sadece kendisine ve 1 sayısına bölünebilen 1’den büyük pozitif tam sayılardır.
# Buna göre kullanıcıdan tekrarlı bir şekilde tam sayılar alan ve bu sayıların asal olup olmadığını
# bulup ekrana yazdıran bir algoritma ve program yazınız (2’den küçük bir sayı girilirse program sonlanmalıdır).
#
# Not: 2’den sayının kareköküne kadar olan sayıların kontrol edilmesi yeterlidir.


# Algoritma:
# sayi=input()
# while sayi>1:
#    for bolen in range(2,sayi**0.5+1):
#        if sayi%bolen==0:
#            print("asal değil!")
#            break # for döngüsünden çıkar...
#    else: # break ile çıkılmamışsa çalışır...
#        print("asal!")
#
#    sayi=input()


# Program:
sayi = int(input("Asal olup olmadığını öğrenmek istediğiniz (çıkmak için 2'den küçük) bir sayı giriniz:"))
while sayi > 1:
    for bolen in range(2, int(sayi ** 0.5) + 1):
        if sayi % bolen == 0:
            print(f"{sayi} asal değil!")
            break  # for döngüsünden çıkar...
    else:  # break ile çıkılmamışsa çalışır...
        print(f"{sayi} asal!")

    sayi = int(input("Asal olup olmadığını öğrenmek istediğiniz (çıkmak için 2'den küçük) bir sayı giriniz:"))

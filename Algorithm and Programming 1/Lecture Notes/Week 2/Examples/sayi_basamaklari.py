# Problem:
# Kullanıcıdan 2 basamaklı bir tamsayı alan (hata kontrolü yapılmasına gerek yoktur) ve
# bu sayının birler ve onlar basamağındaki sayıları, bu sayıların toplamını ve
# sayının basamakları karşılıklı yer değiştirildiğinde oluşan yeni sayıyı ekrana yazdıran
# bir algoritma (python-like pseudocode) ve program (python source code) yazınız.

# Algoritma:
# iki_basamakli_sayi=input()
# birler_bas=iki_basamakli_sayi%10
# onlar_bas=iki_basamakli_sayi//10
# ters_sayi=birler_bas*10+onlar_bas
# print(birler_bas,onlar_bas)
# print(birler_bas+onlar_bas)
# print(ters_sayi)

# Program:
iki_basamakli_sayi = int(input("2 basamaklı bir sayı giriniz:"))
birler_bas = iki_basamakli_sayi % 10
onlar_bas = iki_basamakli_sayi // 10
ters_sayi = birler_bas * 10 + onlar_bas
print("birler basamağı:", birler_bas, "\nonlar basamağı:", onlar_bas)
print("basamakların sayı değerleri toplamı:", birler_bas + onlar_bas)
print("basamaklari yer değiştiğinde oluşan sayı:", ters_sayi)

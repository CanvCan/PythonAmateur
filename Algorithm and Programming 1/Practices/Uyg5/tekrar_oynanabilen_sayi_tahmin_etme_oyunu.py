import random  # random kütüphanesi, rasgele sayı üretimi ile ilgili hazır fonksiyonları içerir.

MIN_SAYI = 1
MAX_SAYI = 100

min_tahmin_say = MAX_SAYI - MIN_SAYI + 1
tekrar = 'e'

while tekrar == 'e' or tekrar == 'E':  # En az 1 kez girmesi isteniyor.
    sayi = random.randint(MIN_SAYI,
                          MAX_SAYI)  # randint(min,max) fonksiyonu, min ile max arasında rasgele bir tamsayı döndürür.

    tahmin = int(input("Lütfen tahmini bir sayı giriniz:"))
    tahmin_say = 1

    while sayi != tahmin:
        if tahmin < sayi:
            print("YUKARI!")
        else:
            print("AŞAĞI!")

        tahmin = int(input("Lütfen tahmini bir sayı giriniz:"))
        tahmin_say += 1

    print("TEBRİKLER! Doğru tahmin ettiniz.")
    print(f"{tahmin_say} tahminde bilgisayarın tuttuğu sayıyı buldunuz.")

    if tahmin_say < min_tahmin_say:
        min_tahmin_say = tahmin_say

    tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")
    while tekrar not in ['e', 'E', 'h', 'H']:  # in operatörü, liste içerisinde belirli bir elemanın aranmasını sağlar.
        tekrar = input("Tekrar oynamak ister misiniz(e/E/h/H)?")

print("Hoşçakal")
print(f"En az tahmin sayısı rekoru:{min_tahmin_say}")

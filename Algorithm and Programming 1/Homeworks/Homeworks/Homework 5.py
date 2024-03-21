# İlk girdi
top_mac = int(input('oynadığınız toplam maç sayısını giriniz: '))

# değişkenler_1
max_set = 5
max_fark = 0
max_fark_rakip = 0
top_win_set = 0
top_lose_set = 0
win_mac = 0
lose_mac = 0
not_set_mac = 0
set_sayi = 0

# döngüler
for sayac_1 in range(1, top_mac + 1):
    rakip_ad = input('lütfen rakip takımın adını giriniz ')
    # degişkenler_2
    win_set = 0
    lose_set = 0
    top_win_sayi = 0
    top_lose_sayi = 0
    for sayac_2 in range(1, max_set + 1):
        win_sayi = int(input('kazandığınız sayı miktarını giriniz: '))
        lose_sayi = int(input('kaybettiğiniz sayı miktarını giriniz: '))
        if win_sayi > lose_sayi:
            win_set += 1
        elif win_sayi < lose_sayi:
            lose_set += 1

        if win_set > lose_set and win_set >= 3:
            win_mac += 1
        else:
            lose_mac += 1

        if win_set == 3 and lose_set == 0:
            not_set_mac += 1
        # hesaplamalar
        set_sayi += 1
        top_win_sayi += win_sayi
        top_lose_sayi += lose_sayi
        top_win_set += win_set
        top_lose_set += lose_set
        ort_win_sayi = top_win_sayi / set_sayi
        ort_lose_sayi = top_lose_sayi / set_sayi
        if win_set == 3 or lose_set == 3:
            break
    if top_win_sayi - top_lose_sayi > max_fark:
        max_fark = top_win_sayi - top_lose_sayi
        max_fark_rakip = rakip_ad
    # print_kısmı_1
    print('kazandığınız toplam sayı: ', top_win_sayi)
    print('kaybettiğiniz toplam sayı: ', top_lose_sayi)
    print('kazandığınız toplam set sayısı: ', win_set)
    print('kaybettiğiniz toplam set sayısı: ', lose_set)
    print(f"set başına kazandığınız ortalama sayı: {ort_win_sayi:,.2f}")
    print(f"set başına kaybettiğiniz ortalama sayı: {ort_lose_sayi:,.2f}")

# print_kısmı_2
print('kazandığınız toplam sayı miktarı: ', top_win_sayi)
print(f"maç başına kazandığınız ortalama sayı miktarı: {top_win_sayi / top_mac:,.2f}")
print('kazandığınız toplam maç sayısı: ', win_mac)
print('kaybettiğiniz toplam maç sayısı: ', lose_mac)
print('set kaybetmeden kazandığınız maç sayısı: ', not_set_mac, 've bunun tüm maçlar içindeki oranı: %',
      format(not_set_mac / win_mac * 100, ',.2f'))
print('farkın en büyük olduğu maçtaki fark: ', max_fark, 've rakim takımın adı: ', max_fark_rakip)

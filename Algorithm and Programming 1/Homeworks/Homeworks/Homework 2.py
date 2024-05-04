ilk_ad = input('Lütfen ilk takımın adını giriniz: ')

ilk_set = int(input('Lütfen ilk takımın kazandığı set sayısını giriniz: '))

ikinci_ad = input('Lütfen ikinci takımın adını giriniz: ')

ikinci_set = int(input('Lütfen ikinci takımın kazandığı set sayısını giriniz: '))

# while döngüsünün kullanılması istenmediğinden kullanıcının set değeri olarak 0,1,2 ve 3 dışında başka bir değer girmediği ve bunları (3-0/3-1/3-2/0-3/1-3/2-3) şeklinde girdiği varsayılmaktadır

if ilk_set == 3 and ikinci_set == 0 or ilk_set == 3 and ikinci_set == 1:
    print('Maçı kazanan takımın adı: ', ilk_ad, 'puanı: ', 3)

    print('Maçı kaybeden takımın adı: ', ikinci_ad, 'puanı: ', 0)

if ilk_set == 3 and ikinci_set == 2:
    print('Maçı kazanan takımın adı: ', ilk_ad, 'puanı: ', 2)

    print('Maçı kaybeden takımın adı: ', ikinci_ad, 'puanı: ', 1)

if ikinci_set == 3 and ilk_set == 0 or ikinci_set == 3 and ilk_set == 1:
    print('Maçı kazanan takımın adı: ', ikinci_ad, 'puanı: ', 3)

    print('Maçı kaybeden takımın adı: ', ilk_ad, 'puanı: ', 0)

if ikinci_set == 3 and ilk_set == 2:
    print('Maçı kazanan takımın adı: ', ikinci_ad, 'puanı: ', 2)

    print('Maçı kaybeden takımın adı: ', ilk_ad, 'puanı: ', 1)

# Problem:
# Amerikan doları cinsinden girilen bir para miktarının TL karşılığını (1$=18,5885 TL) hesaplayıp
# ekrana yazdıran bir algoritma (python-like pseudocode) ve program (python source code) yazınız.

# Algoritma:
# DOLAR_KURU=18.5885
# dolar_miktari=input()
# tl_miktari=dolar_miktari*DOLAR_KURU
# print(tl_miktari)

# Program:
DOLAR_KURU = 18.5885
dolar_miktari = float(input("TL karşılığını öğrenmek istediğiniz Amerikan doları miktarını giriniz:"))
tl_miktari = dolar_miktari * DOLAR_KURU
print(f'{dolar_miktari:,.2f} $ = {tl_miktari:,.2f} TL')

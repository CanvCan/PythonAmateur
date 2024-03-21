import cember
import kuvvet
import math

cevre = cember.cemberin_cevresi()
print(f"cemberin cevresi: {cevre}")

cevre = cember.cemberin_cevresi(5)
print(f"cemberin cevresi: {cevre}")

cevre = cember.cemberin_cevresi(5, 3)
print(f"cemberin cevresi: {cevre}")

cevre = cember.cemberin_cevresi(pi_sayisi=3, yaricap=5)
print(f"cemberin cevresi: {cevre}")

yaricap = float(input("cemberin yaricap uzunlugunu giriniz:"))
cevre = cember.cemberin_cevresi(yaricap)
print(f"cemberin cevresi: {cevre}")

cevre = cember.cemberin_cevresi(yaricap, math.pi)
print(f"cemberin cevresi: {cevre}")

print(f"2 üzeri 16: {kuvvet.kuvvet(2, 16)}")

print(f"111 üzeri 0: {kuvvet.kuvvet(111, 0)}")

print(f"2 üzeri 10: {kuvvet.kuvvet(us=10, taban=2)}")

taban = int(input("tabanı giriniz:"))
us = int(input("üssü giriniz(0 ya da daha büyük):"))
print(f"{taban} üzeri {us}: {kuvvet.kuvvet(taban, us)}")
print(f"{taban} üzeri {us}: {kuvvet.kuvvet(us=us, taban=taban)}")

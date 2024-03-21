"""
program girilen metinin uzunluğuna göre okuma süresini verir
Türkçe bir metin için normal okuma hızı ile bir saniyede 3 kelime okunduğu varsayılır
"""


def entry(text):

    import sys

    print("Lütfen metninizi giriniz ve çıkmak için ctrl+d yapınız: ")

    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        text.append(line)

    while "\n" in text:
        text.remove("\n")
    while " \n" in text:
        text.remove(" \n")

    purification(text)


def purification(text):

    file = open("C:\\Users\\Can\\Desktop\\data_set.txt", "w")
    for i in text:
        file.write(i)

    file.close()

    file = open("C:\\Users\\Can\\Desktop\\data_set.txt", "r")

    pure_text = file.read().split(" ")
    file.close()

    calculation(pure_text)


def calculation(pure_text):

    sum_reading_time_sn = len(pure_text) / 3
    sum_reading_time_dk = len(pure_text) / 180

    typing(sum_reading_time_sn, sum_reading_time_dk)


def typing(sum_reading_time_sn, sum_reading_time_dk):

    print(f"Tahmini okuma süreniz {sum_reading_time_dk:.2f} dakika ya da {sum_reading_time_sn:.2f} saniyedir.")
    print("Tahmini okuma süreniz: {} dk ya da {} sn ".format(round(sum_reading_time_dk, 2), round(sum_reading_time_sn, 2)))


def main():
    text = []
    entry(text)


main()

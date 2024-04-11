

# region Sayı Tahmin Oyunu
try:
    import random

    gizli_sayi = random.randint(1, 10)

    print(" Sayı tahmin oyununa hoşgeldiniz ")
    deneme = 0

    while True:
        girilen_sayi = int(input(" Sayı tahmini giriniz: "))
        deneme += 1
        if girilen_sayi < gizli_sayi:
            print(" Daha büyük ")
        elif girilen_sayi > gizli_sayi:
            print(" Daha küçük ")
        else:
            print(f'Tebrikler! {deneme} denemede bildiniz. ')
            break
except ValueError as err:
    print("Lütfen sayı giriniz..!")
finally:
    print("Game Over")
# endregion



# region 10 Defa Tahmin Hakkı Olan Sayı Tahmin Oyunu
from random import randint
try:
    rastgele_sayi = randint(1,100)
    print("Sayı tahmin oyununa hoşgeldiniz.")
    deneme = 0
    Hak = 10
    while True:
        oyuncu = int(input("Sayı tahmini yapınız:"))
        deneme += 1
        Hak -= 1
        if rastgele_sayi == oyuncu:
            print(f'Tebrikler.{deneme} denemede kalan {Hak} hakkınızı kullanmadan bildiniz!')
            break
        elif rastgele_sayi < oyuncu:
            print("Daha küçük bir sayı giriniz..")
        elif rastgele_sayi > oyuncu:
            print("Daha büyük bir sayı giriniz..")
        if Hak == 0:
            print(f'Bütün hakkınızı kullandınız. Tutulan sayı: {rastgele_sayi}')
            break
except ValueError as err:
    print(f'Lütfen geçerli parametreleri giriniz..!  {err}')
# endregion
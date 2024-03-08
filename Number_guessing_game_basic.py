

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


# region PROJE: Kelime Analiz Programı [S O R]
# Kelime ve ya cümle gir ve metni analiz ederek şunları yap: Metin içinde belirli harf ve ya kelime var mı. Girilen metin bir palindrom mu (tersten okunursa da aynı). metinde türkçe karakterler var mı.

try:
    metin = input("Kelime veya cümle giriniz")
    aranan_kelime_harf = input("Aranan kelime veya harfi giriniz: ")
    turkce_karakter = "ı,ğ,ü,ş,ö,ç"
    palindrom_kelime = metin[::-1]
    if aranan_kelime_harf in metin and metin == palindrom_kelime:
        print(f'Aranan palindrom kelime / harf bulundu \n{aranan_kelime_harf}')
    elif turkce_karakter in metin:
        print("Metin türkçe karakter içeriyor. ")
    else:
        print("Metin türkçe karakter içermiyor. ")
except Exception as err:
    print(f'{err} ')
finally:
    print("Program sonlandırılıyor...")
# endregion
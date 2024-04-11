

# region ATM - Bankamatik uygulaması
# Çekilmek istenilen para bakiye tarafından karşılanmalı
# Miktar bakiyeden fazla ise ek hesap kullanılsın mı diye müşteriye soralım
# Müşteri evet derse ek hesap devreye girsin ve para çekilsin
# Hayır derse işlem iptal
# Adamın balance ve additional balance'si çekilmek istenilen tutarı karşılamıyorsa feedback verilsin ve işlem iptal edilsin
# işlem önceliği ekhesapta olsun. önce o kısım boşsa para ile doldurulsun.
# EFT İşlemi yapılabilsin.


bora_hesap = {
    'hesap_no': '12345',
    'full_name': 'Bora Eren Erdem',
    'password': '123',
    'bakiye': 2000,
    'ek_bakiye': 1200
}


mehmet_hesap = {
    'hesap_no': '98765',
    'full_name': 'Mehmet Erdem',
    'password': '123',
    'bakiye': 5000,
    'ek_bakiye': 1200
}


ayse_hesap = {
    'hesap_no': '74185',
    'full_name': 'Ayşe Erdem',
    'password': '123',
    'bakiye': 6200,
    'ek_bakiye': 1200
}

kullanicilar = [bora_hesap, mehmet_hesap, ayse_hesap]


def panel(hesap: dict):
    print(f"Hoşgeldiniz {hesap['full_name']}\n"
            f"/////////////////////////\n"
            f"Para Çekmek İçin: 1\n"
            f"Para Yatırmak İçin: 2\n"
            f"Hesap Bilgisi İçin: 3\n"
            f"EFT İşlemleri İçin: 4\n"
            f"Çıkış İçin: 5\n")



def hesap_bilgisi(hesap: dict):
    print(f"Hesap Bilgileri:\n"
            f"////////////\n"
            f"Ad/Soyad: {hesap['full_name']}\n"
            f"Hesap Numarası: {hesap['hesap_no']}\n"
            f"Şifre: {hesap['password']}\n"
            f"Bakiye: {hesap['bakiye']}\n"
            f"Ek Bakiye: {hesap['ek_bakiye']}")



def login(hesap_no: str, password: str):
    hesap = {}
    for i in kullanicilar:
        if i['hesap_no'] == hesap_no and i['password'] == password:
            hesap = i
            break

    return hesap



def bakiye_sonucu(hesap: dict):
    print(f"{hesap['hesap_no']} numaralı banka hesabınızda bakiyenizde {hesap['bakiye']} TL bulunmaktadır.\n"
            f"Ek hesabınızdaki güncel durum: {hesap['ek_bakiye']} TL bulunmaktadır.")



def para_cekme(hesap: dict, miktar: int):
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print(f'Paranızı almayı unutmayınız..!')
        bakiye_sonucu(hesap)
    else:
        toplam_bakiye = hesap['bakiye'] + hesap['ek_bakiye']

        if toplam_bakiye >= miktar:
            ek_bakiye_sorgusu = input("Bakiyeniz yetersiz olduğu için işlemi gerçekleştiremiyorsunuz. Ek bakiyenizden kullanmak ister misiniz? (Evet/Hayır)").lower()

            if ek_bakiye_sorgusu == 'evet':
                kullanilan_ek_bakiye = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ek_bakiye'] -= kullanilan_ek_bakiye
                bakiye_sonucu(hesap)

            elif ek_bakiye_sorgusu == 'hayır':
                print(f'Para çekme işleminiz iptal edilmiştir..!')
                bakiye_sonucu(hesap)

            elif ek_bakiye_sorgusu != 'evet' or 'hayır':
                print(f'Lütfen belirtilen işlem türünü seçin..! (Evet/Hayır)')

        else:
            print(f'Toplam bakiye yetersiz olduğu için işleminiz iptal edilmiştir..!')



def para_yatirma(hesap: dict, miktar: int):
    hesap['bakiye'] += miktar

    if hesap['ek_bakiye'] < 1200:
        ek_hesaba_aktarilacak_miktar = 1200 - hesap['ek_bakiye']
        hesap['bakiye'] -= ek_hesaba_aktarilacak_miktar
        hesap['ek_bakiye'] += ek_hesaba_aktarilacak_miktar
    bakiye_sonucu(hesap)



def EFT_islemleri(gonderici_hesabi: dict, alici_hesap_numarasi: str, miktar: int):
    for i in kullanicilar:
        if i['hesap_no'] == alici_hesap_numarasi:
            para_cekme(gonderici_hesabi, miktar)
            para_yatirma(i, miktar)



def main():
    kullanici_hesabi = login(
        input("Hoşgeldiniz.\n"
                "=============\n"
                "Hesap Numarası: ").lower(),
        input("Password: ")
    )

    if kullanici_hesabi != {}:
        panel(kullanici_hesabi)
        while True:
            islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

            if islem == '1':
                miktar = int(input("Lütfen miktarı giriniz: "))
                para_cekme(kullanici_hesabi, miktar)

            elif islem == '2':
                miktar = int(input("Lütfen miktarı giriniz: "))
                para_yatirma(kullanici_hesabi, miktar)

            elif islem == '3':
                hesap_bilgisi(kullanici_hesabi)

            elif islem == '4':
                miktar = int(input("Lütfen miktarı giriniz: "))
                alici_hesap_numarasi = input("Hesap numarasını giriniz: ")
                EFT_islemleri(kullanici_hesabi, alici_hesap_numarasi, miktar)

            elif islem == '5':
                print(f'Aplikasyondan çıkış yapılıyor..')
                break

            else:
                print(f'Yanlış işlem numarasını tuşladınız..!')

        else:
            print(f'Kimlik doğrulama başarısız oldu. Lütfen kimlik bilgilerinizi kontrol edin..!')

main()
# endregion
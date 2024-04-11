

BoraHesap = {
    'ad': 'Bora Eren Erdem',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Matkap',
    'hesapNo': '98765432',
    'bakiye': 5000,
    'ekHesap': 1000
}


def paracek(hesap:dict, miktar: int):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print(f'Paranızı alabilirsiniz. Güncel bakiyeniz: {hesap["bakiye"]}')
    else:
        if hesap['bakiye'] + hesap['ekHesap'] >= miktar:  # Ek hesap kullanılabilir mi?
            sorgu = input(f'Çekmek istediğiniz tutar bakiyenizden fazla. EkHesaptan kullanmak ister misiniz? (Evet/Hayır)').lower()
            if sorgu == 'evet':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                hesap['bakiye'] = 0
                print(f'Para çekme işleminiz başarıyla gerçekleşti.\n'
                        f"{hesap['hesapNo']} nolu hesabınızdaki güncel durum:\n"
                        f"Güncel bakiyeniz: {hesap['bakiye']}\n"
                        f"Güncel ekHesap bakiyeniz: {hesap['ekHesap']}")
            else:
                print(f'Para çekme talebiniz bakiyeniz yetersiz olduğundan işlem iptal edilmiştir.')
        else:
            print(f'Bakiyeniz ve ek hesabınız toplamı çekmek istediğiniz tutardan yetersizdir.')



def bakiyeSorgula(hesap: dict):
    print(f"{hesap['hesapNo']} nolu hesabınızdaki bilgiler:\n"
            f"güncel bakiyeniz: {hesap['bakiye']}\n"
            f"güncel ekHesabınız: {hesap['ekHesap']}")



def main():
    while True:
        try:
            sorgu = input(f'Hoşgeldiniz. İşlem tercihinizi yapmak için lütfen aşağıdaki numaraları seçin:\n'
                    f'*******************************\n'
                    f'Para çekmek için: 1\n'
                    f'Hesap bakiye durumunu öğrenmek için: 2\n'
                    f'Çıkış yapmak için: 3\n')

            if sorgu == '1':
                hesap_adi = input("Hesap adını giriniz:").lower()
                miktar = int(input("Çekmek istediğniz miktarı giriniz:"))
                if hesap_adi == 'borahesap':
                    paracek(BoraHesap, miktar)
                elif hesap_adi == 'alihesap':
                    paracek(AliHesap, miktar)
                else:
                    print(f'Hesap adınız yanlış. Bilgilerinizi kontrol ediniz.')

            elif sorgu == '2':
                hesap_adi = input("Hesap adını giriniz:").lower()
                if hesap_adi == 'borahesap':
                    bakiyeSorgula(BoraHesap)
                elif hesap_adi == 'alihesap':
                    bakiyeSorgula(AliHesap)

            elif sorgu == '3':
                print(f'Çıkış yapılıyor...')
                break

        except Exception as err:
            print(f'Beklenmedik bir hata oluştu. Lütfen sayfayı yenileyip tekrar deneyiniz..! {err}')

main()
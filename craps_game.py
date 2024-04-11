

# region Basit Barbut Oyunu
# botlar = ['ahmet', 'mehmet', 'ayşe']
# minimum_bahis = 100
# Kullanıcıalrın kasası olacak. Kazanırsayaptığı bahisin 2 katı hesabına yatırılacak. Kaybederseyaptığı bahis kasadan düşecek.
# login işlemi olacak.
# Kullanıcı login olduğunda daily_chip hediye edilecek (1000, 2000 arasında)

from random import randint, choice

botlar = ['ahmet', 'mehmet', 'ayse']
minimum_bet = 100
kullanici_dict = {
    '1': {
        'kullanici_adi': 'beast',
        'password': '123',
        'kasa': 1200
    },
    '2': {
        'kullanici_adi': 'savage',
        'password': '123',
        'kasa': 2000
    },
}

def botgetirme(botlar):
    return choice(botlar)


def zar_atisi():
    return randint(2, 12)


def gunluk_giris_parasi():
    return randint(1000, 2000)


def bet_kontrolu(guncel_bahis: int, kasa: int):
    if minimum_bet <= guncel_bahis <= kasa:
        return True
    else:
        return False


def giris(kullanici_adi: str, password: str):
    for i in range(1, len(kullanici_dict) + 1):
        if kullanici_dict.get(str(i)).get('kullanici_adi') == kullanici_adi and kullanici_dict.get(str(i)).get('password') == password:
            kullanici_id = str(i)
            print(f'Giriş başarılı....Hoşgeldiniz..!')
            return kullanici_id
    else:
        print(f'Hatalı kullanıcı adı veya şifre tuşladınız. Lütfen bilgilerinizi kontrol ediniz.')


def kasa_guncelleme(kazanilan_para: int, kullanici_id: str, kullanici_dict: dict):
    kullanici_dict[kullanici_id]['kasa'] += kazanilan_para


def main():
    kullanici_id = giris(
        input("Kullanıcı adı:"),
        input("Password:")
    )

    if kullanici_id:
        gunluk_para = gunluk_giris_parasi()

        kasa_guncelleme(gunluk_para, kullanici_id, kullanici_dict)

        print(f"Hoşgeldiniz {kullanici_dict[kullanici_id]['kullanici_adi']}, {gunluk_para} kazandınız. Kasanızın güncel durumu = {kullanici_dict[kullanici_id]['kasa']}")

        while True:
            if kullanici_dict[kullanici_id]['kasa'] >= minimum_bet:
                bahis = int(input("Lütfen bahis miktarını giriniz:"))

                if bet_kontrolu(bahis, kullanici_dict[kullanici_id]['kasa']):
                    oyuncu = botgetirme(botlar)
                    print(f'{oyuncu} isimli oyuncuyla karşılaştınız. Bol şanslar...')

                    oyuncu1_zar_atisi = zar_atisi()
                    oyuncu2_zar_atisi = zar_atisi()

                    if oyuncu1_zar_atisi > oyuncu2_zar_atisi:
                        kullanici_dict[kullanici_id]['kasa'] += (bahis * 2)

                        print(f'Zarınız: {oyuncu1_zar_atisi}\n'
                                f'{oyuncu} zar atışı: {oyuncu2_zar_atisi}')

                        print(f'Tebrikler. {kullanici_dict[kullanici_id]['kullanici_adi']}\n'
                                f'Toplam kasanızdaki miktar: {kullanici_dict[kullanici_id]['kasa']}')

                    elif oyuncu2_zar_atisi > oyuncu1_zar_atisi:
                        kullanici_dict[kullanici_id]['kasa'] -= bahis

                        print(f'Zarınız: {oyuncu1_zar_atisi}\n'
                                f'{oyuncu} zar atışı: {oyuncu2_zar_atisi}')

                        print(f'Kaybettiniz. {kullanici_dict[kullanici_id]['kullanici_adi']}\n'
                                f'Toplam kasanızdaki miktar: {kullanici_dict[kullanici_id]['kasa']}')

                    else:
                        print(f'Oyuncular berabere.')
                else:
                    print(f'Lütfen geçerli bir bahis yapınız.')

            else:
                print(f'Kasanız minumum bet tutarının altında. Para yatırıp devam etmek ister misiniz?')
                break

    else:
        print(f'Geçersiz bilgiler.')

main()
# endregion
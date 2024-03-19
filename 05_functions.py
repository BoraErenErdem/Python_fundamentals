

# *params =>  Python'da bir fonksiyona değişken sayıda argüman geçirmek için kullanılan bir tekniktir. * operatörü, Python'da bir tuple'ı temsil eder. Bu nedenle, *params demek, bir tuple içinde toplanmış olan değişken sayıda argümanları ifade eder.

# **params => Python'da bir fonksiyona değişken sayıda anahtar-değer çifti geçirmek için kullanılan bir tekniktir. Bu ifade, sözlük (dictionary) türünü temsil eder. Fonksiyon çağrısı sırasında ** operatörüyle belirtilen argümanlar, bir sözlük içinde toplanır.




# functions Example

# region Verilen bir metni tersine çeviren bir Python fonksiyonu yazın
# 1.Yol
def tersine(metin: str):
    ters_metin = metin[::-1]
    print(ters_metin)

tersine(
    input("Metin giriniz:")
)


# 2.Yol
def tersten(metin: str):
    ters_metin = "".join(reversed(metin))
    print(ters_metin)

tersten(
    input("Metin giriniz:")
)
# endregion


# region Yaş hesaplama
def yas_hesaplama(dogumyili):
    return 2024 - dogumyili

yas = yas_hesaplama(2001)
print(yas)
# endregion


# region Emekliliğe kaç yıl kaldığını bulun
def emeklilik_hesabi(dogumyili: int, isim: str):
    yas = yas_hesaplama(dogumyili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print("Zaten emekli oldunuz.")

emeklilik_hesabi(
        int(input("Doğum yılınızı giriniz:")),
        input("İsim giriniz:"))
# endregion


# region Döngü ile sayıları toplama
def sayitoplam(sayi1:int, sayi2:int, sayi3:int):
    toplam = 0
    for i in sayi1, sayi2, sayi3:
        toplam += i
    return toplam

sonuc = sayitoplam(
    int(input("Sayi1:")),
    int(input("Sayi2:")),
    int(input("Sayi3:"))
)

print(sonuc)
# enderegion


# region Kullanıcıdan alınan sayı çift mi tek mi bul
def cift_tek(sayi: int):
    if sayi % 2 == 0:
        print(f'{sayi} çifttir')
    else:
        print(f'{sayi} tektir')

cift_tek(
    int(input("Sayi giriniz:"))
)
# endregion


# region Kullanıcıya mail oluştur
def mail_olustur(ad: str):
    ad_split = ad.lower().split(" ")
    print(f'{ad_split[0]}.{ad_split[-1]}@gmail.com')

mail_olustur(
    input("Adınızı giriniz:")
)
# endregion


# region Faktöriyel hesaplayan fonksiyon
def faktoriyel(sayi: int):
    fak = 1
    if sayi <= 0:
        print(f'Sayı sıfır veya negatif olamaz.')
    elif sayi == 1:
        print(f'1 sayısının faktöriyeli == 1')
    else:
        for i in range(1, sayi + 1):
            fak *= i
        print(f'{sayi} sayısının faktöiryeli = {fak}')

faktoriyel(
    int(input("Sayı girişi:"))
)
# endregion


# region kullanıcıdan kullanıcı adı ve password alalım login işlemi yapalım. kullanıcılar = [('beast', '123'), ('bear', '234'), ('savage', '987')]
kullanicilar = [('beast', '123'), ('bear', '234'), ('savage', '987')]

def login(kullanici_adi: str, password: str):
    for i, j in kullanicilar:
        if i == kullanici_adi and j == password:
            print(f'Giriş başarılı. Hoşgeldiniz...')
            break
    else:
        print(f'Giriş başarısız. Yanlış kullanıcı adı veya password tuşladınız..!')

login(
    input("Kullanıcı adınız:"),
    input("Password:")
)
# endregion


# region kullanıcıdan kullanıcı adı ve password alalım login işlemi yapalım. kullanıcılar = {'alice': '1234', 'bob': '5678', 'charlie': '91011'}
# 1.Yol
uyeler = {'alice': '1234', 'bob': '5678', 'charlie': '91011'}
def uye_girisi(uye_adi: str, sifre: str):
    for i, j in uyeler.items():  # uyeler bir dictionary olduğu için for ile elemanalrını çıkaramazsın. o yüzden sonuna .items() ekleyerek anahtar - değer ilişkisini çıkarsın.
        if i == uye_adi and j == sifre:
            print(f'Üye girişi başarılı. Hoşgeldiniz {uye_adi}')
            break
    else:
        print(f'Giriş başarısız..!')

uye_girisi(
    input("Üye adınızı giriniz:"),
    input("Şifre giriniz:")
)


# 2.Yol
kullanicilar = {'alice': '1234', 'bob': '5678', 'charlie': '91011'}
def giris(kullanici_adi: str, sifre: str):
    if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:  # kullanicilar bir dictionary olduğu için kullanicilar[kullanici_adi] == sifre yaptık.
        print("Giriş başarılı. Hoş geldiniz, {}!".format(kullanici_adi))
    else:
        print("Giriş başarısız. Yanlış kullanıcı adı veya şifre girdiniz.")

giris(
    input("Kullanıcı adı:"),
    input("Şifre:")
)
# endregion


# region *params ile değişik sayıda argümanlarla toplama işlemi.
def supertoplama(*params):
    toplam = 0
    for i in params:
        toplam += i
    print(toplam)

supertoplama(10,45,6,7,78)
# endregion


# region *params ile çarpma işlemi
def carpma_islemi(*params: int):
    carpim = 1
    for i in params:
        if i <= 0:
            print(f'Çarpım sonucu negatif ya da sıfır olamaz..!')
            return  # return ifadesi, fonksiyonun işlevini sonlandırır ve fonksiyon çağrıldığı yere geri döner. Bu, fonksiyon içindeki kodun geri kalanının çalıştırılmamasını sağlar.
        else:
            carpim *= i
    print(f'Çarpım sonucu = {carpim}')

carpma_islemi(10,2,5,7,7)
# endregion


# region *params ile aritmetik ortalama işlemi
def aritmetik_ort(*params: int):
    toplam = 0
    for i in params:
        toplam += i
        aritmetik = toplam / len(params)
    print(f'Aritmetik ortalama = {aritmetik}')

aritmetik_ort(10, 245, 67)
# endregion


# region return ile ilgili pratik
def kontrol(a: str):
    if a == 'bora':
        print("Girdiğiniz string bora")
    else:
        print("Girdiğiniz string farklı bişey.")

kontrol(
    str(input("İfade giriniz:"))
)
# endregion


# region return ile ilgili pratik
def cift_bul(x:int, y:int):
    cifttoplam = 0
    for i in range(x, y):
        if i % 2 == 0:
            cifttoplam += i
    print(f'çift sayılar toplamı: {cifttoplam}')
    if cifttoplam == 0:
        print(f'Geçersiz değer girdiniz..!')

cift_bul(
    int(input("Sayı giriniz:")),
    int(input("Sayı giriniz:"))
)
# endregion


# region *params pratikleri
def yenitoplama(*params):
    return sum(params)

print(yenitoplama(10,20,30,40,50,60))
print(yenitoplama(45,87,10000))
# endregion


# region *params pratikleri
def fonksiyon(*params):
    return params  # return kullandığımız için tipi tuple oldu. Normalde return kullanmasaydık print kullansaydık Nonetype olarak karşımıza çıkacaktı.

print(fonksiyon(1,23,6,3))
print(type(fonksiyon()))
# endreigon


# region Verilen dictionaryde key kontrolü yap (**params ile)
def keykontrol(**params):
    if 'bora' in params:
        print(f'bora keyi yer alıyor.')
    else:
        print(f'bora keyi yer almıyor.')

keykontrol(bora= 70, ali= 34, ahmet= 45)
# endregion


# region Gönderilen kelimeyi belirtilen kez ekranda gösteren fonksiyon yaz
def tekrar(kelime: str, sayac: int):
    for i in range(1, sayac + 1):
        print(f'Girdiğiniz {kelime} kelimeniz {sayac} defa tekrar ettirildi.')

tekrar('bora', 3)
# endregion


# region Kullanıcı tarafından sınırsız sayıda gönderilen parametreyi listeye çeviren fonksiyon
def parametre_listele(*params):
    liste = []
    for i in params:
        liste.append(i)
    return liste

sonuc = parametre_listele(1,2,3,4,5,6,'bora','eren','Erdem', 23545)
print(sonuc)
# endregion


# region Alınan 2 sayı arasından tüm asal sayıları bulun
def asalbul(sayi1: int, sayi2: int):
    for i in range(sayi1, sayi2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    print(f'Asal değil.{i}')
                    break
            else:
                print(f'Asal. {i}')

asalbul(
    int(input("Sayı giriniz:")),
    int(input("Sayı giriniz:"))
)
# endregion


# region Alınan bir sayının tam bölenlerini bir liste şeklinde tanımla
def tambolenliste(sayi: int):
    liste = []
    for i in range(1, sayi+1):
        if sayi % i == 0:
            liste.append(i)
    return liste

sonuc = tambolenliste(
    int(input("Sayı girişi:"))
)

print(sonuc)
# endregion


# region Sayının faktöriyelini hesaplayan fonksiyon
def faktoriyelhesaplama(x: int):
    faktor = 1
    if x <= 0:
        print(f'Sayı sıfır veya negatif olamaz.')
    elif x == 1:
        print(f"1'in faktöriyeli her zaman 1'dir.")
    else:
        for i in range(2, x+1):
            faktor *= i
    print(f'{x} sayısının faktöriyeli = {faktor}')

faktoriyelhesaplama(
    int(input("Sayı giriniz:"))
)
# endregion


# region Verilen bir listenin elemanlarının toplamını hesapla
liste = [1,3,6,7,98,3,5,2]
def listetoplam(list):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam

sonuc = listetoplam(list)
print(sonuc)
# endregion


# region Verilen bir string içindeki her bir karakterin kaç defa tekrarlandığını bulan bir fonksiyon yaz
string = "merhaba"
def tekrarlanankarakter():
    karakter = {}
    for i in string:
        if i in karakter:
            karakter[i] += 1
        else:
            karakter[i] = 1
    for i,j in karakter.items():
        print(f'{i} - {j}')

tekrarlanankarakter()
# endregion


# region Verilen bir listedeki herhangi bir sayının tek mi yoksa çift mi olduğunu belirleyen bir fonksiyon yaz
sayilistesi = [10,256,78,6274,89,416,45]
def tekcift(list):
    yeni_liste_cift = []
    yeni_liste_tek = []
    for i in sayilistesi:
        if i % 2 == 0:
            yeni_liste_cift.append(i)
        else:
            yeni_liste_tek.append(i)
    return yeni_liste_cift, yeni_liste_tek

cift_sonuc, tek_sonuc = tekcift(list)
print(cift_sonuc)
print(tek_sonuc)
# endregion


# region Verilen bir listenin en büyük ve en küçük elemanlarını bulan fonksiyon
liste = [1, 2, 4, 5, 78, 9, 234, 4, 2]
def buyuk_kucuk(list):
    yeni_liste = []
    for i in liste:
        liste.sort()
        yeni_liste.append(liste[0])
        yeni_liste.append(liste[-1])
    return yeni_liste

sonuc = buyuk_kucuk(list)
print(sonuc)
# endregion


# region Verilen bir listenin en uzun ve en kısa karakter sayısını bulan fonksiyon yazın
karakterler = ('bora','eren','erdem','yunus','gul','başaramadıklarımızdan','harikasın')

# endregion


# region Bir listedeki tüm negatif sayıların karesini alan bir fonksiyon yaz. Negatif olmayan sayıları olduğu gibi bırakmalı
sayi_listesi = [1,-4,6,-3,7,-4,7-43,78,-45]
def negatifkare(list):
    yenisayilistesi = []
    for sayi in sayi_listesi:
        if sayi < 0:
            kare = sayi ** 2
            yenisayilistesi.append(kare)
        elif sayi >= 0:
            yenisayilistesi.append(sayi)
    return sorted(yenisayilistesi)  # sort() metodunu kullansaydık "None" değeri alırdı. Oyüzden sorted() fonksiyonunu kullandık.

sonuc = negatifkare(list)
print(sonuc)
# endregion


# region Bir listedeki tekrarlanan elemanları bulan ve bu tekrarlanan elemanları bir liste olarak döndüren bir fonksiyon yaz
liste = [1,2,3,4,5,6,7,8,5,7,9]
def tekrarlanan_eleman(list):
    sayac = []
    tekrarlananlar = {}
    for i in liste:
        if i in tekrarlananlar:
            tekrarlananlar[i] += 1
        else:
            tekrarlananlar[i] = 1
    for i, j in tekrarlananlar.items():
        if j > 1:
            sayac.append(i)
    return sayac

sonuc = tekrarlanan_eleman(list)
print(sonuc)
# endregion


# region toplama fonksiyonu
def toplama(sayi1: int, sayi2: int):
    toplam = sayi1 + sayi2
    return toplam
sonuc = toplama(
    int(input("Sayı girin:")),
    int(input("Sayı girin:"))
)

print(sonuc)
# endregion


# region en büyük sayıyı bulan fonksiyonu yaz
# 1.Yol
sayilar = [1,3,4,6,5,2,7]
def enbuyuk():
    for i in sayilar:
        siralanmisListe = sorted(sayilar)
    return siralanmisListe[-1]

sonuc = enbuyuk()
print(sonuc)


# 2.Yol
sayilar = [1,3,4,6,5,2,7]
def buyuksayi():
    max(sayilar)
    return max(sayilar)

sonuc = buyuksayi()
print(sonuc)
# endregion


# region harf sayısını hesaplayan fonksiyon
def harf_sayisi_hesap(kelimeler: str):
    return len(kelimeler)

sonuc = harf_sayisi_hesap(
    input("Kelimeler giriniz:")
)

print(sonuc)
# endregion


# region Ürünlerin KDV'li fiyatını hesaplayan fonksiyon. KDV = 0.18
def kdv(fiyat: float):
    kdvli_fiyat = fiyat * 0.18
    return kdvli_fiyat

def toplam_fiyat(fiyat: float):
    kdvli_fiyat = kdv(fiyat)
    satis_fiyati = fiyat + kdvli_fiyat
    return satis_fiyati

def main():
    urunun_fiyati = float(input("Fiyat giriniz:"))
    urunun_toplam_fiyati = toplam_fiyat(urunun_fiyati)
    print("Ürünün toplam fiyatı:", urunun_toplam_fiyati)

main()
# endregion


# region yüzde ve indirimli fiyat hesaplayan fonksiyon yazın
def fiyat_yuzdesi(fiyat: float, yuzde: float):
    yuzde_hesap = (fiyat * yuzde) / 100
    return yuzde_hesap

def indirimli_fiyat(fiyat: float, yuzde:  float):
    indirim_miktari = fiyat_yuzdesi(fiyat, yuzde)
    indirimli_fiyat = fiyat - indirim_miktari
    return indirimli_fiyat

def main():
    fiyat = float(input("Fiyat girişi yapınız:"))
    yuzde = float(input("Yüzde girişi yapınız:"))
    sonuc = indirimli_fiyat(fiyat, yuzde)
    print(sonuc)

main()
# endregion
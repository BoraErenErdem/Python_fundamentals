

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
    for i, j in uyeler.items():  # uyeler bir dictionary olduğu için for ile elemanlarını çıkaramazsın. o yüzden sonuna .items() ekleyerek anahtar - değer ilişkisini çıkarsın.
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


# region Bir listede (örneğin, [1, 2, 3, 4, 5]) yer alan çift sayıların toplamını bulan bir Python fonksiyonu yazın.

liste = [1, 2, 3, 4, 5]
def cifttoplam(liste):
    cifttop = 0
    for i in liste:
        if i % 2 == 0:
            cifttop += i
    return cifttop

sonuc = cifttoplam(liste)
print(sonuc)
# endregion


# region Verilen bir sayının faktöriyelini hesaplayan bir Python fonksiyonu yazın
def faktoriyel(sayi):
    faktor = 1
    for i in range(1, sayi + 1):
        faktor *= i
    return faktor

sonuc = faktoriyel(
    int(input("Sayı giriniz:"))
)
print(sonuc)
# endregion


# region Kullanıcıdan alınan sayı çift mi tek mi
def tek_cift(sayi: int):
    if sayi % 2 == 0:
        print(f'Sayı çifttir.')
    else:
        print(f'Sayi tektir.')

tek_cift(
    int(input("Sayı giriniz:"))
)
# endregion


# region Emeklilik hesaplama
def yashesapla(dogumyili: int):
    return 2024 - dogumyili


def EmeklilikHesaplama(dogumyili: int, isim: str):
    yas = yashesapla(dogumyili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'{emeklilik} yıl kaldı.')
    else:
        print(f'Zaten emekli oldunuz.')


EmeklilikHesaplama(2001, 'Bora')
EmeklilikHesaplama(
    int(input("Doğum yılını giriniz:")),
    input("İsminizi giriniz:")
)
# endregion


# region Gönderilen kelimeyi belirtilen kez ekranda gösteren fonksiyon yazınız
def tekraryaz(x: str, y: int):
    for i in range(1, y+1):
        return f"{x} kelimesi {y} kere yazdırıldı."

print(tekraryaz(
    input("Kelime giriniz:"),
    int(input("Tekrar sayısını giriniz:"))
))
# endregion


# region Gönderilen sınırsız sayıda parametreleri listeye çevirin
def listeyecevir(*args):
    list = []
    for i in args:
        list.append(i)
    return list

print(listeyecevir(
    1,2,3,4,5,6,7,'ada','balık',67.9
))
# endregion


# region Sayının tam bölenlerini listeye çevir.
def tambolen(sayi: int):
    liste = []
    for i in range(2, sayi):
        if sayi % i == 0:
            liste.append(i)
    return liste

print(tambolen(
    int(input("Sayı giriniz:"))
))
# endregion


# region Kullanıcıdan adını ve soyadını al. Gmail oluştur.
def mailyaratici(kullanici: str):
    bolunenisim = kullanici.lower().split(" ")
    print(f'{bolunenisim[0]}.{bolunenisim[-1]}@gmail.com')

mailyaratici(
    input("İsminizi giriniz:")
)
# endregion

# region faktöriyel hesaplama tekrarı
def faktorr(x: int):
    faktoriyell = 1

    for i in range(1, x+1):
        faktoriyell *= i
    return faktoriyell

print(faktorr(
    int(input("Sayi girişi yapınız:"))
))
# endregion


# region kullanıcıdan kullanıcı adı ve password alalım login işlemi yapalım. kullanıcılar = [('beast', '123'), ('bear', '234'), ('savage', '987')]
kullanicilar = [('beast', '123'), ('bear', '234'), ('savage', '987')]

def giris(username: str, password: str):
    for i,j in kullanicilar:
        if i == username and j == password:
            print(f'Giriş başarılı. Hoşgeldiniz.')
            break
    else:
        print(f'Geçersiz kombinasyon tuşladınız.!')

giris(
    input("Kullanıcı adınızı giriniz:"),
    input("Şifrenizi giriniz:")
)
# endregion


# region Fonksiyonlarla öğrenci id'lerini uuid4 ile yaratıp CRUD işlemleri yapın
# Dictionary Structure
# students = {
#     'student_id': {
#         'first_name': 'fdasa',
#         'last name': 'fdsd',
#         'phone': 'fdsfds'
#     },
#     'student_id': {
#         'first name': 'fdasa',
#         'last_name': 'fdfds',
#         'phone': 'fdsfd'
#     }
# }


from uuid import uuid4
from pprint import pprint

students = {}

def create_students(isim: str, soyisim: str, telefon: str):
    ogrenci_id = str(uuid4())
    students[ogrenci_id] = {
        'İsim':isim,
        'Soyisim': soyisim,
        'Telefon': telefon
    }


def update_students(ogrenci_id: str, isim: str, soyisim: str, telefon: str):
    students.update({
        ogrenci_id: {
            'İsim': isim,
            'Soyisim': soyisim,
            'Telefon': telefon
        }
    })

    print(f'{ogrenci_id} başarıyla güncellenmiştir.')



def delete_studenst(ogrenci_id: str):
    del students[ogrenci_id]
    print(f'{ogrenci_id} başarıyla silinmiştir..!')



def main():
    while True:
        print(f'Yapmak istediğiniz işlemi seçiniz:\n'
                f'================\n'
                f'Create\n'
                f'List\n'
                f'Update\n'
                f'Delete\n'
                f'Exit')
        islem = input(f'Yapmak istediğiniz işlem türünü giriniz.').lower()

        if islem == 'create':
            isim = input("İsminizi giriniz:")
            soyisim = input("Soyisminizi giriniz:")
            telefon = input("Telefon numaranızı giriniz:")
            create_students(isim, soyisim, telefon)

        elif islem == 'list':
            pprint(students)

        elif islem == 'update':
            ogrenci_id = input("Öğrenci ID'nizi giriniz:")
            isim = input("İsminizi giriniz:")
            soyisim = input("Soyisminizi giriniz:")
            telefon = input("Telefon numaranızı giriniz:")
            update_students(ogrenci_id, isim, soyisim, telefon)

        elif islem == 'delete':
            ogrenci_id = input("Öğrenci ID'nizi giriniz:")
            delete_studenst(ogrenci_id)

        elif islem == 'exit':
            print(f'Uygulamadan çıkış yapılıyor..!')
            break

        else:
            print(f'Lütfen geçerli işlem türünü yazınız..!')

main()
# endregion


# region Liste içerisindeki çift sayıları 2 ile çarparak tek sayıları 3 ile çarparak yeni listeye ekle.
lst = [12, 11, 19, 2, 99]
yeni_lst = []
def cifttekbulma(x: int):
    if x % 2 == 0:
        return 'çift sayı'
    else:
        return 'tek sayı'


def listeyeeklemek(sonuc: str, x: int):
    if sonuc == 'cift sayi':
        yeni_lst.append(x * 2)
    else:
        yeni_lst.append(x * 3)


def main():
    for i in lst:
        sonuc = cifttekbulma(i)
        listeyeeklemek(sonuc, i)
    print(yeni_lst)

main()
# endregion


# region Kullanıcıdan alınan 3 adet sayıyı topladıktan sonra karesini alarak sonucu ekrana yaz
def toplam(a: int, b: int, c: int):
    return a + b + c

def karesini_alma(x: int):
    return x ** 2

def main():
    a = int(input("Sayi:"))
    b = int(input("Sayi:"))
    c = int(input("Sayi:"))
    result = toplam(a, b, c)
    Cevap = karesini_alma(result)
    print(f'İşlem sonucu = {Cevap}')

main()
# endregion


# region Aşağıdaki listede bulunan rakamların liste içerisinde geçme sıklığını bulun ve sözlük tipinde çıktı verin. rakamın kendisi key, geçme sıklığı value olacak şekilde olsun.
rakamlar = [1,1,1,5,5,3,1,3,3,1,4,4,4,4,2,2,4,3,5]

def gecmesikligi(list):
    sozluk = {}

    for i in rakamlar:
        if i in sozluk:
            sozluk[i] += 1
        else:
            sozluk[i] = 1

    for i, j in sozluk.items():
        print(f'{i}-----{j}')

gecmesikligi(rakamlar)
# endregion


# region Yukarıdaki sorunun benzeri.
sayilar = [10,10,10,5,5,3,1,3,3,1,4,4,4,4,24,26,84,3,5,24]

def sayisayaci(list):
    sayac_dict = {}

    for i in sayilar:
        if i in sayac_dict:
            sayac_dict[i] += 1
        else:
            sayac_dict[i] = 1

    for key, value in sayac_dict.items():
        print(f'{key}----{value}')

sayisayaci(sayilar)
# endregion


# region Söz öbeğinde tekrar eden kelimelerden arındırarak çıkı ver.
def tekrarengelleyici(x: str):
    liste = []

    for i in x.split(" "):
        if i not in liste:
            liste.append(i)

    sonuc = " ".join(liste)
    print(sonuc)

tekrarengelleyici(
    input("Söz öbeği giriniz:")
)
# endregion


# region Kullancıdan alınan söz öbeğindeki kelimeleri alfabetik olarak sıralayalım
def sozsiralama(x: str):
    liste = []
    for i in x.split(' '):
        if i not in liste:
            liste.append(i)
    liste.sort()
    yeni_liste = " ".join(liste)
    print(yeni_liste)

sozsiralama(
    input('Söz öbeği giriniz:')
)
# endregion


# region Kullanıcı giriş yapabilsin hem de kayıt olabilsin. yeni biri eklenebilsin. kişi login olabilsin. kayıt olan kişi sayısı kaldığı yerden devam edecek. isimler 1 kere kullanıcalak.
user_dict = {
    '1': {
        'user_name': 'beast',
        'password': '123'
    },
    '2': {
        'user_name': 'savage',
        'password': '123'
    },
}


def login(user_name: str, password: str):
    for key, value in user_dict.items():
        if value['user_name'] == user_name and value['password'] == password:
            print('Hoşgeldiniz!')
            break
    else:
        print('Geçersiz kullanıcı adı veya şifre!')


def get_user_name(users: dict):
    user_name_list = []

    for key, value in users.items():
        user_name_list.append(value['user_name'])

    return user_name_list


def sign_up(user_name: str, password: str):
    if user_name in get_user_name(user_dict):
        print("Bu kullanıcı adı zaten mevcut. Lütfen farklı bir kullanıcı adı seçin!")
    else:
        user_dict[str(len(user_dict) + 1)] = {
            'user_name': user_name,
            'password': password
        }
        print('Hesabınız başarıyla oluşturuldu!')


def main():
    while True:
        islem = input("Yapmak istediğiniz işlemi seçiniz:").lower()

        if islem == 'login':
            kullanici_adi = input("Kullanıcı adı:")
            password = input("Şifre:")
            login(kullanici_adi, password)

        elif islem == 'sign up':
            kullanici_adi = input("Kullanıcı adı:")
            password = input("Şifre:")
            sign_up(kullanici_adi, password)

        else:
            print(f'Lütfen geçerli bir işlem seçiniz!')


main()
# endregion


# region metindeki her bir kelimenin uzunluğunu hesaplayan ve bu uzunlukları bir liste olarak döndüren bir Python fonksiyonu yaz.
def metin_uzunluk_hesaplama(soz: str):
    liste = []

    for i in soz.split(" "):
        liste.append(len(i))
    return liste

sonuc = metin_uzunluk_hesaplama(
    input("Metin giriniz:")
)

print(sonuc)
# endregion


# region Verilen bir listedeki en büyük ve en küçük elemanları bulan ve bu elemanları bir demet olarak döndüren bir Python fonksiyonu yaz.
liste = [12, 5, 27, 8, 19]

def minmaxbulma(liste):
    liste.sort()
    min = liste[0]
    max = liste[-1]
    return (min, max)

sonuc = minmaxbulma(liste)
print(sonuc)
# endregion


# region Verilen liste içindeki sayıların toplamını hesaplayan fonksiyon yaz
liste = [1, 2, 3, 4, 5, 6]

def toplama(liste):
    toplamislemi = 0
    for i in liste:
        toplamislemi += i
    return toplamislemi

sonuc = toplama(liste)
print(sonuc)
# endregion


# region Verilen bir listedeki her bir sayının karesini hesaplayan ve bu kareleri içeren yeni bir liste döndüren bir Python fonksiyonu yaz
liste = [1, 2, 3, 4, 5]
def karehesaplama(list):
    new_list = []
    for i in liste:
        new_list.append(i ** 2)
    return new_list

sonuc = karehesaplama(list)
print(sonuc)
# endregion


# region metnin içindeki sesli harf sayısını ve sessiz harf sayısını hesaplayan bir Python fonksiyonu yaz.
metin = "Python programlama dili"

def seslisessizhesaplama(metin: str):
    sesliharf_sayisi = 0
    sessizharf_sayisi = 0

    sesliharfler = 'a,e,ı,i,o,ö,u,ü'

    for i in metin:
        if i.lower() in sesliharfler:
            sesliharf_sayisi += 1
        else:
            sessizharf_sayisi += 1
    return sesliharf_sayisi, sessizharf_sayisi


sonuc = seslisessizhesaplama(metin)
print(sonuc)
# endregion


# region Bir listedeki çift sayıları filtreleyen ve yeni bir listede saklayan bir Python fonksiyonu yaz.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtreleme(liste):
    yeni_liste = []
    for i in liste:
        if i % 2 == 0:
            yeni_liste.append(i)
    return yeni_liste

sonuc = filtreleme(liste)
print(sonuc)
# endregion


# region Bir metindeki her kelimenin baş harfini büyük harfe dönüştüren bir Python fonksiyonu yaz.
metin = "python programlama dili"

def basharfibuyutme(metin: str):
    yeni_metin = metin.title()
    return yeni_metin

sonuc = basharfibuyutme(metin)

print(sonuc)
# endregion


# region Bir metindeki her bir karakterin kaç kez geçtiğini hesaplayan ve sonucu bir sözlük olarak döndüren bir Python fonksiyonu yazalım.
metin = "python programlama dili"

def karakter_tekrari_hesaplama(metin: str):
    karakter_sozlugu = {}
    for i in metin:
        if i in karakter_sozlugu:
            karakter_sozlugu[i] += 1
        else:
            karakter_sozlugu[i] = 1
    return karakter_sozlugu

result = karakter_tekrari_hesaplama(metin)
print(result)
# endregion


# region listedeki en büyük 2 sayıyı döndürecek biçimde oluşturun.
liste = [1,5,10,2,6]

def buyuksayi(liste):
    liste.sort()
    return liste[-1], liste[-2]

sonuc = buyuksayi(liste)
print(sonuc)
# endregion


# region
def zamanverisi():
    saat = int(input("Saati giriniz:"))
    if saat >= 0 and saat <= 24:
        dakika = int(input("Dakika giriniz:"))
        if dakika >= 0 and dakika <= 60:
            return f"Giriş yapılan zaman: {saat}:{dakika}"
        else:
            print(f'Girdiğiniz dakika yanlış. Lütfen kontrol ediniz..!')
    else:
        print(f'Girdiğiniz saat yanlış. Lütfen kontrol ediniz..!')

result = zamanverisi()
print(result)
# endregion


# region Bir listedeki en büyük sayıyı bulan ve döndüren bir Python fonksiyonu yazalım.
liste = [12, 5, 27, 8, 19]

def enbuyuk(liste):
    liste.sort()
    liste[-1]
    return liste[-1]

result = enbuyuk(liste)
print(result)
# endregion


# region Basit Hesap Makinesi
def toplamaislemi(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam


def cikarmaislemi(*args):
    if len(args) < 2:
        raise ValueError('En az 2 sayı girilmesi gerekir.')

    sonuc = args[0]
    for i in args[1:]:
        sonuc -= i
    return sonuc



def carpmaislemi(*args):
    carpim = 1
    for i in args:
        carpim *= i
    return carpim


def bolmeislemi(*args):
    if len(args) < 2:
        raise ValueError('En az iki sayı girilmesi gerekir.')

    bolum = args[0]
    for i in args[1:]:
        if i == 0:
            raise ZeroDivisionError("Sıfıra bölme işlemi yapılamaz.")
        bolum /= i
    return bolum



def main():
    while True:
        try:
            islem = input("Hesap makinesine hoşgeldiniz. Lütfen yapmak istediğiniz işlemi seçiniz")
            if islem not in ('+','-','*','/'):
                raise ValueError("Lütfen geçerli işlem türü giriniz.")

            Degerler = (input("Lütfen istediğiniz sayıları boşluklu olarak giriniz:"))
            Degerler = [int(i) for i in Degerler.split(" ")]


            if islem == '+':
                print(toplamaislemi(*Degerler))

            elif islem == '-':
                print(cikarmaislemi(*Degerler))

            elif islem == '*':
                print(carpmaislemi(*Degerler))

            elif islem == '/':
                print(bolmeislemi(*Degerler))

        except ValueError as err:
            print(f"Hata..! {err}")

main()
# endregion
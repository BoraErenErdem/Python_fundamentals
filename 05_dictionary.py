

# Dictionary Example

# region Example 1
release_year_movie = {
    'Fight Club': 1999,
    'The Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2010,
    'Dune': 2011,
}


# region Herhangi bir value ekrana yaz

# 1.Yol
print(release_year_movie["Fight Club"])  # "Fight Club" indeksindeki value'yi yazar

# 2.Yol
print(f'Fight Club yayınlanma tarihi: {release_year_movie.get("Fight Club")}')  #.get() ile yazma

# 3.Yol
print(f'Fight Club yayınlanma tarihi: {release_year_movie["Fight Club"]}')

# endregion


# region Bütün keyleri ekrana yazdıralım
for key in release_year_movie.keys():
    print(key)
# endregion


# region Bütün valuesler ekrana yazdıralım
for value in release_year_movie.values():
    print(value)
# endregion


for value in release_year_movie:
    print(value)

# region Bütün hepsinin çıktısını ekrana yazdıralım (tuple şeklinde yazdırır)
print(release_year_movie.items())

for i in release_year_movie.items():
    print(i)

# endregion


# region Bütün hepsinin çıktısını ekrana yazdıralım
for key, value in release_year_movie.items():
    print(f'Film ismi: {key}\n'
        f'Çıkış Tarihi: {value}')


for i, j in release_year_movie.items():
    print(i,j)

# endregion
# endregion


# region Example 2
# Example 1
plakalar = {"kocaeli": 41, "istanbul": 34}
print(plakalar["kocaeli"])
print(plakalar["istanbul"])
plakalar["ankara"] = 6
print(plakalar)
plakalar["kocaeli"] = "yeni value atadım"


# Example 2
users = {
    "boraerdem": {
        "yaş": 22,
        "email": "erdemeren3460@gmail.com",
        "adres": "istanbul",
        "telefon": "123456"
    },
    "cinarerdem": {
        "yaş": 18,
        "email": "cinar3460@gmail.com",
        "adres": "alanya",
        "telefon": "123456"
    }
}

print(users["cinarerdem"])
print(users["cinarerdem"]["yaş"])

print(users.get("boraerdem"))
print(f' Kişi bilgisi: {users["boraerdem"]}')

for i in users.items():
    print(i)

print(users.items())

for i, j in users.items():
    print(i, j)


# endregion


# region Example 3
products = [
    {'name': 'Everlast Pro Boxing Gloves', 'price': 245},
    {'name': 'Everlast Training Gloves', 'price': 200},
    {'name': 'Everlast Heavy Bag', 'price': 445},
    {'name': 'Iphone 15 Pro Max', 'price': 85000},
    {'name': 'Samsun S24 Ultra', 'price': 80000},
    {'name': 'Lenovo X1 Carbon', 'price': 59000},
]


# products listesindeki tüm ürünlerin fiyatlarını toplayarak ekrana yazdırın
# 1.Yol
toplam = 0
for i in products:
    toplam += i["price"]
print(toplam)


# 2.Yol
toplam = 0
for i in products:
    toplam += i.get("price")
print(toplam)




# products listesinde ki ürünlerin fiyatı 30000'den büyük olan ürünleri listeleyin
# 1.Yol
for i in products:
    if i.get("price") >= 30000:
        print(f'Ürünler = {i.get("name")}  Fiyatları = {i.get("price")}')


# 2.Yol
for i in products:
    if i["price"] >= 30000:
        print(f'Ürünler = {i["name"]}  Fiyatlar = {i["price"]}')


# ürün adı içerisinde Everlast geçen ve fiyat aralığı 240 - ile 500 arasında olan ürünleri listeleyin
# 1.Yol
for i in products:
    if i.get("name").__contains__("Everlast"):  #__.contains__ komutu filtreler girilen değeri ya da karakteri arar
        if 240 < i.get("price") < 500:
            print(f' Ürün ismi = {i.get("name")}  Fiyatı = {i.get("price")}')

# 2.Yol
for i in products:
    if i["name"].__contains__("Everlast"):
        if 240 < i["price"] < 500:
            print(f' Ürün ismi = {i["name"]}  Fiyatı = {i["price"]}')


for i in products:
    if i["name"].__contains__("Everlast"):
        if 240 < i["price"] < 500:
            print(f' Ürün ismi = {i["name"]}  Fiyatı = {i["price"]}')
# endregion


# region Example 4
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}

# region Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayıp güncelleyin
yeni_ogrenci = {
    str(input("Numara giriniz:")): {
        'ad': str(input('Adınızı giriniz:')),
        'soyad': str(input('Soyadınızı giriniz:')),
        'telefon': str(input("Telefon numaranızı giriniz:"))
    }
}

ogrenciler.update(yeni_ogrenci)
print(ogrenciler)
# endregion


# endregion


# region Telefon defterindeki bilgilere kullanıcının rehberdeki kişiye ulaşmasını sağla.
telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                    "mehmet su": "0543 543 42 42",
                    "seda naz" : "0533 533 33 33",
                    "eda ala"  : "0212 212 12 12"}

kullanici = input("Numara sorgulamak için kişi ismi giriniz: ")
if kullanici in telefon_defteri:
    print(f'{kullanici} kişisinin telefon numarası: {telefon_defteri.get(kullanici)}')
else:
    print(f'{kullanici} kişisi listede yer almıyor...')
# endregion


# region Example 6
sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu"}

# region sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız
meslekler = sozluk.copy()
print(meslekler)
# endregion


# region sozluk isimli sözlüğün değerlerini ekrana yazdırınız.
print(sozluk.values())
# endregion


# region sozluk isimli sözlüğü içi boş bir sözlük hâline getiriniz.
sozluk.clear()
# endregion


# region sozluk isimli sözlüğe Matematikçi: Cahit Arf ikilisini ekleyiniz.
sozluk["Matematikçi"] = "Cahit Arif"
# endregion


# region sozluk isimli sözlüğün içinde sanatçı anahtarının olup olmadığını sorgulayınız.
# 1.Yol
print(sozluk.get("sanatçı"))

# 2.Yol
if 'sanatçı' in sozluk:
    print("anahtar var")
else:
    print("anahtar yok")
# endregion


# region sozluk isimli sözlüğün bilim insanı anahtarındaki değeri Canan Dağdeviren olarak değiştiriniz.
sozluk["Bilim insanı"] = "Canan Dağdeviren"
print(sozluk)
# endregion


# region  sozluk isimli sözlüğün şair anahtarı ile eşleşen değeri ekrana yazdırınız.
# 1.Yol
print(sozluk.get("Şair"))

# 2.Yol
print(sozluk["Şair"])
# endregion


# endregion


# region Example 7
onemli_bilgiler = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}

# region önemli_bilgiler isimli sözlüğün değerlerini ekrana yazdırınız.
print(onemli_bilgiler.values())
# endregion


# region önemli_bilgiler isimli sözlükten Acil Çağrı Merkezi anahtarını ve değerini siliniz.
onemli_bilgiler.pop("Acil Çağrı Merkezi")
print(onemli_bilgiler)
# endregion


# region önemli_bilgiler isimli sözlükte Sağlık Bakanlığı İletişim Merkezi olup olmadığını sorgulayınız.
#"1.Yol
print(onemli_bilgiler.get("Sağlık Bakanlığı İletişim Merkezi"))

#2.Yol
if "Sağlık Bakanlığı İletişim Merkezi" in onemli_bilgiler:
    print("True")
else:
    print("False")
# endregion


# region Alt alta sıralayın
for i,j in onemli_bilgiler.items():
    print(i,j)
# endregion

# endregion


# region Öğrenci sözlüğü oluşturun ve her yeni öğrenci kaydında sözlüğü güncelleyin
ogrenci = {}

while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz: (exit / create) ")
    if islem == 'exit':
        print("Döngüden çıkılıyor ve sonuç yazdırılıyor.")
        break
    elif islem == 'create':
        print('Öğrenci kayıt bölümüne hoşgeldiniz!')
        yeni_ogrenci = {
            str(input("Numara giriniz:")): {
                'ad': input("Ad girişi yapınız:"),
                'soyad': input("Soyad girişi yapınız:"),
                'telefon': input("Telefon numarası girişi yapınız:")
            }
        }

        ogrenci.update(yeni_ogrenci)
print(ogrenci)
# endregion


# region öğrenci id'lerini örnekteki sözlük tipine uygun olarak uuid4 ile yaratın

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


from pprint import pprint
from uuid import uuid4

ogrenciler = {}
while True:
    print("Manuel Giriş:\n"
            "/////////////\n"
            "Yarat\n"
            "Güncelle\n"
            "Listele\n"
            "Sil\n"
            "Çıkış")

    islem = input("Yapmak istediğiniz işlemi seçiniz:").lower()

    if islem == 'yarat':
        yeni_ogrenci = {
            str(uuid4()): {
        'adi' : input("Adını giriniz:"),
        'soyadi' : input("Soyadını giriniz:"),
        'telefon' : input("Telefon numarasını giriniz:")
        }
    }
        ogrenciler.update(yeni_ogrenci)

    elif islem == 'listele':
        pprint(ogrenciler)

    elif islem == 'güncelle':
        ogrenci_id = input("Güncellenecek öğrenci ID'sini giriniz:")
        if ogrenci_id in ogrenciler:
            ogrenciler[ogrenci_id].update({
                'adi': input("Yeni adını giriniz:"),
                'soyadi': input("Yeni soyadını giriniz:"),
                'telefon': input("Yeni telefon numarasını giriniz:")
            })
            print(f'{ogrenci_id} başarıyla güncellenmiştir..!')
        else:
            print(f'{ogrenci_id} ID\'siyle eşleşen öğrenci bulunamadı.')

    elif islem == 'sil':
        ogrenci_id = input("Öğrenci id'sini giriniz: ")
        del ogrenciler[ogrenci_id]
        print(f'{ogrenci_id} başarıyla silinmiştir!')

    elif islem == 'çıkış':
        print("Programdan çıkış yapılıyor.....")
        break

    else:
        print("Geçerli işlem türünü giriniz.!")
# endregion


# region Example 10
kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlık': ['Front-End']
}

kullanici2 = {
    'ad': 'Gökçe',
    'soyad': 'Gün',
    'uzmanlık': ['Tasarım']
}

kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlık': ['Front-End']
}

# region Ferhat Ibrik kullanıcısının uzmanlık alanın döndür
print(kullanici1.get('uzmanlık'))

print(kullanici1["uzmanlık"])
# endregion


# region Front-End alanındaki uzmanların isimlerini döndür
kullaici_listesi = [kullanici1, kullanici2, kullanici3]
for i in kullaici_listesi:
    if i["uzmanlık"].__contains__("Front-End"):
        print(i)


for i in kullaici_listesi:
    if i.get("uzmanlık").__contains__("Front-End"):
        print(i)
# endregion


# region Mesut kullanıcısı uzmanlığına 'yazılım' bilgisini ekledi, bilgileri güncelle
kullanici3.get("uzmanlık").append("yazılım")
print(kullanici3)
# endregion


# region birden fazla uzmanlık alanı olan kullanıcıları döndür
for i in kullaici_listesi:
    if len(i.get("uzmanlık")) > 1:
        print(i)
# endregion
# endregion


# region Kitap bilgileri tutan sözlük oluşturun. her kitap için kitap adı, yazarı, yayın yılı ve ISBN numarası olsun. en az 3 kitap girilsin ve bilgiler ekrana yazdırılsın
from pprint import pprint

kitap_bilgileri = {}

while True:
    islem = input("İşlem türünü giriniz (exit/create/list): ")

    if islem == 'exit':
        print("Programdan çıkılıyor..")
        break
    elif islem == "create":
        print("Sisteme hoşgeldiniz.")
        kitap_adi = input("Kitap Adı: ")
        yazarin_adi = input("Yazar: ")
        yayin_yili = input("Yayın Yılı: ")
        ISBN_numarasi = input("ISBN Numarası: ")

        yeni_kitap = {
            'kitap adı': kitap_adi,
            'yazarı': yazarin_adi,
            'yayın yılı': yayin_yili,
            'ISBN numarası': ISBN_numarasi
        }

        kitap_bilgileri.update({kitap_adi: yeni_kitap})
        pprint(kitap_bilgileri)

    elif islem == 'list':
        pprint(kitap_bilgileri)
        break
# endregion


# region tek bir için öğrenci bilgi sistemi tasarla.öğrencinin bir öğrenci id'si, adı, soyadı ve aldığı derslerin bilgileri bulunsun. Her dersin adı, öğretmeni var. buna göre yap.
from pprint import pprint
from uuid import uuid4
ogr_bilgi_sistemi = {}
while True:
    islem_turu = input("İşlem türünü giriniz(çıkış,oluştur,listele):")
    if islem_turu == 'çıkış':
        print("Sistemden çıkış yapılıyor..")
        break
    elif islem_turu == 'listele':
        pprint(ogr_bilgi_sistemi)
    elif islem_turu == 'oluştur':

        yeni_ogr = {
        str(uuid4()): {
            'ad': input("Adı:"),
            'soyad': input("Soyad:"),
            'aldığı dersler': {
                input("Aldığı dersler:"): {
                    "ögretmen": input("öğretmen ismi:")
                }
            }
        }
    }

        print(ogr_bilgi_sistemi.update(yeni_ogr))
# endregion


# region Bir film bilgi sistemi uygulaması yapalım. film adı, yönetmen, yayın yılı ve oyuncular bilgilerini içersin. Kullanıcıdan bu bilgileri alarak bir film ekleyelim.
from uuid import uuid4
film_bilgileri = {}

film_id = str(uuid4())
film_adi = input("Film adını giriniz:")
yonetmen = input("Yönetmen adı giriniz:")
yayin_yili = input("Yayın yılını giriniz:")
oyuncular = input("Oyuncu isimlerini lütfen virgülle ayırarak giriniz:").split(",")

film_bilgileri[film_id] = {
    'film ID': film_id,
    'film adı': film_adi,
    'yönetmen': yonetmen,
    'yayın yılı': yayin_yili,
    'oyuncular': oyuncular
}

print(film_bilgileri)
# endregion


# region Bir restoran menüsü oluştur. Yemek ismi, fiyatı ve içeriği olsun. Kullanıcıdan bir yemek ismi alın ve bu yemeğin fiyatını ve içeriğini listele. Menüye yemek eklesin.
from pprint import pprint
restoran_menusu = {}
print("Lütfen siparişiniz ile ilgili yapmak istediğiniz işlemi belirtiniz:\n"
        "*****************\n"
        "Sepetim\n"
        "Oluştur\n"
        "Güncelle\n"
        "Sil\n"
        "Çıkış")

while True:
    siparis_islemi = input("Sipariş işleminizi girmek için buraya tıklayın:").lower()

    if siparis_islemi == 'oluştur':
        siparis_adi = input("Siparişe isim veriniz:")
        Yemek_adi = input("İstediğiniz yemeği giriniz:")
        icerigi = input("Yemek içeriğini giriniz:")
        fiyati = input("Fiyatı:")

        restoran_menusu[siparis_adi] = {
            'Yemek adı': Yemek_adi,
            'İçeriği': icerigi,
            'Fiyatı': fiyati
        }

    elif siparis_islemi == 'sepetim':
        print(restoran_menusu)

    elif siparis_islemi == 'güncelle':
        siparis_adi = input("Sipariş adını giriniz:")
        Yemek_adi = input("Yeni istediğiniz yemeği giriniz:")
        icerigi = input("Yemek içeriğini giriniz:")
        fiyati = input("Fiyatı:")

        restoran_menusu.update({
            'Sipariş adı': siparis_adi,
            'Yemek adı': Yemek_adi,
            'İçeriği': icerigi,
            'Fiyatı': fiyati
        })

        print(f'{siparis_adi} adlı siparişiniz başarıyla oluşturuldu.')
    elif siparis_islemi == 'sil':
        siparis_adi = input("Sipariş adını giriniz:")
        del restoran_menusu[siparis_adi]

    elif siparis_islemi == 'çıkış':
        print("Uygulamadan çıkılıyor..Yine bekleriz...")
        break

    else:
        print("Lütfen geçerli sipariş türünü giriniz..!")
# endregion


# region öğrenci not defteri uygulaması yap. Her öğrencinin bir ID'si olacak ve bu ID'ye göre öğrenci bilgileri saklanacak.ad, soyad, doğum yılı, sınıfı, ders adı ve notu.
from uuid import uuid4
from pprint import pprint

not_defteri = {}
print("Not defterine hoşgeldiniz. Lütfen devam etmek istediğiniz işlemleri seçiniz:\n"
        "---------WELCOME--------\n"
        "oluştur\n"
        "güncelle\n"
        "listele\n"
        "sil\n"
        "çıkış")

while True:
    islem = input("Yapmak istediğiniz işlemi giriniz:")

    if islem == 'oluştur':
        ogrenciID = str(uuid4())
        ad = input("Adı:")
        soyad = input("Soyadı:")
        dogum_yili = input("Doğum yılı:")
        sinifi = input("Sınıfı:")
        dersleri = input("Aldığı dersleri ve notları virgülle ayırarak giriniz:").split(",")

        not_defteri[ogrenciID] = {
            'Ad': ad,
            'Soyad': soyad,
            'Doğum yılı': dogum_yili,
            'Sınıfı': sinifi,
            'Dersleri': dersleri
        }

        print("Öğrenci kaydı başarıyla oluşturuldu.")

    elif islem == 'listele':
        pprint(not_defteri)

    elif islem == 'güncelle':
        ogrenciID = input("Öğrenci ID'sini giriniz:")
        ad = input("Adı:")
        soyad = input("Soyadı:")
        dogum_yili = input("Doğum yılı:")
        sinifi = input("Sınıfı:")
        dersleri = input("Aldığı dersler ve notlar:")

        not_defteri.update({
            ogrenciID: {
                'Ad': ad,
                'Soyad': soyad,
                'Doğum yılı': dogum_yili,
                'Sınıfı': sinifi,
                'Dersleri': dersleri
            }
        })

        print(f'{ogrenciID} başarıyla güncellenmiştir.')

    elif islem == 'sil':
        ogrenciID = input("Öğrenci ID'sini giriniz:")
        not_defteri.pop(ogrenciID)
        print(f'{ogrenciID} başarıyla silinmiştir.')

    elif islem == 'çıkış':
        print("Programdan çıkılıyor...")
        break

    else:
        print("Lütfen geçerli işlem türünü giriniz!")
# endregion


# region Öğrenci uygulaması oluşturalım. Her öğrencimizin adı, soyadı, yaş ve hobileri yer alsın. öğrenciler için arayüz oluştur.
ogr = {}

print("Öğrencim uygulamasına hoşgeldiniz.Lütfen devam etmek istediğiniz işlemi seçiniz:\n"
        "----H O Ş G E L D İ N İ Z----\n"
        "1:Yeni öğrenci ekle\n"
        "2:Öğrencileri listele\n"
        "3:Öğrencileri güncelle\n"
        "4:Öğrenci sil\n"
        "5:Programdan çıkış yap")

while True:
    secim = input("Yapmak istediğiniz işlem numarasını giriniz:").lower()

    if secim == '1':
        adi = input("Adınız:")
        soyadi = input("Soyadınız:")
        yasi = input("Yaşınız:")
        hobiler = input("lütfen hobilerinizi virgülle belirtiniz:").split(",")

        ogr[adi] = {
            'Adı': adi,
            'Soyadı': soyadi,
            'Yaşı': yasi,
            'Hobileri': hobiler
        }

        print(f'{ogr[adi]} isimli öğrenci başarıyla kaydedildi.')

    elif secim == '2':
        print(ogr)

    elif secim == '3':
        adi = input("Güncellenecek öğrencinin adını giriniz:")
        if adi in ogr:
            soyadi = input("Soyadınız:")
            yasi = input("Yaşınız:")
            hobiler = input("lütfen hobilerinizi virgülle belirtiniz:").split(",")

            ogr.update({
                adi: {
                    'Soyadı': soyadi,
                    'Yaşı': yasi,
                    'Hobileri': hobiler
                }
            })

            print(f'{ogr[adi]} başarıyla güncellendi.')

        else:
            print("Güncellenecek öğrenci bulunamadı..!")

    elif secim == '4':
        adi = input("Öğrencinin adını giriniz:")
        del ogr[adi]
        print(f'{adi} adlı öğrenci başarıyla silinmiştir.')

    elif secim == '5':
        print("Programdan çıkış yapılyor..!")
        break

    else:
        print("Lütfen menüde yer alan geçerli seçimleri yapınız.")
# endregion


# region retorant menüsü oluştur. 3 farklı yemek olsun ve adları, fiyatları, içeriği olsun. menü oluştur ve sipariş al. siparişten sonra fiyatı ekrana yazsın
from pprint import pprint
restorant_menu = {
    'Soslu Makarna': {
        'içeriği': ['napoliten sos, domates salçası, tuz, sirke, şeker, karabiber, soğan, sarımsak'],
        'Fiyat': 120
    },
    'Patates Köfte': {
        'içeriği': ['1 adet yumurta, 1 adet orta boy soğan, kimyon, karabiber, yarım demet maydonoz, hafif acılı elma dilim patates'],
        'Fiyat': 180
    },
    'Mercimek Çorbası': {
        'içeriği': ['1 adet soğan, 1 adet havuç, 1 adet patates, tuz, karabiber, 2 kaşık sıvıyağ'],
        'Fiyat': 80
    }
}
print("Restorantımıza hoşgeldiniz.\n"
        "Sipariş oluşturmak için: 1\n"
        "Siparişlerimi görüntülemek için: 2\n"
        "Siparişlerimi güncellemek için: 3\n"
        "Siparişimi silmek için: 4\n"
        "Çıkış için: 5")

while True:
    musteri = input("Yapmak istediğinizi işlem numarasını giriniz:")

    if musteri == '1':
        print("Mevcut menü:")
        pprint(restorant_menu)
        siparis_ani = input("İstediğiniz menüleri girin:")
        if siparis_ani == 'Soslu Makarna':
            print(f'Ödeyeceğiniz fiyat: {restorant_menu['Soslu Makarna'].get("Fiyat")}')
        elif siparis_ani == 'Patates Köfte':
            print(f'Ödeyeceğiniz fiyat: {restorant_menu['Patates Köfte'].get("Fiyat")}')
        elif siparis_ani == 'Mercimek Çorbası':
            print(f'Ödeyeceğiniz fiyat: {restorant_menu['Mercimek Çorbası']["Fiyat"]}')
        else:
            print("Sadece menüde yer alan yemekleri tercih edebilirsiniz..!")

    elif musteri == '2':
        pprint(restorant_menu)

    elif musteri == '3':
        yemek_adi = input("Yeni yemek adını giriniz:")
        if yemek_adi in restorant_menu:
            print("Siparişiniz başarıyla güncellenmiştir..")
        else:
            print("Sadece menümüzde bulunan yemeklerden sipariş verebilirsiniz!")

    elif musteri == '4':
        yemek_adi = input("Silmek istediğiniz yemeğin adını giriniz:")
        del restorant_menu[yemek_adi]
        print("Başarıyla silinmiştişr..")

    elif musteri == '5':
        print("Çıkış yapılıyor. Yine bekleriz...")
        break

    else:
        print("Lütfen geçerli numaraları giriniz..!")
# endregion
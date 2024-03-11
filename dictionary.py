

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
# endregion


# region Bütün hepsinin çıktısını ekrana yazdıralım
for key, value in release_year_movie.items():
    print(f'Film ismi: {key}\n'
        f'Çıkış Tarihi: {value}')
# endregion


# region Sözlüklerle ilgili alıştırmalar
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





# region Example
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


# region Example
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



# region Example
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
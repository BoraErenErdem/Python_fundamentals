

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
print(f'Fight Club yayınlanma tarihi: {release_year_movie.get("Fight Club")}')

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
# endregion



# region Bir öğrenci veritabanı oluşturun. Her öğrencinin adı, soyadı, sınıfı ve aldığı ders notları bulunmalıdır. Yeni öğrencinin bilgilerini ekleyin ve bir öğrencinin notlarını güncelleyin. Son olarak, tüm öğrencilerin adını, soyadını ve sınıfını ekrana yazdırın.

ogrenci_veritabani = {
    'birinci öğrenci': {
        'isim': 'Bora',
        'soyadı': 'Erdem',
        'sınıf': '1',
        'notlar': {
            'matematik': 85,
            'fizik': 75,
            'kimya': 55
        }
    },
    'ikinci öğrenci': {
        'isim': 'Eren',
        'soyisim': 'Kovanski',
        'sınıf': '2',
        'notlar': {
            'matematik': 67,
            'fizik': 98,
            'kimya': 45
        }
    },
    'üçüncü öğrenci': {
        'isim': 'ahmet',
        'soyisim': 'canikci',
        'sınıf': '3',
        'notlar': {
            'matematik': 44,
            'fizik': 56,
            'kimya': 66
        }
    }
}


# Yeni bir öğrenci ekleyin

yeni_ogrenci = {
    'dördüncü öğrenci': {
        'isim': 'Mahmut',
        'soyadı': 'Kurt',
        'sınıf': '4',
        'notlar': {
            'matematik': 45,
            'fizik': 39,
            'kimya': 17
        }
    }
}


# endregion




list = ["abc", 123, 12.6]
print(list)
type(list)

print(list[0])
print(list[0:2])


x = "Ali"
y = "Veli"
x + y
x + " " + y

# -------------------------------------------------------------------------- #
### str ###
# str ifadelerde kullanılan metodlar

x = "Bora erdem"
len(x)  # len() operatörü stringin uzunluğunu bulmak için kullanılır

# index örnekleri
x[0]
x[3]
x[-1]
x[1:3]
x[2:]
x[:4]
x[::-1]
# karakterin stringde olup olmadığını kontrol etmek için in operatörü kullanılır
"a" in x
"A" in x
# aynı şekilde kontrol etmek için olumsuzunu da kullanabilirisin
"c" not in x
"B" not in x

# string metodları
print(x.upper())  # karakterlerin hepsini büyütmek için kullanılır
print(x.lower())  # karakterlerin hepsini küçültmek için kullanılır
print(x.replace("dem", "en"))  # string yerine başka bir string koymak için kullanılır. önce değişmek istediğin ifadeyi yaz sonra yerine getireceğin ifadeyi yaz
print(x.index("r"))  # karakterin indexini bulmak istersek kullanırız
print(x.title())  # her kelimenin baş harfi büyük karaktere çevrilir
print(x.capitalize())  # sadece ilk kelimenin baş harfi büyük olur gerisi küçük olur
print(x.split())  # .split() metodu string ifadeleri ayırıp parçalıyor ve liste oluşturuyor
print((x.join()))  # .join() metodu string ifadelerde kullanılır. Liste elemanlarını birleştirir (splitin tam tersi)
print(x.isalpha())  # isalpha() metodu, bir string içindeki tüm karakterlerin alfabetik olup olmadığını kontrol eder. Eğer tamamen harflerden oluşuyorsa True, aksi takdirde False döndürür. Ayrıca string içinde boşluk varsa yine False çıktısı verir


# -------------------------------------------------------------------------- #
### Listeler ###

# sort() metodu orijinal listeyi değiştirirken, sorted() fonksiyonu orijinal listenin kopyasını sıralar ve bu sıralanmış kopyayı döndürür, orijinal listeyi değiştirmez.
# sort() metodu return olduğu zaman "None" değeri döndürür. sordet() fonksiyonu ise sıralanmış kopyayı döndürür ve sıralanmış bir liste döndürmüş olur.

# index örnekleri
liste = ["bora", 2001, True]
type(liste)
liste[0]
liste[-1]
liste[1:2]
liste[0:2]
liste[1:]
liste[:1]

len(liste)  # listenin uzunluğunu öğrenmek için kullanılır
liste = ["bora", 2001, True, [1,2,3]]  # NestedList: listenin içine başka bir liste yazılabilir
len(liste)
liste[3][0]  # listenin içindeki listenin bileşenlerine erişmek için önce listenin olduğu indexi yazarız sonrasında diğer bulmak istediğimiz indexi yazarız
liste[3][0:2]

nestedlist = [1,5,"bora",4,[6,"z"]]  # NestedList örneği
nestedlist[1]
nestedlist[4]
nestedlist[4][0]
nestedlist[4][0:2]

# + operatörü iki listeyi birleştirir
liste = ["bora", 2001, True]
x = [1,2,3]
liste + x

# in operatörü bir bileşenin listede olup olmadığını denetler. not in ile de kullanılabilir
2001 in liste
"1234" in liste
"eren" not in liste
2001 not in liste

# listeye bileşen eklenebilir
liste[0] = "erdem"
liste
liste[1] = 2002
liste

# liste metodları
isimler = ["Bora", "Ahmet", "Ayşe"]
maaslar = [2000, 3000, 4000]
isimler.append("Mert")  # append() metodu listeye bileşen eklemek için kullanılır
isimler
maaslar.append(7000)  # .append() metodu ile maaslara bileşen ekledik
maaslar

# .extend() metodu listeye başka listenin eklenmesini sağlar
isimler.extend(maaslar)
isimler
# .insert() metodu herhangi bir bileşeni istediğimiz indexe yerleştirmemizi sağlar. önce ekleyeceğimiz yerin indexini yazarız sonra ekleyeceğimiz bileşeni yazarız
isimler.insert(1, "Veli")
isimler
# .index() metodu listedeki bir bileşenin indexini gösterir
isimler.index("Bora")
# .sort() metodu listedeki bileşenleri küçükten büyüğe ya da alfabetik sıraya göre sıralar
isimler.sort()
isimler
# .reverse() metodu listenin bileşenlerini sondan başa doğru döndürür
isimler.reverse()
isimler
maaslar.reverse()
maaslar
# .remove() metodu listedeki bileşeni siler ve bileşene bir daha ulaşılamaz
isimler.remove("Mert")
isimler
maaslar.remove(7000)
maaslar
# pop() metodu indexi verilen bileşeni listeden çıkarır fakat çıkarılan bileşen bellekte saklanır
isimler.pop(0)
isimler
maaslar.pop(0)
maaslar
# del() metodu indexi verilen bileşeni listeden çıkarır
del(isimler[1])
isimler
del(maaslar[1])
maaslar
# bütün listeyi silmek istersen de del yazıp yanına listenin ismini yaz
del isimler  # isimler listesini sildik


arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]
len(arabalar)
arabalar[0]
arabalar[-1]
arabalar[3] = "Toyota"  # Mazda değerini Toyota ile değiştirdim
arabalar[-2]
arabalar[0:3]
arabalar[2:4] = "Toyota", "Renault"  # son 2 değeri Toyota ve Renault ile değiştirdik
# listeye 2 değer ekleme
a = ["Audi" , "Nissan"]
arabalar + a
arabalar[::-1]  # tersten yazdırma
del arabalar[-1]




names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]
names.append("Cenk")
names.insert(0 , "Sena")
names.pop(4)
del(names[3])
names.remove("Deniz")
names.index("Deniz")
"Ali" in names
names.reverse()
names.sort()
years.sort()
z = "Chevrolet,Dacia"
names.append(z)
years.sort()
years[3]
years[0]
min(years)
max(years)
years.count(1998)
years.clear()




website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
len(course)

website[7:10]

website[21:25]

len(course)
course[:15]
course[50:]

course[::-1]  # course ifadesini tersten yazdırma

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"
print(f'Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}')

x = "Hello world"
x.replace("w", "W")

"abc"*3





esyalar = [['dolap', 'ütü', 'fön'],
            ['telefon', 'televizyon', 'klima'],
            ['ütü masası', 'bulaşık makinası', 'çamaşır makinası']]

print(f'eşyalar listesinin orjinali = {esyalar}')
print()

liste = []

for i in esyalar:
    for j in i[::-1]:
        liste.append(j)
print(f"eşyalar listesinin herbir elemanının ters çevrilmiş şeklini tek bir liste haline getirdik = {liste}")






# Tuple (Demetler)

# () parantez ile gösterilir.
# değiştirilemezler

x = (1, 2, 3, 4, 5)
print(type(x))
print(x[2])
print(x[1:3])
print(len(x))


x = (1, 2, 3, 4, 5)
y = ('bora', 'eren', 'erdem')
z = x + y
print(z)


a = (1, 2, 5.6, 'daytona', 2, 54, 7,'daytona', 2)
a.count(2)  # 2 sayısı kaç kere tekrarlanıyor ona baktık



# Sözlük (Dictionary)
from pprint import pprint
dil = {
        "Ali": "ingilizce",
        "Can": "almanca",
        "Ayşe":"fransızca"
    }

len(dil)

dil["Ali"]
dil["Can"]
dil["Veli"]  # Sözlükte "Veli" sözcüğü yer almadığı için hata verir
dil["Veli"] = "ispanyolca"  # Veli sözcüğü ve ispanyolca anahtarını ekledik
dil["Ali"] = "rusça"  # Ali anahtarının değerini rusça olarak değiştirdik

dil.keys()  # anahtarlar ekrana gelir
dil.values()  # değerler ekrana gelir
dil.items()  # hem anahtar hem değeri alırız (tuple şeklinde)
dil.get("Ali")  # anahtarın değerini .get() kullanarakta alabiliriz
dil.clear()  # dil sözlüğündeki bileşenlerin hepsini siler
dil.__contains__("Ali")  # .contains() metodu filtrelemeye yarar
dil.update()  # .update() metodu bir sözlüğü başka bir sözlükle güncellemek veya bir sözlüğe yeni anahtar-değer çiftleri eklemek için kullanılır
dil.copy()  # .copy() metodu sözlüğün bir kopyasını oluşturur ve bu kopyayı yeni bir değişkene atar
dil.pop("Ali")  # pop() metodu belirli bir anahtarı sözlükten çıkarır ve değerini döndürür. Eğer anahtar bulunamazsa, bir hata fırlatır veya belirtilen bir varsayılan değeri döndürür




# Set (Kümeler)

my_List = [1,2,3,1,2,3]
my_List  # listelerde aynı ifadeyi birden fazla kez yazabiliriz ve bu bir sorun teşkil etmez ancak setlerde aynı ifadeyi birden fazla kez yazamayız..!

my_SetList = set(my_List)
my_SetList  # Tekrarlanan ifadeleri attı ve her ifadenin sadece 1 kere yazılmasına izin verdi

my_set = {'a', 'b', 'c', 'a'}
my_set  # Sözlük parantezlerini kullanırız ancak setlerde key : value ilişkisi yoktur. Ayrıca değerleri tekrar edemez.

bos_set = set()  # Boş set tanımlamak istersek böyle yapmalıyız. {} böyle yaparsak python bunu boş bir dict diye algılar.

bos_set.add(10)
bos_set.add(10)
bos_set.add(20)
bos_set  # Boş set'in içine değerler ekledik. Ayrıca set'ler indexlenemezler.

meyveler = {'portakal', 'elma', 'muz'}

for i in meyveler:  # set veri tipi indexlenemez. İterasyonla (for döngüsüyle) elemanlarına ulaşılabilir.
    print(i)

meyveler.add('çilek')
print(meyveler)

meyveler.update(['ananas', 'mango'])  # Liste şeklinde update() metoduyla meyveler set'ine eklenildiğinde rastgele düzende yerleştirir.
print(meyveler)
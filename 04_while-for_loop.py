

# while - For Loops Example


# While Loop Example

# region 0 ve 100 arasındaki sayıları yaz
sayac = 0
while sayac < 100:
    print(sayac)
    sayac += 1
# endregion


# region 1 ve 100 arasındaki sayıları topla
sayac = 1
toplam = 0
while sayac <= 100:
    toplam += sayac
    sayac += 1
print(toplam)
# endregion


# region 1 ve 100 arasındaki çift ve tek sayıların toplamını ayrı ayrı yaz
sayac = 1
cift_toplam = 0
tek_toplam = 0
while sayac <= 100:
    if sayac % 2 == 0:
        cift_toplam += sayac
    else:
        tek_toplam += sayac
    sayac += 1
print(cift_toplam)
print(tek_toplam)
# endregion


# region 0 ile 100 arasındaki sayılardan kaç tanesi çift kaç tanesi tek
sayac = 0
cift = 0
tek = 0
while sayac <= 100:
    if sayac % 2 == 0:
        cift += 1
    else:
        tek += 1
    sayac += 1
print(f' Çift sayılar: {cift}')
print(f' Tek sayılar: {tek}')
# endregion


# region Kullanıcıdan işlem türü al (e, +, -, *, /). Alınan işlem türüne göre ilgili işlemi yap ve çıktısını ekrana yaz. Kullanıcı 'e' işlemini gönderene kadar sınırsız sayıda 4 işlem yap.(match- case ile de yapabilirsin)
while True:
    islem_turu = input("İşlem türünü giriniz: ")
    x = int(input("Sayı giriniz: "))
    y = int(input("Sayı giriniz: "))
    if islem_turu == "e":
        print("Döngüden çıkılmıştır! ")
        break
    elif islem_turu == "*":
        carpim = x * y
        print(f' Çarpım = {carpim}')
    elif islem_turu == "+":
        toplam = x + y
        print(f' Toplam = {toplam}')
    elif islem_turu == "-":
        cikarma = x - y
        print(f' çıkarma = {cikarma}')
    elif islem_turu == "/":
        bolme = x / y
        print(f' Bölüm = {bolme}')
    else:
        print("Doğru işlem türünü giriniz..! ")
# endregion


# region Kullanıcıdan alınan sayı asal mı değil mi yaz
x = int(input("Sayı giriniz: "))
if x <= 0:
    print("Sıfır ve negatif asal sayı değildir! ")
else:
    asal_mi = True
    if x == 1:
        asal_mi = False
    else:
        asal_mi = True
    sayac = 2
    while sayac < x:
        if x % sayac == 0:
            asal_mi = False
            break
        sayac += 1
    if asal_mi:
        print(f'{x} asaldır. ')
    else:
        print(f'{x} asal değildir. ')
# endregion


# region Kullanıcıdan alınan sayının faktöriyelini hesaplayıp yaz
x = int(input(" Sayı giriniz: "))
faktoriyel = 1
sayac = 1
if x < 0:
    print("Negatif sayıların faktöriyeli tanımsızdır.")
elif x == 0:
    print(" Sıfır faktöriyel her zaman 1'e eşittir. ")
else:
    while sayac <= x:
        faktoriyel *= sayac
        sayac += 1
    print(f' {x} sayısının faktöriyeli = {faktoriyel} ')
# endregion


# region Başlangıç ve bitiş değerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yaz
baslangic = int(input("Başlangıç değeri giriniz: "))
bitis = int(input("Bitiş değeri giriniz: "))
sayac = baslangic
while sayac < bitis:
    sayac += 1
    if sayac % 2 != 0:
        print(sayac)
# endregion


# region 1 ile 100 arasındaki sayıları azalan şekilde yaz
sayac = 100
while sayac > 0:
    sayac -= 1
    print(sayac)
# endregion


# region Kullanıcıdan alınan 5 sayıyı ekrana sıralı şekilde yaz
sayi1 = int(input(" Sayı giriniz: "))
sayi2 = int(input(" Sayı giriniz: "))
sayi3 = int(input(" Sayı giriniz: "))
sayi4 = int(input(" Sayı giriniz: "))
sayi5 = int(input(" Sayı giriniz: "))
sayac = 0
while sayac < 5:
    print(sayi1)
    sayac += 1
    print(sayi2)
    sayac += 1
    print(sayi3)
    sayac += 1
    print(sayi4)
    sayac += 1
    print(sayi5)
    sayac += 1

# endregion


# region Pozitif sayı gir sıfır girilirse program biter. Program sayıların toplamını yazar. Negatif sayı girilirse program bişey yazmadan biter.
toplam = 0
while True:
    a = int(input(" Sayı giriniz: "))
    if a == 0:
        print(" Sıfır girdiğiniz için program bitirildi. ")
        break
    elif a < 0:
        print(" Negatif sayı girdiğiniz için program bitirldi.")
        break
    else:
        toplam += a
        print(f'Girilen sayı = {toplam}')
# endregion


# region Girilen n sayısına kadar sayıların karelerini yaz
x = int(input(" Sayı giriniz: "))
sayac = 1
if x == 0:
    print(" Sıfırın karesi sıfırdır. ")
elif x < 0:
    print(" Negatif sayı girdiniz. Lütfen pozitif sayı giriniz. ")
else:
    while sayac <= x:
        kare = sayac ** 2
        print(f' Sayısının karesi = {kare} ')
        sayac += 1
# endregion


# region Bir sporcu birinci gün x km koştu daha sonra her gün bir önceki güne göre %10 arttırdı. Hangi gün en az y km koşmuştur.
gun = int(input("Günü giriniz: "))
gun_toplam = 0
sayac = 1
while sayac <= gun:
    gun_toplam = gun + (gun * 0.90)
    gun_toplam += sayac
    print(f' Sonuç = {gun_toplam}')
    sayac += 1
# endregion


# region Girilen n sayısına göre n.ci Fibonacci sayısını bulan programı yaz
n = int(input(" Sayı giriniz: "))    # Çıktı doğru çalışmıyor
sayac = 1
n_toplam = 0
if n == 0:
    print(" Fibonacci sayısında sıfır kabul edilmez. ")
elif n < 0:
    print(" Sadece pozitif sayı giriniz.! ")
else:
    while sayac <= n:
        n_toplam = sayac + n
        print(f' Sonuç = {n_toplam}')
        sayac += 1
# endregion


# region Kullanıcı adı ve parola kontrolü şifre değiştirme
kullanici_adi = "kawasaki"
sifre = "zx10rr"
while True:
    a = input("Kullanıcı adı: ")
    b = input(" Şifre: ")
    if a == kullanici_adi and b == sifre:
        print(" Giriş başarılı. ")
        break
    elif a != kullanici_adi and b == sifre:
        print(" Kullanıcı adını yanlış girdiniz! ")
    elif a == kullanici_adi and b != sifre:
        print("Girdiğiniz şifre hatalı.\n Şifrenizi mi unuttunuz? ")
        print("Şifrenizi değiştirmek ister misiniz? (E/H)")
        cevap = input()
        if cevap == "E":
            yeni_sifre = input("Yeni Şifre: ")
            print("Lütfen bekleyin. ")
            sifre = yeni_sifre
            print("Şifre başarıyla değiştirildi. ")
    else:
        print("Kullanıcı adı veya şifre hatalı.\n Lütfen tekrar deneyin ")
# endregion


# region Girilen sayı asal mı değil mi
a = int(input(" Sayı giriniz: "))
if a <= 0:
    print("Asal sayı negatif ya da sıfır olamaz! ")
elif a == 1:
    print(" Asal sayı 1 olamaz! ")
else:
    if a > 1:  # daha iyi anlaşılsın neyi sorguladığımızı bilelim diye else kısmından sonra bir if bloğu daha açtım
        sayac = 2
        while sayac < a:
            if a % sayac == 0:
                print(f'{a} sayısı asal değildir. ')
                break
            sayac += 1
        else:
            print(f'{a} sayısı asaldır. ')
# endregion


# region Kullanıcıdan alınan sayının faktöriyeli
sayi = int(input(" Sayı giriniz: "))
sayac = 1
fak = 1
if sayi == 0:
    print(" Sıfırın faktöriyeli her zaman 1'e eşittir. ")
else:
    while sayac <= sayi:
        fak *= sayac
        print(f'{sayi} sayısının faktöriyellerii = {fak}')
        sayac += 1
# endregion


# region Kullanıcıdan işlem türü al (e, +, -, *, /). Alınan işlem türüne göre ilgili işlemi yap ve çıktısını ekrana yaz. Kullanıcı 'e' işlemini gönderene kadar sınırsız sayıda 4 işlem yap.(match- case ile de yapabilirsin
while True:
    islem_t = input(" İşlem türünü giriniz: ")
    sayi_1 = int(input(" Sayı giriniz: "))
    sayi_2 = int(input(" Sayı giriniz: "))
    if islem_t == 'e':
        print(" Döngüden çıkıldı.")
        break
    elif islem_t == '+':
        print(f'İşlem türü sonucu = {sayi_1 + sayi_2}')
    elif islem_t == '-':
        print(f' İşlem türü sonucu = {sayi_1 - sayi_2}')
    elif islem_t == '*':
        print(f' İşlem türü sonucu = {sayi_1 * sayi_2}')
    elif islem_t == '/':
        print(f' İşlem türü sonuvu = {sayi_1 / sayi_2}')
    else:
        print("Doğru işilem türünü giriniz! ")
# endregion


# region 1 ile 5 arasında sayı gir. 3 sayısı girildiğinde break kullanarak döngüden çık
sayi = int(input(" 1 - 5 arasında sayı giriniz: "))
sayac = 1
while sayac <= sayi:
    if sayi == 3:
        print(" 3 sayısı girildi ve döngüden çıkıldı. ")
        break
    else:
        print(f'{sayac} defa yazdırıldı. ')
    sayac += 1
# endregion


# region Kullanıcıdan 8 karakterlik bir şifre girmesini iste. Kullanıcı 8’den az ya da daha fazla karakter içeren bir şifre girdiğinde “Şifreniz 8 karakter olmalıdır.” şeklinde uyarı ver. Kullanıcı şartlara uygun bir şifre girdiğinde de “Şifreniz kaydedildi.” uyarısı ver
while True:
    sifre = input("8 karakterlik şifrenizi giriniz: ")
    if len(sifre) == 8:
        print(f'Şifreniz başarıyla kaydedildi. {sifre}')
        break
    else:
        print("Giriş hatalı...")
# endregion


# region Kullanıcıdan alınan 5 sayıyı sıralı şekilde ekrana yazdır
sayi = []
i = 0
while i < 5:
    deger = int(input("Girilen değer: "))
    sayi.append(deger)  # .append() metodu listelere eleman ekler sadece listenin sonuna 1 eleman ekler
    i += 1
sayi.sort()  # .sort() metodu sayıları küçükten büyüğe doğru sıralar
print(sayi)
# endregion


# region 1 -100 arasındaki sayıları azalan şekilde yaz
x = 100
while x > 0:
    print(f'{x}')
    x -= 1
# endregion


# region sayilar listesini while ile ekrana yazdır
sayilar = [1,3,5,7,9,12,19,21]
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1
# endregion


# region Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır
baslangic_degeri = int(input("Başlangıç değeri = "))
bitis_degeri = int(input("Bitiş değeri = "))
i = baslangic_degeri
while i < bitis_degeri:
    if i % 2 != 0:
        print(i)
    i += 1
# endregion


# region 1 - 100 arasındaki sayıları azalan şekilde yazın
i = 100
while i > 0:
    print(i)
    i -= 1
# endregion


# region Kullanıcıdan alınan 5 tane sayıyı ekrana sıralı şekilde yazın
sayilar_list = []
i = 0
while i < 5:
    sayi = int(input("Sayı giriniz: "))
    sayilar_list.append(sayi)
    i += 1
sayilar_list.sort()
print(sayilar_list)
# endregion


# region Kullanıcı sayı girsin. 0 girene kadar sayıların toplamını hesapla. 0 girince program sonlansın ve toplam ekrana yazsın
toplam = 0
while True:
    sayi = int(input("Sayı girişi yapınız: "))
    if sayi == 0:
        print(f'0 ı tuşladığınız için döngü durdurldu. {toplam}')
        break
    else:
        toplam += sayi
# endregion


# region Kullanıcıdan 1-10 arası sayı tahmin etmesini iste. bilgisayar sayı seçsin tahmine göre çıktı versin kullanıcı sayıyı bilene kadar döngü devam etsin
try:
    import random

    bilgisayar = random.randint(1, 10)
    while True:
        kullanici_tahmin = int(input("Sayı tahmin ediniz:"))
        if bilgisayar == kullanici_tahmin:
            print(f'Doğru bildiniz! {kullanici_tahmin}')
            break
        elif bilgisayar > kullanici_tahmin:
            print(f'Daha büyük sayı giriniz. {kullanici_tahmin}')
        else:
            print(f'Daha küçük sayı giriniz. {kullanici_tahmin}')
except ValueError as err:
    print("HATA! Lütfen sayı giriniz.")
finally:
    print("Tekrar oynamak ister misiniz? ")
# endregion


# region Girilen sayıya göre kaç defa yazdırılmak isteniyorsa çıktısını ver. 3 girilirse döngüyü bitir
while True:
    girilen_sayi = int(input("1 ile 5 arasında sayı girişi yapın:"))
    if girilen_sayi == 3:
        print("Döngüden çıkılıyor.")
        break
    else:
        print(f'{girilen_sayi} defa yazdırıldı')
# endregion



# For Loop Example

# region 0 - 100 arasındaki (100 dahil) çift ve tek sayıların toplamını yazdır
cift_toplam = 0
tek_toplam = 0
for i in range(0, 101, 1):
    if i % 2 == 0:
        cift_toplam += i
    else:
        tek_toplam += i
print(cift_toplam)
print(tek_toplam)
# endregion


# region Başlangıç bitiş ve artış miktarını kullanıcının belirlediği bir range() foksiyonundaki her bir sayıyının karesini ekrana yaz
baslangic = int(input("Sayı giriniz:"))
bitis = int(input("Sayı giriniz:"))
artis_miktari = int(input("Artış miktarı giriniz:"))
i = baslangic
for i in range(baslangic, bitis, artis_miktari):
    kare = i ** 2
    print(f'{kare}')
# endregion


# region faktöriyel hesaplaması
x = int(input("Sayı giriniz: "))
faktoriyel = 1
if x <= 0:
    print("Sayı sıfır veya negatif olamaz!")
elif x == 1:
    print("Sayı bir olamaz!")
else:
    for i in range(1, x+1):
        faktoriyel *= i
print(f'Faktöriyel = {faktoriyel}')
# endregion


# region çarpım tablosu yap    # iç içe geçmiş for loopu örneği çarklı (dişli sistemi) mantığı
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
# endregion


# region x sembollerini kullanarak içi dolu dörtgen yap
for i in range(4):  # satır
    for j in range(8):  # sütun
        print('x', end=" ")
    print(" ")
# endregion


# region x sembolü ile dik üçgen yap
for i in range(6):  # satır
    for j in range(6):  # sütun
        if j <= i:
            print('x', end=" ")
    print(" ")
# endregion


# region sayılar isimli bir liste içerisinde otomatik olarak random 10 tane sayı ile dolduralım
import random
sayilar = []
for i in range(10):
    sayilar.append(random.randint(1, 100))
print(sayilar)
# endregion


# region Kullancıdan bir söz öbeği alalım. Örneğin "merhaba ben bora". ilgili söz öbeğindeki sesli harfleri sesli harfler listesine. sessiz harfleri sessiz harfler listesine ekle. örneğin e harfi listeye eklendiyse bir daha eklemeyelim. kullanıcıdan alınan söz öbeğindeki tüm harfleri küçük harfe dönüştürün.rakamları eleyin.
soz_obegi = input("Söz öbeği giriniz:").lower()
sesli_harfler_listesi = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
sessiz_harfler = []
sesli_harfler = []
for harf in soz_obegi:
    if harf.isalpha():
        if harf not in sesli_harfler and harf not in sessiz_harfler:
            if harf in sesli_harfler_listesi:
                sesli_harfler.append(harf)
            else:
                sessiz_harfler.append(harf)
print(sesli_harfler)
print(sessiz_harfler)
# endregion


# region iki listeyi random sayılar ile dolduralım. akabinde benzer index'lerde tutulan değerleri toplayarak 3. listede gene aynı index'se yazalım
import random

liste1 = []
liste2 = []
liste3 = []
for i in range(10):
    liste1.insert(i, random.randint(0, 9))
    liste2.insert(i, random.randint(0, 9))
    liste3.insert(i, (liste1[i] + liste2[i]))
print(liste1)
print(liste2)
print(liste3)
# endregion


# region listedeki sayıların toplamını veren program yazalım
sayilar = [8,15,10,7,20]
toplam = 0
for i in sayilar:
    toplam += i
print(toplam)
# endregion


# region sayilar listesindeki hangi sayılar 3'ün katıdır
sayilar = [1,3,5,7,9,12,19,21]
for sayi in sayilar:
    if sayi % 3 == 0:
        print(sayi)
# endregion


# region sayilar listesinde sayilar toplamı kaçtır
sayilar = [1,3,5,7,9,12,19,21]
toplam = 0
for sayi in sayilar:
    toplam += sayi
print(toplam)
# endregion


# region sayilar listesindeki tek sayiların karesini al
sayilar = [1,3,5,7,9,12,19,21]
for sayi in sayilar:
    if sayi % 2 == 1:
        kare = sayi ** 2
        print(f'{kare}')
# endregion


# region şehirlerden hangileri en fazla 5 karakterlidir
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
for i in sehirler:
    if len(i) <= 5:
        print(i)
# endregion


# region programcının girdiği sayıya kadar olan sayıların toplamını yaz
x = int(input("Sayı giriniz"))
toplam = 0
for i in range(1, x+1):
    toplam += i
    print(toplam)
# endregion


# region Girilen ismi 10 kere ekrana yazdır
x = input("İsim giriniz:")
for i in range(10):
    print(x)
# endregion


# region dodgedeamon isminin harflerini alt alta yazdır
isim = 'dodgedeamon'
for harf in isim:
    print(harf)
# endregion


# region python ismini tersten yazdır
isim = 'Python'
for harf in reversed(isim):  # reversed() fonksiyonu listeyi ya da parametreyi tersine çevirir
    print(harf)
# endregion


# region sehirler listesini karakter sayılarıyla ekrana yazdır
sehirler = ["Edirne","Konya","Ankara","İstanbul","Tekridağ"]
for i in sehirler:
    print(f'{i} şehri {len(i)} karaktere sahiptir.')
# endregion


# region 6 kararkterli şehirleri yazdır
sehirler = ["Edirne","Konya","Ankara","İstanbul","Tekridağ"]
for i in sehirler:
    if len(i) == 6:
        print(i)
# endregion


# region sayılar listesindeki tek sayıları ekrana yazdır
sayilar = [12,43,11,56,43,12,8,6,43,21,23]
for i in sayilar:
    if i % 2 == 1:
        print(i)
# endregion


# region çift sayıların toplamını yazdır
sayilar = [12,43,11,56,43,12,8,6,43,21,23]
cift_toplam = 0
for i in sayilar:
    if i % 2 == 0:
        cift_toplam += i
print(cift_toplam)
# endregion


# region 1'den 100'e kadar tek sayıların toplamı (continue)
i = 0
toplam = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        continue
    toplam += i
print(toplam)
# endregion
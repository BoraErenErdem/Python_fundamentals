

# if - elif - else Example #


# region Büyük olanı bul ve ekrana yazdır
x = int(input(" Lütfen sayı giriniz: "))
y = int(input(" Lütfen sayı giriniz: "))

if x > y:
    print(" X sayısı büyüktür ")
elif y > x:
    print(" Y sayısı büyüktür ")
else:
    print(" X ve Y sayısı birbirine eşittir ")
# endregion


# region Kullanıcıdan alınan sayı çift mi tek mi
x = int(input(" Lütfen sayı giriniz: "))

if x % 2 == 0:
    print(f' Çifttir {x}')
else:
    print(" Tektir ", x )
# endregion


# region Sayı pozitif mi negatif mi nötr mü
x = int(input(" Lütfen sayı giriniz: "))

if x > 0:
    print(" Sayı pozitiftir ", x)
elif x == 0:
    print(" Sayı nötrdür ", x)
else:
    print(" Sayı negatiftir ", x)
# endregion


# region Mevsim bilgisi al gelen bilgiye göre ayları yazdır ( hem if - else hem de match - case )
# if - else
x = input(" Mevsim bilgisi giriniz: ")

if x == "Kış":
    print(" Aralık \n Ocak \n Şubat")
elif x == "İlkbahar":
    print(" Mart \n Nisa \n Mayıs")
elif x == "Yaz":
    print(" Haziran \n Temmuz \n Ağustos")
elif x == "Sonbahar":
    print(" Eylül \n Ekim \n Kasım")
else:
    print("Lütfen doğru mevsimi girdiğinizden emin olunuz..!")


# match - case
x = input(" Mevsim bilgisi giriniz: ")

match x:
    case "Kış":
        print(" Aralık \n Ocak \n Şubat")
    case "İlkbahar":
        print(" Mart \n Nisan \n Mayıs")
    case "Yaz":
        print(" Haziran \n Temmuz \n Ağustos")
    case "Sonbahar":
        print(" Eylül \n Ekim \n Kasım")
    case _:
        print(" Böyle bir mevsim yok..!")
# endregion


# region Araç türüne göre ceza var ya da yok. araba = 55 motor = 60 kamyon = 35
x = input(" Araç türünü giriniz: ")
y = int(input(" Hız giriniz: "))

if x == "araba":
    if y <= 55:
        print(f' Cezalı değilsiniz {y}')
    else:
        print(f' Cezalısınız.! {y}')
elif x == "motor":
    if y <= 60:
        print(" Cezalı değilsiniz", y)
    else:
        print(" Cezalısınız.!", y)
elif x == "kamyon":
    if y <= 35:
        print(f' Cezalı değilsiniz {y}')
    else:
        print(" Cezalısınız.!", y)
else:
    print(" Lütfen geçerli parametreleri giriniz..!")
# endregion


# region Kullanıcıdan alınan 3 tane sayıdan büyük olanı yaz
x = int(input(" Sayı giriniz: "))
y = int(input(" Sayı giriniz: "))
z = int(input(" Sayı giriniz: "))

if x > y and x > z:
    print(f' X sayısı en büyüktür {x}')
elif y > x and y > z:
    print(f' Y sayısı en büyüktür {y}')
elif z > x and z > y:
    print(f' Z sayısı en büyüktür {z}')
else:
    print(" Uygun parametreler giriniz")
# endregion


# region Aranılan ürün bilgisini al ve ürünün reyonuna yönlendir. sebze = domates - biber - patlıcan teknoloji = telefon - tablet - mouse kozmetik = wax - krem - parfüm
x = input(" Ürünü giriniz: ")

if x == 'domates' or x == 'biber' or x == 'patlıcan':
    print(" Sebze reyonuna gidiniz ")
elif x == 'telefon' or x == 'tablet' or x == 'mouse':
    print(" Teknoloji reyonuna gidiniz ")
elif x == 'wax' or x == 'krem' or x == 'parfüm':
    print(" Kozmetik reyonuna gidiniz ")
else:
    print(" Doğru ürünü giriniz...")
# endregion


# region Kullanıcıdan satın aldığı kitap sayısını alalım. Bir kitap 5 tl. 1 - 20 arasında kitap alırsa % 5 indirim. 21 - 50 arasıdna % 10. 51 - 75 arasında % 15. 76 - 100 arasında % 20
x = int(input(" Kitap sayısı giriniz: "))

if 1 <= x <= 20:
    t = x * 5 * 0.95
    print(f' Ödeyeceğiniz tutar: {t}')
elif 21 <= x <= 50:
    t = x * 5 * 0.90
    print(f' Ödeyeceğiniz tutar: {t}')
elif 51 <= x <= 75:
    t = x * 5 * 0.85
    print(f' Ödeyeceğiniz tutar: {t}')
elif 76 <= x <= 100:
    t = x * 5* 0.80
    print(f' Ödeyeceğiniz tutar: {t}')
else:
    print(" Geçerli parametreleri giriniz.")
# endregion


# region Lineer bir doğrunun katsayılarını bulun formül = b ** - 4 * a * c  delta sıfırdan büyükse 2 kök var. delta sıfırsa kök 1. delta sıfırdan küçükse reel kök yok
a = int(input('(a) katsayısını giriniz: '))
b = int(input('(b) katsayısını giriniz: '))
c = int(input('(c) katsayısını giriniz: '))

delta = b ** - 4 * a * c

if delta > 0:
    x1 = -b - sqrt(delta) / 2 * a
    x2 = - b + sqrt(delta) / 2 * a
    print(f' 2 gerçek kökü var.\nİlk gerçek kök: {x1}\nİkinci gerçek kök: {x2}')
elif delta == 0:
    x1 = -b - sqrt(delta) / 2 * a
    print(f' Gerçek bir tane reel kökü var\nİlk gerçek kök: {x1}')
else:
    print(' Gerçek kök yok ')
# endregion


# region Kullanıcıdan username, password, kilo, boy bilgilerini giriniz. login olacak (beast, 123)
x = input(" Username: ")
y = input(" Password: ")

if x == 'beast' and y == '123':
    print(" Login ")
    a = float(input(" Kilonuzu giriniz: "))
    b = float(input(" Boyunuzu giriniz: "))
    vki = a / (b ** 2)

    if 0 <= vki <= 18.5:
        print(" Zayıf", vki)
    elif 18.6 <= vki <= 24.9:
        print(" Normal", vki)
    elif 25 <= vki <= 29.9:
        print(f' Kilolu {vki}')
    elif vki <= 30:
        print(f' Obez {vki}')
    else:
        print(" Doğru değerleri giriniz.!")
# endregion


# region Kullanıcı bir ayı temsil eden sayı girsin karşılık gelen ayı yazdır
x = int(input(" Lütfen bir sayı giriniz: "))

if 1 <= x <= 12:
    if x == 1:
        print(" Ocak ")
    elif x == 2:
        print(" Şubat ")
    elif x == 3:
        print(" Mart ")
    elif x == 4:
        print(" Nisan")
    elif x == 5:
        print(" Mayıs ")
    elif x == 6:
        print(" Haziran ")
    elif x == 7:
        print(" Temmuz ")
    elif x == 8:
        print(" Ağustos ")
    elif x == 9:
        print(" Eylül ")
    elif x == 10:
        print(" Ekim ")
    elif x == 11:
        print(" Kasım")
    elif x == 12:
        print(" Aralık ")
else:
    print(" Geçersiz sayı. Lütfen 1 -12 arasında sayı giriniz. ")
# endregion


# region Girilen sayıya göre pozitif mi negatif mi sıfır mı bul
x = float(input(" Sayı giriniz: "))

if x > 0:
    print(f'Sayı pozitiftir. {x}')
elif x == 0:
    print(f'Sayı negatiftir. {x}')
elif x < 0:
    print(f'Sayı negatiftir. {x}')
else:
    print(f'Geçerli değer girdiğinizden emin olun.! {x}')
# endregion


# region Kullanıcıdan alınan sayının sorgulanması. çift ve 10 a bölünürse. çift ve 10 a bölünmezse. tek ve 5 e bölünürse. tek ve 5 e bölünmezse şartlarını bul
x = int(input(" Sayı giriniz: "))
if x % 2 == 0 and x % 10 == 0:        # not operatörü mantıksal ifadeyi tersine çevirmek için kullanılır. olan durumu tersine çevirir. true ise false yapar gibi.
    print(" Sayı hem çift hem 10 a bölünebilir. ")
elif x % 2 == 0 and not x % 10 == 0:
    print(" Sayı çift ama 10 a bölünemez. ")
elif x % 1 == 0 and x % 5 == 0:
    print(" Sayı tek ve 5 e bölünebilir. ")
elif x % 1 == 0 and not x % 5 == 0:
    print(" Sayı tek ama 5 e bölünemez. ")
else:
    print(" Geçerli parametreleri giriniz.!")
# endregion


# region Girilen sayıya göre çocuk mu yetişkin mi yaşlı mı olduğunu yaz. çocuk 0-  18 yetişkin 19 - 65 yaşlı 65 ve üstü
x = int(input(" Yaşınızı giriniz: "))

if 0 <= x <= 18:
    print(f' Çocuk: {x}')
elif 19 <= x <= 65:
    print(f' Yetişkin: {x}')
elif 66 <= x:
    print(f' Yaşlı: {x}')
else:
    print(" Lütfen geçerli bir sayı giriniz.!")
# endregion


# region Girilen harfin sesli mi sessiz mi olduğunu bul
x = input(" Harf giriniz: ")
sesli_harf = 'aeıioöuü'
sessiz_harf = 'zyvtşsrpnrmlkhjğgdçcbqwx'

if x in sesli_harf:
    print(" Sesli harf girdiniz: ", x)
elif x in sessiz_harf:
    print(" Sessiz harf girdiniz: ", x)
else:
    print(" Lütfen geçerli harf giriniz !", x)
# endregion


# region Girilen iki sayıda pozitifse toplamını yaz. iki sayıda negatifse farkını yaz. diğer durumlarda çarpımın yaz
x = float(input(" Sayı giriniz: "))
y = float(input(" Sayı giriniz: "))

if x > 0 and y > 0:
    toplam = x + y
    print(f' Sayıların toplamı = {toplam}')
elif x < 0 and y < 0:
    fark = x - y
    print(f' Sayıların farkı = {fark}')
else:
    carpim = x * y
    print(f' Sayıların çarpımı = {carpim}')
# endregion


# region Not girildiğinde kaç aldığını ekrana yaz. 90 ve üzeri AA. 80-89 BB. 70-79 CC. 60-69 DD. 60 ve altı FF
x = int(input(" Notunuzu giriniz: "))

if 90 <= x <= 100:
    print(" Notunuz: AA ")
elif 80 <= x <= 89:
    print(" Notunuz: BB ")
elif 70 <= x <= 79:
    print(" Notunuz: CC ")
elif 60 <= x <= 69:
    print(" Notunuz: DD ")
elif x <= 59:
    print(" Notunuz: FF - Sınavdan kaldınız.")
else:
    print(" Lütfen geçerli not sonucunuzu giriniz !")
# endregion


# region Girilen kelime python ise yazdır. java ise yazdır. c++ ise yazdır
x = input(" Kelime giriniz: ")

if x == 'python':
    print(f' Python dilini seçtiniz. ')
elif x == 'java':
    print(f' Java dilini seçtiniz. ')
elif x == 'c++':
    print(f' C++ dilini seçtiniz. ')
else:
    print(f' Geçersiz dil seçtiniz!')
# endregion


# region Girilen iki sayı ve operatöre göre ekrana yaz
x = float(input(" Lütfen sayı giriniz: "))
y = float(input(" Lütfen sayı giriniz: "))
operator = input(" Operatör giriniz ( +, -, *, / ): ")

if operator == "+":
    print(f' Sayıların toplamı: {x + y}')
elif operator == "-":
    print(f' Sayıların farkı: {x - y}')
elif operator == "*":
    print(f' Sayıların çarpımı: {x * y}')
elif operator == "/":
    print(f' Sayıların bölümü: {x / y}')
else:
    print(" Geçerli parametreleri giriniz.!")
# endregion


# region Kullanıcının bilgilerini kontrol et. kullanıcı adı = ktm1390 şifre = beast123
kullanici = input(" Kullanıcı adını giriniz: ")
sifre = input(" Şifrenizi giriniz: ")

if kullanici == "ktm1390" and sifre == "beast123":
    print(" Giriş başarılı: ", kullanici, sifre)
else:
    print(" Giriş bilgilerinizi kontrol ediniz.!", kullanici, sifre)
# endregion


# region Girilen 2 veri eşitse true değilse false
x = input(" Veri giriniz: ")
y = input(" Veri giriniz: ")

if x == y:
    print(" True ")
else:
    print(" False ")
# endregion


# region Kullanıcıdan 3 değer al birinci değer iki ve üçüncü değerin arasındaysa true değilse false yaz
x = float(input(" Lütfen değer giriniz: "))
y = float(input(" Lütfen değer giriniz: "))
z = float(input(" Lütfen değer giriniz: "))

if x < y and x > z:
    print(" True ")
elif x > y and x < z:
    print(" True ")
else:
    print(" False ")
# endregion


# region Kullanıcıdan 2 tam sayı al bunların herhangi birisi 10 ya da ikisini toplamı 10 ise true değilse false yaz
x = int(input(" Sayı giriniz: "))
y = int(input(" Sayı giriniz: "))

if x == 10 or y == 10:
    print(" True ")
elif x + y == 10:
    print(" True ")
else:
    print(" False ")
# endregion


# region Kullanıcıdan bir ay adı girsin girilen ayın kaç gün sürece devam ettiğini yaz
x = input(" Lütfen ay giriniz: ")

if x == "Ocak":
    print(" Ocak ayı 31 gün sürer ")
elif x == "Şubat":
    print(" Şubat ayı 29 gün sürer ")
elif x == "Mart":
    print(" Mart ayı 31 gün sürer ")
elif x == "Nisan":
    print(" Nisan ayı 30 gün sürer ")
elif x == "Mayıs":
    print(" Mayıs ayı 31 gün sürer ")
elif x == "Haziran":
    print(" Haziran ayı 30 gün sürer ")
elif x == "Temmuz":
    print(" Temmuz ayı 31 gün sürer ")
elif x == "Ağustos":
    print(" Ağustos ayı 31 gün sürer ")
elif x == "Eylül":
    print(" Eylül ayı 30 gün sürer ")
elif x == "Ekim":
    print(" Ekim ayı 31 gün sürer ")
elif x == "Kasım":
    print(" Kasım ayı 30 gün sürer ")
elif x == "Aralık":
    print(" Aralık ayı 31 gün sürer ")
else:
    print(" Lütfen geçerli komut giriniz.! ")
# endregion


# region Kullanıcıdan isim yaş eğitim bilgilerini iste. duruma göre ehliyet alma durumunu kontrol et. 18 yaş ve en az lise ya da üni mezunu
Adiniz = (input("Adınızı giriniz: "))
Yasiniz = int(input("Yaşınızı giriniz: "))
Egitim_bilgisi = input("Eğitim durumunuzu giriniz: ")

if Yasiniz >= 18 and Egitim_bilgisi == 'lise' or Egitim_bilgisi == 'üniversite':
    print("Ehliyet alabilirsiniz. ")
else:
    print("Ehliyet alamazsınız.!")
# endregion
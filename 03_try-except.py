

# try - except Example


# region try - except basic
try:
    x = int(input(" Tamsayı giriniz: "))
    sonuc = x / 0
    print(" sonuc ")
except:
    print(" Tamsayı sıfıra bölünmez! ")
finally:
    print(" Ne olursa olsun çalışırım. ")
# endregion


# region try - except ZeroDivisionError
try:
    x = int(input(" Tamsayı giriniz: "))
    sonuc = x / 0
    print(" sonuc ")
except ZeroDivisionError as err:
    print(" Tamsayı sıfıra bölünmez! ")
finally:
    print(" Doğru işlemleri gerçekleştiriniz.")
# endregion


# region try - except ValueError ( Red )
try:
    x = int(input(" Tamsayı giriniz: "))
    sonuc = x / 0
    print(f' Sonuc {x}')
except ValueError as err:
    print(f' Sonuc {err}')
# endregion


# region try - except - else
try:
    x = int(input(" Age: "))
    print(f' Age = {x}')
except ValueError as err:
    print(f' Age = {err}')
else:
    print(" Except çalışmazsa çalışırım. ")
# endregion


# region try - except - else - finally
try:
    x = int(input(" Age: "))
    print(f' Age = {x}')
except ValueError as err:
    print(f' Age = {err}')
else:
    print(" Beklenmeyen bir hata oluştu.")
finally:
    print(" Lütfen tekrar deneyiniz. ")
# endregion


# region Girilen 2 adet sayı bölünürse başarılı bölünmezse hata yaz
try:
    x = float(input(" Sayı giriniz: "))
    y = float(input(" Sayı giriniz: "))
    bolme = x / y
    print(f' Bölüm başarılı = {bolme}')
except ZeroDivisionError as err:
    print(f' Sayı sıfıra bölünmez. {err}')
except ValueError as err:
    print(f' Geçersiz sayı girişi. {err}')
except Exception as err:
    print(f' Hata. {err}')
# endregion


# region Girilen sayının karesi al. Girilen sayı negatifse uyarı ver. Uyarı almaksızın yazdır
try:
    x = float(input(" Sayı giriniz: "))
    if x ** 2 >= 0:
        kare = x ** 2
        print(f' Sonuç pozitif. {kare}')
    else:
        print(f' Sonuç negatif. Yeniden sayı giriniz! ')
except ValueError as err:
    print(f' Geçerli sayı giriniz. {err}')
except Exception as err:
    print(f' Hata! {err}')
# endregion


# region Girilen 2 tam sayıyı bölmeye çalış ve bölmeyi denetle. başarılıysa sonucu yazdır değilse hata ver. finally bloğuna mesaj yazdır
try:
    x = int(input(" Tam sayı giriniz: "))
    y = int(input(" Tam sayı giriniz: "))
    bolme = x / y
    print(f' Bölme işlemi başarılı: {bolme}')
except ZeroDivisionError as err:
    print(f' Tam sayı sıfıra bölünmez! {err}')
except ValueError as err:
    print(f' Tam sayı giriniz!')
except Exception as err:
    print(f' Hata! {err}')
finally:
    print(" Bu uygulamayı başka sayılarla tekrar deneyiniz...")
# endregion


# region Girilen sayı sıfır mı pozitif mi negatif mi yazdır. metin girilirse de yaz
try:
    x = float(input(" Lütfen sayı giriniz: "))
    if x == 0:
        print(" Sayı sıfırdır. ")
    elif x > 0:
        print(f' Sayı pozitiftir. {x}')
    else:
        print(f' Sayı negatiftir. {x}')
except ValueError as err:
    print(f' {err}')
except Exception as err:
    print(f' {err}')
finally:
    print(" İşlem kapanıyor..")
# endregion


# region Girilen sayının karesini yaz. başka durumlar için hata yaz
try:
    x = float(input(" Sayı giriniz: "))
    islem = x ** 2
    print(f' Girilen sayının karesi = {islem}')
except ValueError as err:
    print(" Sayı giriniz!!!")
except Exception as err:
    print("HATA!", err)
finally:
    print(" Program sonlandırılıyor.. ")
# endregion


# region Sayı girilirse 2 ile çarp. Sayı girmezse ona göre yazdır. Negatif ya da sıfır girerse ona göre yazdır
try:
    x = float(input(" Sayı giriniz: "))
    carpim = x * 2
    if x > 0:
        print(f' Sonuc = {carpim}')
    elif x < 0:
        print(f' Negatif sayı girişi yapamazsınız! ')
    else:
        print(f' Sıfır sayısını giremezsiniz! ')
except ValueError as err:
    print(" Pozitif sayı giriniz!!!")
except Exception as err:
    print(f' HATA {err}')
finally:
    print(" İşlem sonlandırılıyor..")
# endregion


# region Girilen sayıların aritmetik ortalamasını al doğru ve yanlışsa çıktı ver
try:
    x = float(input(" Sayı giriniz: "))
    y = float(input(" Sayı giriniz: "))
    a_o = (x + y) / 2
    print(f' Aritmetik ortalama = {a_o}')
except ValueError as err:
    print(" Sayısal değer girmediniz! ", err)
except ArithmeticError as err:
    print(" Aritmetik ortalama hesaplanamadı!", err)
except Exception as err:
    print(f'{err}')
else:
    print(" - Başarılı - ")
finally:
    print(" Sistem yeniden yapılandırılıyor..")
# endregion


# region Girilen sayıysa sayının karesini al. sayı 10 dan büyükse karesinin yarısını yaz. 5-9 arasındaysa karesinin iki katını yaz. 1-4 arasındaysa karesinin üç katını yaz. sıfır hariç.
try:
    x = float(input(" Sayı giriniz: "))
    if x == float:
        kare1 = x ** 2
        print(f' Sonuç = {kare1}')
    elif x >= 10:
        kare2 = (x ** 2) / 2
        print(f' Sonuç = {kare2}')
    elif 5 <= x <= 9:
        kare3 = (x ** 2) * 2
        print(f' Sonuç = {kare3}')
    elif 1 <= x <= 4:
        kare4 = (x ** 2) * 3
        print(f' Sonuç = {kare4}')
    elif x == 0:
        print(" Sonuç sıfıra eşit olamaz! ")
    else:
        print(" Negatif sayı girilemez. Pozitif sayı giriniz..!")
except ValueError as err:
    print(" Geçersiz giriş! Lütfen bir sayı giriniz. ")
finally:
    print(" Sistem yeniden yapılandırılıyor...")
# endregion


# region Girilen iki sayıyı birbirine böl. duruma göre hataları ver.sıfırı böleme
try:
    x = float(input(" Sayı giriniz: "))
    y = float(input(" Sayı giriniz: "))
    bolme = x / y
    print(f' Sonuç = {bolme}')
except ZeroDivisionError:
    print(" Sayılar sıfıra bölünemez! ")
except ValueError:
    print(" Geçersiz giriş. Sayı giriniz! ")
except Exception:
    print(" Beklenmedik bir hata oluştu!!! ")
finally:
    print(" Veriler sunucuyla paylaşılıyor..")
# endregion


# region Girilen kelimenin uzunluğu 5-10 arasında ise uzun. 4 ise ve daha küçükse kısa. 11 den büyükse çok uzun. hata durumunu da yaz
try:
    x = input(" Kelime giriniz: ")

    rakamlar_listesi = "0123456789"

    if x in rakamlar_listesi:
        print("Sayı değeri giremezsiniz..! ")

    x_uzunluk = len(x)

    if 5 <= x_uzunluk <= 10:
        print(" Uzun kelime seçtiniz. ")
    elif x_uzunluk <= 4:
        print(" Kısa kelime seçtiniz. ")
    else:
        print(" Çok uzun kelime seçtiniz. ")
except Exception as err:
    print(f' Beklenmedik hata oluştu... {err}!')
finally:
    print(" Bilgileriniz kaydedildi. ")


try:
    x = input(" Kelime giriniz: ")

    rakamlar_listesi = "0123456789"

    if x in rakamlar_listesi:
        print("Sayı değeri giremezsiniz..! ")

    for i in x:
        if i.isnumeric():
            raise Exception("hata")


    x_uzunluk = len(x)

    if 5 <= x_uzunluk <= 10:
        print(" Uzun kelime seçtiniz. ")
    elif x_uzunluk <= 4:
        print(" Kısa kelime seçtiniz. ")
    else:
        print(" Çok uzun kelime seçtiniz. ")
except Exception as err:
    print(f' Beklenmedik hata oluştu... {err}!')
finally:
    print(" Bilgileriniz kaydedildi. ")
# endregion


# region Boolean ile oyun karakterinin yaşayıp yaşamadığına bak
karakterCanli = True
if karakterCanli:
    print(" Oyun karakteriniz yaşıyor.")
else:
    print("Oyun karakteriniz yaşamıyor.")
# endregion


# region in ile stringin içinde aranılan ifade var mı yok mu bak
girilen_kararkter = "BoraErdem"
if "Bora" in girilen_kararkter:
    print("Karakter var. ")
else:
    print("Karakter yok. ")
# endregion


# region Kullanıcıdan harf girişi alalım harfin 'aeiou' arasında olup olmadığını kontrol et ona göre yazdır
harf = input("Harf giriniz: ")
sesli_harf = "aeiou"
if harf in sesli_harf:
    print(f'Sesli harf girişi yaptınız: {harf}')
else:
    print(f'Sessiz harf girişi yaptınız: {harf}')
# endregion


# region Kullanıcın girdiği kelimede in geçiyor mu kontrol et ona göre yaz
kelime = input("Kelime girişi yapınız: ")
bakilacak_kelime = "in"
if "in" in kelime:  # if bakilacak_kelime in kelime: diye de yazabilirdik
    print(f'Kelimenin içinde in ifadesi yer almaktadır.')
else:
    print(f'Kelimenin içinde in ifadesi yer almamaktadır..!')
# endregion
f = open(dosya_adı, kip)
# “tahsilat.txt” adlı bir dosyayı yazma kipinde açmak için şöyle bir komut kullanıyoruz:
tahsilat_dosyası = open("tahsilat_dosyası.txt", "w")
# Bulunduğun dizin değilde farklı bir dizindeki dosyaya yazmak yada okumak istiyorsan
dosya = open("/dosyayı/oluşturmak/istediğimiz/dizin/dosya_adı", "w")
# Burda kaçma dizisi hatası alacaksın. Çözümler şunlar
open(r"C:\aylar\nisan\toplam masraf\masraf.txt", "w")
open("C:\\aylar\\nisan\\toplam masraf\\masraf.txt", "w")

Dosyaya Yazmak
dosya.write(yazılacak_şeyler)
# Örnek verecek olursak
ths = open("tahsilat_dosyası.txt", "w")
ths.write("Halil Pazarlama: 120.000 TL")
ths.close()

Dosya Okumak
fihrist = open("fihrist.txt", "r")

# Öncelikle içeriği şu olan, fihrist.txt adlı bir dosyamızın olduğunu varsayalım:
#Ahmet Özbudak : 0533 123 23 34
#Mehmet Sülün  : 0532 212 22 22
#Sami Sam      : 0542 333 34 34

fihrist = open("fihrist.txt")
print(fihrist.read())
fihrist.close()
# çıktı yine 3 satır birden olacak.

#Ama şu kodla okursak sadece tek satır alacak
fihrist = open("fihrist.txt")
print(fihrist.readline())
fihrist.close()

#Bu kodla okursak hepsini liste şeklinde alıyor
fihrist = open("fihrist.txt")
print(fihrist.readlines())
fihrist.close()
#output => ['Ahmet Özbudak : 0533 123 23 34\n', 'Mehmet Sülün : 0532 212 22 22\n', 'Sami Sam : 0542 333 34 34']

# YANİ read VE readline OUTPUT OLARAK STRING VERİRKEN readlines LİSTE VERİR.

# Şimdi gelelim her seferinde close komutunu kullanmama yöntemine.
with open("dosyaadı", "r") as dosya:
    print(dosya.read())

Dosyayı İleri-Geri Sarmak
# Dosyayı okuduktan sonra imleç en sonda kalır. İmleci başa almak için seek fonksiyonunu kullanabiliriz.
f.seek(0)
# imleci 0. bayta yani en başa alır. istediğin baytı yazıp gidebilirsin seek(10) 10. bayta gider.
# kaçıncı baytta olduğunu öğrenmek içinde tell fonksiyonunu kullanabilirsin.
f.tell() #outputs => 0   Yani imleç en baştaymış.

Dosyalarda Değişiklik Yapmak
- Dosyaların Sonunda Değişiklik Yapmak
with open("fihrist.txt", "a") as f:
    f.write("Selin Özden\t: 0212 222 22 22")
# önceki örnekte ki isimlerin alt satırına bide selini ekledik
#Burada şu noktaya dikkat etmeniz lazım. Dosyanın sonunda bir satır başı karakterinin (\n) bulunup bulunmamasına bağlı olarak, dosyaya eklediğiniz yeni satırlar 
#düzgün bir şekilde bir alt satıra geçebileceği gibi, dosyanın son satırının yanına da eklenebilir. Dolayısıyla duruma göre yukarıdaki satırı şu şekilde yazmanız gerekebilir:
with open("fihrist.txt", "a") as f:
    f.write("\nSelin Özden\t: 0212 222 22 22")

Dosyaların Başında Değişiklik Yapmak
with open("fihrist.txt", "r+") as f:
    veri = f.read()
    f.seek(0) #Dosyayı başa sarıyoruz
    f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
# Seek ile en başına gidip sedatı öyle yazdık.
# Peki şöyle yapsak ne olurdu?

with open("fihrist.txt", "r+") as f:
    f.seek(0)
    f.write("Sedat Köz\t: 0322 234 45 45\n")
# burada en başa gidiyoruz ama sedatı en başta bulunan ahmetin üzerine yazar. yani veriler kaybolur. O yüzden önce okuyup sonra yazacağımızı yazmamız gerek.























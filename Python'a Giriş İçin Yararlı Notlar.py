#Python'a yeni başlayanlar için kısa öz bilgiler

# Bu komut ile istediğiniz modülü yükleyebilirsiniz. Örneğin projede requests modülü kullanacaksınız. 'pip install requests' yazmanız yeterli
pip install [paketadı]

# Bir paketin bilgisayarımıza yüklenip yüklenmediğini kontrol etmek için bu komutu yazabiliriz.
[paketadı] --version
# örneğin virtualenv --version

# Üstteki şekilde pip yüklediğimiz paketin en güncel sürümünü yükleyecektir. Eğer spesifik bir sürüm yüklemek istersek:
pip install [paketadı]==[sürümNo]
# Örnek verecek olursak
pip install django==1.0.0

# Bir paketi güncellemek içinse bu komut yeterlidir
pip install django --upgrade

#Olurda lazım olursa diye paket kaldırmayı da buraya bırakayım
pip uninstall django

# pip güncel olmadığı zaman kendi uyarıp şu kodu çalıştırarak beni güncelleyebilirsin der ama kıyıda köşede dursun. Pip güncelleme kodu
pip install --upgrade pip

# Virtualenv kullanımı
# Bilgisayarımıza yüklüyoruz
pip install virtualenv

# Şimdi aşağıdaki komutla virt env oluşturuyoruz.
virtualenv ornekProje

# benim oluşturduğum virtualenv şu dizinde:
# C:\Users\honur\Desktop\ornekProje\
# şimdi aktif etmek için virtualenv içindeki scripts klasöründeki activate.bat dosyasını şu komutla çalıştırıyoruz.
# Bulunduğumuz dizini kendi bilgisayarınıza göre ayarlamayı unutmayın.
C:\Users\honur\Desktop\ornekProje\Scripts\activate.bat
# eğer çalıştıysa komut penceresinin başında parantez içinde virtualenv projesinin adını görürsünüz.

# virtualenv tekrar kapatmak içinse bu kod yeterli
C:\Users\honur\Desktop\ornekProje\Scripts\deactivate.bat
# Eğer kapandıysa parantez içindeki proje adı gidecektir.
# Not : Kapatmak için virtualenv açıkken basitçe deactivate yazmanız da yeterlidir.


# şimdi virtualenv'e rasgele bir modül kuralım. pip install numpy yeterli. aşağıdaki komut ile requirements.txt oluşturabiliyoruz.
pip freeze > requirements.txt
# Not: bu komut çalışması için virtualenv active olması gerekiyor.

#Bir kullanıcı bu requirements dosyasının içindeki paketleri yükleyip programınızı çalıştırabilmesi için tek yapması gereken şu.
pip install -r requirements.txt

# Bir repoyu bilgisayara indirmek için 
git clone "file_adress"
# örnek: git clone https://github.com/drdoof2019/Faydali-Kodlar-Python

# add komutu ile commit edeceğimiz dosyaları seçiyoruz.
git add dosyaadi.py
# burada iki aşama kullanılmasının sebebi örneğin 10 dosyalı bir projede çalışıyoruz ancak sadece 2 dosyasını
# github'a göndermek istiyoruz. öyleyse o 2'sini ekliyoruz gerisini göndermemiş oluyoruz.

#commit komutu ile add ettiğimiz dosyaları github'a göndermeden önce lokaldeki git te kaydediyoruz.
git commit -m "mesajınız"
# mesaj ile gönderme bir tür log kaydı olarak düşünülebilir. ilerde hangi aşamada ne yaptığını takip etmek için.

# şimdi lokaldeki clone'umuz ile githubdaki dosya arasındaki farkları görelim. Örneğin gereksiz.html dosyası
# içeren bir repoyu clone'layıp içine hello.html açtık ve 11 satır kod yazdık diyelim. öyleyse aşağıdaki komut çalışınca 
git status
# bize aradaki farkları yani 1 dosya ve 11 satır kodu belirtecek.

# son adımda githuba lokaldeki dosyalarımızı göndermek için
git push
# komutunu kullanıyoruz ve yaptığımız değişiklikler githuba gitmiş oluyor.

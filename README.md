Rasperry Pi Kullanarak Parmak İzi Kontrollü Güvenlik Kontrolü (PAROLİZ)

Giriş
Bu proje parmak izi ve parola kontrolü ile ile güvenlik sistemidir. Raspberry pi ve parmak izi sensörü kullanarak 
kişilerin kendine has olan parmak izi ve kişilerin kendi belirlediği 4 haneli parolaları sorgulayıp -eşleştirip- 
doğruluğunda veya yalnışlığında gerekli işlemleri kendi içerisinde yapan bir güvenlik sistemidir.
Sistemimizde parmak izi sensörü ve klavye giriş olup, çıkışını LCD ekran üzerinden vermektedir. 
Normal durumda iken öncelikle parolayı sorgulayan sistem doğru parola ve parmak izi olması durumunda erişim sağlar. 
Kendi içinde yönetici ara yüzü olup kişi ekleme silme işlemleri de çok rahat bir şekilde yapılabilir.
Bu sistemin her yere entegre edilebilirliğinden kullanım alanı çok geniş ve kullanımı çok kolaydır.

Gerekli Donanım Bileşenleri
1. 1 adet Raspberry pi
2. 1 adet ZFM60 Parmak İzi Okuyucu Sensör
3. 1 adet PL2303 USB-TTL Seri Dönüştürücü Kartı
4. 1 adet 2x16 LCD Ekran


Gerekli Yazılım Bileşenleri

1. Raspbian Jessie OS (www.raspbian.org)


Kullanılan Bileşenlerin Özellikleri

1. Raspberry pi ; Raspbery yaklaşık el boyutunda ki bir mini bilgisayardır.Biz projemizde parmak izi sensörü ve
LCD ekranı senkron bir şekilde kullanmak için Raspberry Pi 3 ü kullandık


2.ZFM60 Parmak İzi Okuyucu Sensör ; Parmak izi sensörü parmağın fotoğrafını çekip kendi içinde kaydedebilen, 
kaydedilenler arasında arama yapıp kayıtlı olup olmama durumunu sorgulayan ve kayıtlı parmak izini silebilen bir sensördür.
Bu sensörü direnç.net edinebilirsiniz. (https://www.direnc.net/parmak-izi-okuyucu)


3.PL2303 USB-TTL Seri Dönüştürücü Kartı ; USB seri dönüştürücü kartı parmak izi sensörünü rasbperry üzerinde kullanmamız için gereken 
ara eleman. Bu dönüştürücü kartını direnç.net den edinebilirisiniz. (https://www.direnc.net/pl2303-usb-uart-board-usb-a)

4.2x16 LCD Ekran ; LCD ekran görsel bir çıkış için kullanılmaktadır. LCD ekranı direnç.net den edinebilirisiniz. 
(https://www.direnc.net/2x16-lcd-display-sol-ust-mavi-qapass) 


Yapım aşamaları
Adım 1: İlk olarak Raspberry Pi’deki Raspbian OS’yi güncellemek ve yükseltmek için aşağıdaki komutları
çalıştırın:

~$ sudo apt-get update
~$ sudo apt-get upgrade


Adım 2 : Parmak izi sensörü için gerekenler

Adım 2-1 : Yazılım kurulumu

Adım 2-1-1 : Öncelikle (henüz yapılmadıysa) PM Codeworks deposunu sisteminize eklemeniz gerekir:
~$ echo "deb http://apt.pm-codeworks.de wheezy main" | sudo tee -a /etc/apt/sources.list


Adım 2-1-2 : Daha sonra, paketlerin bütünlüğünden emin olmak için uygun GPG imzalama anahtarını yüklemeniz gerekir:
~$ wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | sudo apt-key add -


Adım 2-1-3 : Yerel paket kaynaklarının bir güncellemesinden sonra, parmak izi paketini kurabilirsiniz:
~$ sudo apt-get update
~$ sudo apt-get install python-fingerprint


Adım 2-1-4 : Raspberry Pi'niz ile dönüştürme kartını kullanarak parmak izi sensörünü bağlarsanız,
cihaz "/ dev / ttyUSB0" yolu ile kullanılabilir hale gelmelidir. Varsayılan olarak sadece root kullanıcısı seri cihazları kullanabilir.
Normal kullanıcının (örn. "Pi") parmak izi sensörünü kullanabildiğinden emin olmak için onu "dialout" kullanıcı grubuna eklemelisiniz:
~$ sudo usermod -a -G dialout pi

Adım 2-1-5 : Şimdi sisteminizi yeniden başlatmanız gerekiyor.

Adım 2-2 :Debian üzerinde paket oluşturma

Adım 2-2-1 :İlk önce bina paketlerini kurun:
~$ sudo apt-get install git devscripts

Adım 2-2-2:Bu linkdeki dosyayı klonlayın:

~$ git clone https://github.com/bastianraschke/pyfingerprint.git

Adım 2-2-3:Paketi oluşturun:

~$ cd ./pyfingerprint/src/
~$ dpkg-buildpackage -uc -us
 

Adım 2-3 :Kurulum

Kütüphane, Python 2 ve Python 3'ü destekler. Her biri için bir Debian paketi vardır. Hangi sürümü kurduğuna bağlı.

Adım 2-3-1 :Python 3 kullanımı için:

~$ sudo dpkg -i ../python3-fingerprint*.deb

Adım 2-3-1 :Python 2 kullanımı için:

~$ sudo dpkg -i ../python-fingerprint*.deb

Adım 2-3-2:Eksik bağımlılıkları yükle:

~$ sudo apt-get -f install


Kütüphane kullanımı 

Yeni bir parmak kaydet

~$ python /usr/share/doc/python-fingerprint/examples/example_enroll.py

Kayıtlı bir parmağı arayın

~$ python /usr/share/doc/python-fingerprint/examples/example_search.py

Kayıtlı bir parmağı sil

~$ python /usr/share/doc/python-fingerprint/examples/example_delete.py

Ancak bu kısımda anlatılanlar bireysel kullanım için bizim kodumuza uygun hale getirilmiş parmak izi dosyaları linkte mevucttur
kurulumu tamamladıktan paroliz dosyasını çalıştırdığınızda sistemimiz çalışmaya hazır olacaktır.


Adım 3 : LCD Ekran için gerekenler
Adım 3-1: Verilen linkteki dosyaların içerisinde 2 tane lcd kütüphane dosyası mevcuttur ve hiç bişey yapmanıza gerek yoktur
bu doslayaları paroliz dosyamıza import etmiş durumdayız yeterki tüm dosyalar yanyana olsun

Adım 4 :SİSTEMİ ÇALIŞTIRMAK
Buraya kadar Parmak izi sensörünün ve LCD ekranın kurulumlarını yapmış olduk.Sırada parmak izi sensörünü USB dönüştürücüye,
USB yi raspberry e takmak ve LCD ekranı raspberrye bağladıktan sonra indirilen dosyaların içerisindeki Paroliz adlı dosyayı
çalıştırmak kaldı.


Github Linki:
https://github.com/muhammetoz/Paroliz


Çalıştırma videosu:
https://youtu.be/yDyp8Kgfn04

import example_delete#Parmak izi kütüphanesi
import example_search#Parmak izi kütüphanesi
import example_enroll#Parmak izi kütüphanesi
import time#zaman kütüphanesi
import lcddeneme#lcd kütüphanesi
example_delete.temizle()#parmak izi sensörümüzün bellegini temizledik
onur = ["Onur", 111, 1]#burada ve alt satırlarda şifre tanımlamaları ve gerekli değişkenleri oluşturduk
muhammet = ["Muhammet", 112,0]
yeni1=["",0,0]
yeni2=["",0,0]
yeni3=["",0,0]
ekli=1
silik=0
def sifregir(yeni):#şifre isteme ve kontrol etme fonksiyonu
    if (yeni == 0):
        lcddeneme.yaz("Lutfen Sifrenizi","Giriniz :")
        deger=int(input("Lütfen Sifrenizi Giriniz :"))
        ax=len(str(deger))
        if(deger==444 or deger== 111 or deger == 112):
            return int(deger)
        if(ax != 4):
            deger = -4
        return int(deger)
    elif(yeni==1):
      lcddeneme.yaz("Onur ","Sifreni Gir:")  
      on=int(input("Onur sifreni gir:"))
      if(on==onur[1]):
          lcddeneme.yaz("Muhammet","Sifreni gir:")
          mu=int(input("Muhammet sifreni gir:"))
          if(mu==muhammet[1]):
            lcddeneme.yaz("Lutfen Sifrenizi","Olusturun:")
            sif1 = int(input("Lütfen sifrenizi olusturun:"))
            lcddeneme.yaz("Lutfen Sifrenizi","Tekrar Giriniz:")
            sif2 = int(input("Lütfen sifrenizi tekrar giriniz:"))
            if (len(str(sif1)) != 4):
                 lcddeneme.yaz("Sifreniz Dort", "Haneli Olmalidir")
                 time.sleep(3)
            elif (sif1 == sif2):
              deger=sif1
            else:
                 lcddeneme.yaz("Sifreler","Eslesmiyor")
                 time.sleep(2)
                 deger=-1
          else:
              lcddeneme.yaz("Hatali", "Sifre")
              time.sleep(2)
              deger = -1
      else:
        lcddeneme.yaz("Hatali", "Sifre")
        time.sleep(2)
        deger=-1
    elif(yeni==2):
        lcddeneme.yaz("Onur","Sifreni gir:")
        on = int(input("Onur sifreni gir:"))
        if (on == onur[1]):
            lcddeneme.yaz("Muhammet","Sifreni gir:")
            mu = int(input("Muhammet sifreni gir:"))
            if(mu==muhammet[1]):
                deger = kisisil()
            else:
                lcddeneme.yaz("Hatali", "Sifre")
                time.sleep(2)
                deger=-4
        else:
            lcddeneme.yaz("Hatali", "Sifre")
            time.sleep(2)
            deger=-4
    return deger

def kisisil():#kişi silmek istediğimiz zaman gerçeklesek işlemler için gerekli olan kodlarımız
    lcddeneme.yaz("Kullanici Sil:","1.     2.     3.")
    sil=int(input("1)Kullanici 1\n2)Kullanici 2\n3)Kullanici 3\nLütfen silinecek kullaniciyi secin: "))
    global silik
    if(sil==1):
        global yeni1
        mmm=4
        yeni1 = ["", 0, 10000]
        silik = 1
        mmm=int(example_delete.silme(1))
        return mmm

    elif(sil==2):
        global yeni2
        yeni2 = ["", 0, 10000]
        silik = 2
        mmm=int(example_delete.silme(2))
        return mmm
    elif(sil==3):
        global yeni3
        mmm=4
        yeni3 = ["", 0, 10000]
        silik = 3
        mmm=int(example_delete.silme(3))
        return mmm
    else:
        lcddeneme.yaz("Hatali", "Secim")
        time.sleep(2)
        return -4

def parmakoku(de):#parmak okumak için gerekli olan kodlarımız
    par = 0
    parm = 1
    if(de==0):
        parmakokun=example_search.hash()
        return parmakokun
    elif(de==1):
            parm=example_enroll.hash()
            return parm


def yenikisi(kacinci,zir):#yeni kişi şifreleri doğru girildiğinde yapılacakların yazıldığı kodlamalar
    paro=sifregir(1)
    global silik
    global ekli
    if(paro==-1):
        return -1
    else:
      iz=parmakoku(1)
      if(iz!=-10): 
        if(kacinci==1 or zir==1):
            global yeni1
            yeni1=["Kullanici 1",paro,iz]
            if(ekli!=4):
                ekli=2
            silik = 0
            return 1
        elif (kacinci == 2 or zir==2):
            global yeni2
            yeni2 = ["Kullanici 2", paro, iz]
            if(ekli!=4):
                ekli = 3
            silik = 0
            return 1
        elif (kacinci == 3 or zir==3):
            global yeni3
            yeni3 = ["Kullanici 3", paro, iz]
            if (ekli != 4):
                ekli = 4
            silik = 0
            return 1
        elif(ekli==4 and zir==0):
            lcddeneme.yaz("Bellek","Dolu")
            time.sleep(2)
            
            lcddeneme.yaz ("Lutfen","Kullanici Silin")
            time.sleep(2)
            return -2
        else:
            return -1
      else:
        return -1

def yenikisiarayüz():#Yönetici araytüz ekranı kodlamaları
   lcddeneme.yaz("1-Kullanici ekle","2-Sil   3-Geri",1)
   secim = int(input("Lütfen seçiminizi yapiniz:"))

   if (secim==1):
           don=yenikisi(ekli,silik)
           if(don==-1 or don==-2 ):
               lcddeneme.yaz("Kullanici","Olusturulamadi")
               time.sleep(2)
               return
           elif(don==1):
               lcddeneme.yaz("Kullanici","Eklendi")
               time.sleep(2)
               return

   elif (secim == 2):
           don = sifregir(2)
           if (don == 4):
               lcddeneme.yaz("Kullanici","Silindi")
               time.sleep(2)
               return
           elif (don == -4):
               lcddeneme.yaz("Kullanici","Silinemedi")
               time.sleep(2)
               return

   elif(secim==3):
       return

   else:
       lcddeneme.yaz("Hatali","Secim")
       time.sleep(2)
       return

while(1):#sonsuz döngü oluşturduk
  try:#hataları yakalamak için gerekli kod

    sifre=sifregir(0)#şifre isteyip fonksiyona gönderdik
    if (sifre == 444):#Arayüz şifresi mi diye kontrol ettik
        yenikisiarayüz()#arayüz şifresiyse fonksiyonunu çağırdık
    else:
        parmak = parmakoku(0)#degilse parmak izi fonksiyonnu çağırdık
        if (sifre==onur[1] and onur[2]==parmak ):#buradan
                lcddeneme.yaz("Hos geldin", onur[0])
                time.sleep(3)
        elif (sifre == muhammet[1] and muhammet[2] == parmak ):
                lcddeneme.yaz("Hos geldin ", muhammet[0])
                time.sleep(3)
        elif (sifre == yeni1[1] and yeni1[2] == parmak):
                lcddeneme.yaz("Hos geldin ",yeni1[0])
                time.sleep(3)
        elif (sifre == yeni2[1] and yeni2[2] == parmak):
                lcddeneme.yaz("Hos geldin", yeni2[0])
                time.sleep(3)
        elif (sifre == yeni3[1] and yeni3[2] == parmak):#buraya kadar şifre parmak izlerinin eşliğini kontrol edip sistemden taradık doğruysa çıkış verdik
                lcddeneme.yaz("Hos geldin", yeni3[0])
                time.sleep(3)
        else:#yanlışsa çıkışımızı verdik
            lcddeneme.yaz("Hatali Sifre","veya Parmak izi")
            time.sleep(3)
  except:
        lcddeneme.yaz("Hatali","Giris!")
        time.sleep(3)



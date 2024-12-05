import datetime,time
# kütüphaneleri çağırdık time.sleep ve datetime komutları için.
nick = ""
Envanter = {"kuşkonmaz": [10,5],"brokoli": [15,6],"havuç": [18,7],"elmalar": [20,5],"muz":
[10,8],"meyve": [30,3],"yumurta": [50,2],"karışık meyve suyu": [0,18],"balık çubukları":
[25,12],"dondurma": [32,6],"elma suyu": [40,7],"portakal suyu": [30,8],"üzüm suyu": [10,9]}
#Aşşağıda kullanıcı adı ve şifre tanımlamalarını yaptık.
kullanıcı = {"ahmet":"İstinye123","meryem":"4444","a":"a"}
urun_ekleme=""
sepet = {}
secim = ""
#yukarıda görüldüğü gibi sözlükler tanımladık.
print("***********************************************")
print("**** İstinye Online Market’e Hoşgeldiniz ****\n")
print("***********************************************")
#hjasbdjashdbajdhajhd1123123123131231231231
#shahdahsdhas11111
#Beğendim Lİkeasdasdasd asdadasdasdad
#Kerem Tabanca Burada Bir Değişiklik yaptı !!!!
#Beğendim Lİke

#kullanıcıdan bilgilerini girmesini(pdf te verildiği gibi) sağladık.
def giris_ekranı():
    
    global nick
    print("Lütfen bilgilerinizi kullanarak giriş yapın..\n")
    kontrol1=True
    while kontrol1:
        nickname = input("Kullanıcı Adı: ")
        password = input("Şifre: ")
        if nickname in kullanıcı and kullanıcı[nickname]==password:
            time.sleep(0.7)
            print("*******************")
            print("****HOSGELDINIZ****")
            print("*******************\n")
            nick = nickname
            kontrol1 = False
        else:
            print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin\n")
#menüler fonksiyonunu tanımladık ve içeriklerini oluşturmuş bulunmaktayız.

def menuler():
    global secim
    print("Lütfen aşağıdaki menülerden birini seçin")
    print(" 1. Ürün Ara \n 2. Sepete Git \n 3. Satın al \n 4. Oturum Kapat \n 5. Çıkış Yap")
    
    kontrol2=True
    while kontrol2:
        secim = input("Seçiminiz: ")
        try:
            if int(secim) > 0 and int(secim) < 6:
                print("Yaptığınız Seçim: ", secim)
                kontrol2 = False
            else:
                print("Yanlış bir sayı girdiniz.!")

#kullanıcı harf girmesi durumunda kodun hata vermesini ve rakam girmesi yönünde direktifte bulunuyoruz.
       
        except ValueError:
            print("Lütfen rakam giriniz.!")

#Aşşağıda ürün arama fonksiyonunu tanımladık.
def urun_arama():
    global urun_ekleme
    bulunanlar={}
    sayı = 1
    
    isim=input("Aratmak istediğiniz ürün : ")
    
    for i in Envanter.keys():      
            if isim in i and Envanter.get(i)[0]>0:             
                
                bulunanlar[i]=str(Envanter[i][1])
#görüldüğü üzere .keys ve .get komutlarından yardım aldık.            
                
          
    if not bulunanlar:
        print("\nAranan değer bulunamadı Ana Menüye Dönmek İçin '0'\nTekrar arama için '1' basınız: ")
        a=input("Seçiminiz : ")
        if a=="1":
            urun_arama()
        else:pass
    else :
        for i in bulunanlar:
            message="{}. {} Adet Fiyatı: {}"
            print(message.format(sayı,i,bulunanlar[i]+" $"))
            sayı = sayı + 1
            time.sleep(0.6)
        urun_ekleme=int(input("Eklemek istediğiniz ürünü seçin(Ana Menüye dönmek için 0'a basınız): "))
        
        if urun_ekleme == 0:
            menuler()
            
        elif urun_ekleme > len(bulunanlar):
            print("geçersiz")
        else:
            sayı = 1
            for i in bulunanlar:
                if sayı == int(urun_ekleme):
                    sepete_ekleme(i)
                sayı = sayı + 1

#Sepet ekleme fonksiyonunu görüldüğü üzere aşşağıda tanımladık.           
        
def sepete_ekleme(name):
    global urun_ekleme
    kontrol4=True
    while kontrol4:
      
        
        kac_tane= int(input("Bu Üründen Kaç Adet Almak İstersiniz: "))
        if kac_tane>0 and kac_tane <= Envanter[name][0]:
            if not sepet.get(nick):
                sepet[nick]={name:[int(kac_tane),Envanter[name][1]]}
                
                time.sleep(2)
                print("\nİstediğiniz Ürün Sepete Ekleniyor")
                kontrol4=False
                print("\n")
            else:
                sepet[nick].update({name:[int(kac_tane),Envanter[name][1]]})
                time.sleep(2)
                break
        else:
            a=input("Miktar fazla veya Stokta Yok. (Çıkmak için 0 tekrar miktar girmek için 1): ")
            if(a=="0"):
                break
        
#sepete git fonksiyonunda; sepette ki ürünleri gösterme, toplam fiyat gösterme yaptırdık.
def sepete_git():
    if not sepet.get(nick):
        print("Sepetiniz Boş ")
    else:    
        print("Sepetinizde ki Ürünler: ") 
        sayi=1
        toplam=0 
        for i in sepet[nick]:
            toplam = toplam + (sepet[nick][i][1] * sepet[nick][i][0])
            print("{}. {}  {} Adet Fiyatı {} $ ".format(sayi,i,sepet[nick][i][0],sepet[nick][i][1]))
            sayi = sayi + 1
        print("\n Toplam Fiyat:{}$\n".format(toplam))
    
# alt menu fonksiyonunda biz; fonksiyonları çağırma bölümlerini tanımladık, kullanıcıya menü seçimini yaptırdık.
#hatalı giriş yapmasını durumunda tekrardan giriş yapması konusunda direktirfte bulunduk.

def alt_menu():
    while True:
        print("\nBir Seçeneği Seçiniz: \n 1.Tutarı Güncelleyin \n 2. Bir Ürünü Kaldırma \n 3. Satın Al \n 4. Ana Menuye Dön")
        secim = int(input("Menü Seçiminiz:\n "))
        if int(secim)==1:
            sepet_guncelleme()
            break
        elif int(secim)==2:
            ürün_kaldırma()
            break
        elif int(secim)==3:
            time.sleep(0.69)
            öde()
            break
        elif int(secim)==4:
            break
        else:
            print("Hatalı Giriş Yaptınız Lütfen Tekrar Giriniz")
            



 
def öde():
    global sepet
    # Aşşağıda ki fonksiyonumuzda biz kullanıcının eğer sepeti boş ise sepetinin boş olduğunu
    if not sepet.get(nick):
         print("Sepetiniz boş!")
    else:
         # makbuz bastırma bölünü burada tanımladık 
         print("\nMakbuzunuz işleniyor ...")
         print("******* İstinye Online Market ********")
         print("************************************* 0850 283 6000\nistinye.edu.tr")
         print("———————:———\\")
         print("Sepetinizde bulunan ürünler:\n") 
         sayi=1
         toplam=0 
         for i in sepet[nick]:
             #sepette bulunan ürünleri kullanıcıya burada gösterdik.
             toplam = toplam +(sepet[nick][i][1] * sepet[nick][i][0])
             print("{}. {} ürününden {} tane {} $ fiyatında. Toplam {} $".format(sayi,i,sepet[nick][i][0],sepet[nick][i][1],sepet[nick][i][1] * sepet[nick][i][0]))
             sayi = sayi + 1
             Envanter[i]=[Envanter[i][0]-sepet[nick][i][0],Envanter[i][1]]
         print("\nToplam Fiyat:{}$".format(toplam))
         tarih = datetime.datetime.now()
         #en sonunda ise bizi tercih için kullanıcıya teşekkür ettik 
         print("{}\nOnline Market’imizi kullandığınız için teşekkür ederiz!\n".format(tarih))
         sepet.pop(nick)
         giris_ekranı()    
    
    
    
# ürün kaldırma fonksiyonumuzu aşşağıda görebilirsiniz.   
def ürün_kaldırma():
    sepet[nick].pop(control2())
    
#sepet güncelleme fonksiyonumuzda kullanıcıya yeni miktar girmesini sağladık
#kullanıcı eğer ürün adedini değiştirmek isterse sıfıra indiremeyeceğini belirttik    
def sepet_guncelleme():
    while True:
        c=control1()
        a=int(input("Yeni Miktarı Giriniz:  "))
        
        if a >= 1:
            sepet[nick].update({c:[int(a),sepet[nick][c][1]]})
            break
        else: 
            print("Ürünün Adetini Sıfıra İndiremezsiniz Tekrar Giriş Yapın.")

def control1():
    while True:
         liste=[]
         for i in sepet[nick]:
             liste.append(i)
         for i in range(0,len(liste)):
             print("{}. ürün {}".format(i+1,liste[i]))
         a = int(input("\nGüncellemek İsteğiniz Ürünü Seçiniz: "))
        
  
         if(a>=1 and a <=len(liste)):             
             return liste[a-1]
         else:
             print("\nHatalı Seçim yaptınız.")
             a=int(input("Tekrar Seçiniz: "))
def control2():
    while True:
        liste=[]
        for i in sepet[nick]:
            liste.append(i)
        for i in range(0,len(liste)):
            print("{}. ürün {}".format(i+1,liste[i]))
        a = int(input("\nKaldırmak İstediğiniz Ürünü Seçiniz : "))
        
  
        if(a>=1 and a <=len(liste)):             
            return liste[a-1]
        else:
            print("\nHatalı Seçim yaptınız.")
            a=int(input("Tekrar Seçiniz: "))
         
            #bütün fonksiyonları ve menü içi dağıımları burada gerçekleştirdik.
            #Projemiz eksiksiz ve istenildiği gibi özenle hazırlanmıştır.
def main_fonks():
    kontrol8=True
    global secim,bulunanlar
    giris_ekranı()
    while kontrol8:
        menuler()
        if int(secim)==1:
            time.sleep(0.8)
            urun_arama()
            kontrol8 = True
        elif int(secim)==2:
            time.sleep(0.3)
            print("Sepete Yönlendiriliyorsunuz.")
            time.sleep(0.7)
            sepete_git()
            if len(sepet[nick])>0:
                alt_menu()
            else:
                print("Sepet boş Ana Menüye Dönülüyor..")
                time.sleep(0.5)
        elif int(secim)==3:
            time.sleep(0.69)
            öde()
        elif int(secim)==4:
            time.sleep(0.6)
            giris_ekranı()
        elif int(secim)==5:
            print("Bizi tercih ettiğiniz için teşekkürler")
            kontrol8=False
        
                   




main_fonks()
#KEREM TABANCA 

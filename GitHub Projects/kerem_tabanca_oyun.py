import random,time

hero1=""
hero2=""
hp1=100
hp2=100
#Oyunumuzun giriş ekranı.
print("--ISTINYE KOMBAT ARENASINA--")
print("---------HOSGELDINIZ--------\n")
#Kahramanlarımızın isim girdileri yazılmıştır.
def isimler():
    global hero1,hero2
    kontrol1=True
    while kontrol1:
        print("-------------------------")
        print("----BIRINCI SALDIRGAN----")
        print("-------------------------")
        hero1=input('SAVAŞÇIYA ISIM VER : ').strip()
        if hero1=="":
             print("\n ISIMSIZ SAVAŞÇI OLMAZ LÜTFEN BIR ISIM VERIN !!  \n")
        else:
            kontrol1==False
            break
    kontrol2=True
            
    kontrol2=True
    while kontrol2:
        print("--------------------------")
        print('-----IKINCI SALDIRGAN-----')
        print("--------------------------")
        hero2=input('SAVAŞÇIYA ISIM VER : ').strip()
        #İsimlerin aynı olma koşulunda tekrar isim istenir.
        if hero1==hero2:
            print("BU ISIM ALINDI BAŞKA BİRİNİ SEÇ  !!")
            kontrol2=True
        
        elif hero2=="" :
            print("\n ISIMSIZ SAVAŞÇI OLMAZ LÜTFEN BIR ISIM VERIN !! \n")
        else:
            kontrol2==False
            break
    kontrol2=True
             
           
    
    return hero1,hero2 
    

#Burada oyuna başlayacak kişi %50 ihtimal dahilinde seçilmiştir.
def yazituraatmak():
    print("\n DÖVÜŞ BAŞLIYOR..!!! \n")
    global hero1,hero2
    #2 sn gecikme ekliyoruz.
    time.sleep(2)
    ilk_oyuncu=random.choice([hero1,hero2])
    if ilk_oyuncu==hero2:
        x=hero1
        hero1=hero2
        hero2=x
        
#Can istatistikleri ekrana dökülmüştür.    
def hp_and_sticks():
    space_between_names = (74 - len(hero1)) * " "
    
    sticks1="♥"*(hp1//2)
    sticks2="♥"*(hp2//2)

    if 10 <= hp1 <= 99:
        hp1_space = (67 - len(sticks1)) * " "
    elif hp1 < 10:
        hp1_space = (68 - len(sticks1)) * " "
    else:
        hp1_space = (66 - len(sticks1)) * " "

    print(hero1,space_between_names,hero2)

    print("HP[{}]:{}".format(hp1,sticks1),hp1_space,"HP[{}]:{}".format(hp2,sticks2))
    return hp1,hp2
    


#Bu fonksyonda ise saldıran kişinin vereceği hasar miktarını alıyoruz. 
def saldiri_mik():
    global hp2
    
    print(hero1,'SALDIRIYOR !!')
    verilenhasar=int(input("1-50 ARASINDA BIR SAYI GIRINIZ :"))
    olasilik=100-verilenhasar
    rand=random.randint(1,100)
    #Burada verilmek istenen hasarın miktarını filtreliyoruz.
    while True:
        if verilenhasar>50:
            verilenhasar=int(input("1-50 Arasında Bir Sayı Yazınız.. : "))
        elif verilenhasar<=50:
            break
    #Verilmek istenen hasarın verilip verilmediğini konrol ediyoruz.
    if olasilik>=rand:
        time.sleep(0.30)
        hp2=hp2-verilenhasar
        print("\n AMAN ALLAHIM MÜKEMMEL BIR SALDIRI !! ")
   
    else:
        print("\n ISKALADIN HA HA HA !")
    
     
#Bu fonksyonumuzda oyuncuların sırasıyla yerlerini değiştirmesini sağlıyoruz.
def oyuncu_degis():
    global hero1,hero2,hp1,hp2
    x=hero1
    hero1=hero2
    hero2=x
    z=hp1
    hp1=hp2
    hp2=z
#Burada oyunun sonucunu kontrol ediyoruz.
def oyun_sonucu():
    if hp1<=0:
        print(hero2,"ISIMLI KAHRAMAN KAZANMAYI HAKETTI !! " ,hero1, "KAYBETTIN HA HA HA ☠️☠️!!")
        
        return False
    elif hp2<=0:
        print(hero1,"ISIMLI KAHRAMAN KAZANMAYI HAKETTI !!" ,hero2, "KAYBETTIN HA HA HA ☠️☠️!!")
        
        return False
    else:
        return True
        
        
#Genel olarak yazdığımız bütün fonksyonları çağırıyoruz.
def cagir():
    global hp1,hp2
    isimler() 
    
    key=True
    main_key=True
    
    while main_key:
        yazituraatmak()
        while key :
           
            hp_and_sticks()
            saldiri_mik()
            oyuncu_degis()
            key=oyun_sonucu()
#Oyuncuya tekrar oynayıp oynamak istemediğini soruyoruz ve cevap çıktısı alıyoruz
        tekrar=input("BIR DAHA DÖVÜŞMEK ISTER MISIN  Y/N ? : ")
        if tekrar=="N" or tekrar=="n":
           main_key=False
           key=False
           print("OYNADIĞINIZ IÇIN TEŞEKKÜR EDERIZ !!")
        if tekrar=="Y" or tekrar=="y":
            key=True
            print("TEKRAR SAVAŞMAYA HAZIR OL !! ")
            hp1=100
            hp2=100
            
 
            
cagir()




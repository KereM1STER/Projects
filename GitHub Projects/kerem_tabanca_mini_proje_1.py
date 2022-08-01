# -*- coding: utf-8 -*-

import time
#Kod başlatıldığında ekrana karşılama mesajı basıyoruz.
print('\n*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*')
print('\n-----------HOŞGELDİNİZ------------')
print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

# Kullanıcının Adını Alalım
isim=input('Adınızı Girin:')

  
kredi_mik=float(input('Kredi Miktarı:'))

# Kullanılan Faiz 
faiz_oran=float(input('Ne Kadar Faiz Koyalım:'))

max_yıl=int(input('Kaç Yılda Ödemek Istersin:'))

max_ay=int(input('Kaç Ayda Ödemek Istersin:'))

yineleme=int(input('Ödeme Sıklığı:'))

print('\nHESAPLANIYOR..')
print('HESAPLANIYOR..')
print('HESAPLANIYOR..\n')

#Bu kısım da hoş görüntü oluşturması için "Hesaplanıyor" kısmına 2 saniyelik bir bekleme süresi ekledim
time.sleep(2)



def print_duration(ay):
    # Bu Fonksiyon zamanı okunabilir şekilde ekrana basar.

    print(int(ay/12), 'Yıl ', ay%12, 'Ay ')
   
    
def print_money(para):
    print(format(para, '.1f'), '$')
    

def print_entry(kredi_tutarı, int_rate, ay):
   
    
    # İşleyecek faiz miktarı hesabı
    
    total_int_rate = (kredi_tutarı / 100) * (int_rate / 12) * ay
    
    # Toplam geri ödenecek tutar hesabı
    total_payment= total_int_rate + kredi_tutarı
    
    # Burada ödenecek olan tutarı ekrana basıyoruz.
    print('----------------------------\nToplam Ödeyeceğiniz Para:')
    print_money(total_payment)
    
    print('Aylık Ödeyeceğiniz Para:')
    print_money(total_payment/ay)
    
    print('----------------------------\n')



def print_full_report(kredi_mik, faiz_oran, max_yıl, max_ay, yineleme):
    y=yineleme
    toplam_ay=max_ay + (max_yıl*12)
    #Ortaya çıkacak toplam ödeme planının hesabı
    while(y<=toplam_ay):
         print_duration(y)
         
        
         print_entry(kredi_mik, faiz_oran, y)
         
         y=yineleme+y
         
print_full_report(kredi_mik, faiz_oran, max_yıl, max_ay, yineleme)
    

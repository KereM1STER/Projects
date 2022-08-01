#include <iostream>
#include <string.h>
#include <stdlib.h>
#include "headerdosyasý.h"
#include <conio.h>
#include <Windows.h>
#include <unistd.h>
using namespace std;


// BURADA KÜTÜPHANEMÝZE KÝTAP EKLÝYORUZ
void kitap::addbook() {
    cin.ignore();
    cout << "Kitap ismi girin: " << endl;
    cin.getline(isim, 20);
    cout << "Kitap kodunu girin: " << endl;
    cin >> *kod;
    cout << "\nEklendi !!" << endl;
    sleep(1.5);
    system("cls");
}
// SEÇÝLEN KÝTABI GÖSTERÝYORUZ
void kitap::kitapgoster() {

    if (*isim == NULL) {
        cout << "Kitap Bulunamadý" << endl;

    }
    else {
        cout << "\nKitap Ismi: " << isim << endl;
        cout << "\nKitap kodu: " << *kod << endl;

    }
}
//BURADA KÝTAP ÝSMÝ ÝLE ARAMA GERÇEKLEÞTÝRÝYORUZ
int kitap::search(char iarat[20]) {
    if (strcmp(iarat, isim) == 0)
        return 1;

    else return 0;
}
//BURADA ÝSE KÝTABIMIZIN KODU ÝLE ARAMA GERÇEKLEÞTÝRÝYORUZ POINTER KULLANARAK
int kitap::koddanbul(int kodarat) {
    if (kodarat == *kod)
        return 1;

    else return 0;
}
//KÝTAPLARIMIZI SÝLMEMÝZÝ SAÐLAYAN FONKSIYON
void kitap::kitapsil() {
    int sayi;
    cout << "Silmek istediðin kitabýn kodu" << endl;
    cin >> sayi;
    if (sayi <= *kod) {
        *kod = *kod - sayi;
        *isim = NULL;
        cout << "Kitap baþarýyla silindi. " << endl;
		sleep(1.5);

    }
    else cout << "Kitap Bulunamadý";
    system("cls");
    cout << "Menüye Dönülüyor.. ";
    sleep(1.5);


}
// BASÝT BÝR SATIN ALMA FONKSÝYONU
void kitap::satin_al() {
    int sayi;
    string adres;
    int fiyat = rand()%30;
    int kargo = 8;
    int onay;
    int cikis0;
    order:cout << "Satýn almak istediðin kitabýn kodu" << endl;
    cin >> sayi;


    cout << "Fiyat : " << fiyat << "TL" << endl;
    cout << "Kargo ücreti:  " << kargo << "TL" << endl;
    cout << "Toplam = " << fiyat + kargo << "TL" << endl;
// KULLANICIYA BAÞKA ÝÞLEM ÝSTEYÝP ÝSTEMEDÝÐÝNÝ SORUYORUZ
    cout << "Onaylýyor Musunuz ? (Evet için 1 && Hayýr için 2 tuþlarýný kullanýnýz)" << endl;
    cin >> onay;
    switch (onay)
    {
	// ONAY VERÝRSE TESLÝM EDÝLECEK ADRESÝ ALIYORUZ VE TEKRARDAN MENÜYE DÖNÜÞÜNÜ SAÐLIYORUZ
    case 1:
        if (sayi <= *kod) {
            *kod = *kod - sayi;
            *isim = NULL;
            cout << "Teslim edilecek yeri giriniz: " << endl;
            cin >> adres;
            cout << "Siparis alýndi. " << endl;
            cout << "Kitabiniz " << adres << "'e teslim edilmek üzere yarin yola cýkacak." << endl ;
            
            cout << "Baska Islem icin 1 , Cikis yapmak icin 2" << endl;
            cin >> cikis0;
            switch(cikis0){
            	case 1:
			        cout << "Menüye Dönülüyor.. ";
			        sleep(3);
					system("cls");
					break;
            	case 2:
            		cout << "Gorusmek Uzere... :)";
            		sleep(2);
            		exit(0);
            	default:
            		cout << "\nHatali Giris Yapildi...";
			}
			break;
			
            
        }
        else cout << "Kitap Bulunamadi";
    case 2:
    	// SÝPARÝÞÝN ÝPTALÝNÝ SAÐLAYIP ANA MENÜYE DÖNÜÞ SAÐLIYORUZ
        cout << "Siparis iptal edildi\n" ;
        sleep(1.5);
        cout << "Menüye Dönülüyor.. ";
        sleep(3);
		system("cls");
        
        break;
        
        
    default:
        cout << "\nHatali Giris Yapildi...";
            goto order;

    }
}


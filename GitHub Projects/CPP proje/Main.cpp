#include <iostream>
#include <string.h>
#include <stdlib.h>
#include "headerdosyas�.h"
#include <conio.h>
#include <Windows.h>
#include <unistd.h>
using namespace std;


// BURADA K�T�PHANEM�ZE K�TAP EKL�YORUZ
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
// SE��LEN K�TABI G�STER�YORUZ
void kitap::kitapgoster() {

    if (*isim == NULL) {
        cout << "Kitap Bulunamad�" << endl;

    }
    else {
        cout << "\nKitap Ismi: " << isim << endl;
        cout << "\nKitap kodu: " << *kod << endl;

    }
}
//BURADA K�TAP �SM� �LE ARAMA GER�EKLE�T�R�YORUZ
int kitap::search(char iarat[20]) {
    if (strcmp(iarat, isim) == 0)
        return 1;

    else return 0;
}
//BURADA �SE K�TABIMIZIN KODU �LE ARAMA GER�EKLE�T�R�YORUZ POINTER KULLANARAK
int kitap::koddanbul(int kodarat) {
    if (kodarat == *kod)
        return 1;

    else return 0;
}
//K�TAPLARIMIZI S�LMEM�Z� SA�LAYAN FONKSIYON
void kitap::kitapsil() {
    int sayi;
    cout << "Silmek istedi�in kitab�n kodu" << endl;
    cin >> sayi;
    if (sayi <= *kod) {
        *kod = *kod - sayi;
        *isim = NULL;
        cout << "Kitap ba�ar�yla silindi. " << endl;
		sleep(1.5);

    }
    else cout << "Kitap Bulunamad�";
    system("cls");
    cout << "Men�ye D�n�l�yor.. ";
    sleep(1.5);


}
// BAS�T B�R SATIN ALMA FONKS�YONU
void kitap::satin_al() {
    int sayi;
    string adres;
    int fiyat = rand()%30;
    int kargo = 8;
    int onay;
    int cikis0;
    order:cout << "Sat�n almak istedi�in kitab�n kodu" << endl;
    cin >> sayi;


    cout << "Fiyat : " << fiyat << "TL" << endl;
    cout << "Kargo �creti:  " << kargo << "TL" << endl;
    cout << "Toplam = " << fiyat + kargo << "TL" << endl;
// KULLANICIYA BA�KA ��LEM �STEY�P �STEMED���N� SORUYORUZ
    cout << "Onayl�yor Musunuz ? (Evet i�in 1 && Hay�r i�in 2 tu�lar�n� kullan�n�z)" << endl;
    cin >> onay;
    switch (onay)
    {
	// ONAY VER�RSE TESL�M ED�LECEK ADRES� ALIYORUZ VE TEKRARDAN MEN�YE D�N���N� SA�LIYORUZ
    case 1:
        if (sayi <= *kod) {
            *kod = *kod - sayi;
            *isim = NULL;
            cout << "Teslim edilecek yeri giriniz: " << endl;
            cin >> adres;
            cout << "Siparis al�ndi. " << endl;
            cout << "Kitabiniz " << adres << "'e teslim edilmek �zere yarin yola c�kacak." << endl ;
            
            cout << "Baska Islem icin 1 , Cikis yapmak icin 2" << endl;
            cin >> cikis0;
            switch(cikis0){
            	case 1:
			        cout << "Men�ye D�n�l�yor.. ";
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
    	// S�PAR���N �PTAL�N� SA�LAYIP ANA MEN�YE D�N�� SA�LIYORUZ
        cout << "Siparis iptal edildi\n" ;
        sleep(1.5);
        cout << "Men�ye D�n�l�yor.. ";
        sleep(3);
		system("cls");
        
        break;
        
        
    default:
        cout << "\nHatali Giris Yapildi...";
            goto order;

    }
}


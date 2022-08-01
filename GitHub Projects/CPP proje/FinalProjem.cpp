//KODUMUZUN BEL KEMIÐI OLAN MAIN FONKSYONUMUZ
int main()
{
    //GEREKLÝ DEÐÝÞKENLERÝ TANIMLIYORUZ
    kitap* K[100];
    int i = 0, r, t, k,  p ,  secim, secim2, kodarat;
    char isimarat[20];
    
    cout << "------------$$$$$-------------" << endl;
    cout << "------------------------------" << endl;
    cout << "---KUTUPHANEYE HOS GELDINIZ---" << endl;
    cout << "------------------------------" << endl;
    cout << "------------$$$$$-------------" << endl;
menu:while (1) {
	//MENÜMÜZÜ OLUÞTURUYORUZ
    cout << "\nMENU" << endl << endl;
    cout << "1. Kitap Ekle" << endl;
    cout << "2. Kitap Arat" << endl;
    cout << "3. Cikis yap" << endl;
    cout << "4. Kitap Sil" << endl;
    cout << "5. Kitap Satin Al" << endl;
    cout << "Lutfen Secim Yapiniz: ";
    cin >> secim;
    system("cls");
    switch (secim)
    {
    case 1:
        //MENÜ SEÇÝMÝNDEN SONRA KÝTAP EKLEME FONKSYONUNU ÇAÐIRIYORUZ
        K[i] = new kitap;
        K[i]->addbook();
        i++;
        
        goto menu;
    menu2:case 2:
        //BURADA KÝTAP ARATMA KISMIMIZ ÝÇÝN TEKRAR MENÜ OLUÞTURUYORUZ KODLA YA DA ÝSÝMLE
        cout << "1. Isimle arat." << endl;
        cout << "2. Kodla arat." << endl;
        cout << "3. Menuye Don. " << endl;
        cin >> secim2;
        switch (secim2)
        {
        case 1:
            cin.ignore();
            cout << "\nKitap ismi girin: "; cin.getline(isimarat, 20);


            for (t = 0; t < i; t++) {
                if (K[t]->search(isimarat)) {
                    cout << "\nElimizde Var." << endl;
                    sleep(1.5);
                    K[t]->kitapgoster();


                }
                else {
                    cout << "\n\nElimizde Yok." << endl;

                    
                }
            }
            goto menu;

        case 2:
            cout << "\nKitap kodu girin: ";
            cin >> kodarat;
            system("cls");
            for (t = 0; t < i; t++) {
                if (K[t]->koddanbul(kodarat)) {
                    cout << "\nElimizde Var." << endl;
                    K[t]->kitapgoster();

                    goto menu;
                }
                else {
                	
                    cout << "Kitap Bulunamadý";
                    goto menu;
                }

            }
            
        case 3:
	        sleep(1.5);
	        cout << "Menüye Dönülüyor.. ";
	        sleep(3);
			system("cls");
			goto menu;
        default:
            cout << "\nHatali Giris Yapildi." << endl;

            goto menu2;

        }

// KODU KAPATIYORUZ
    case 3:
		cout << "Gorusmek Uzere... :)";
		sleep(2);    	
        exit(0);
        // KÝTAP SÝLMEMÝZE YARAYAN FONKSÝYONU TANIMLIYORUZ
    case 4:
        for (k = 0; k < i; k++) {
            if (K[k]->koddanbul(kodarat)) {
                K[k]->kitapsil();

                goto menu;
            }
        }
// SATIN ALMAMIZA YARAYAN FONKSYON
    case 5:
        for (p = 0; p < i; p++) {
            if (K[p]->koddanbul(kodarat)) {
                K[p]->satin_al();

                goto menu;
            }
        }
       

    default:
        cout << "\n\nYanlis Secim Yapildi." << endl;
		
        goto menu;
    }
}

return 0;
}
// 201216064 KEREM TABANCA ADLI ÖÐRENCÝNÝN PROJESÝ
//PROGRAMIN ÝÇÝNDE BAZI BUGLAR BULUNMAKTA ÇÖZÜMLERÝNÝ NE YAZIK KÝ YAPAMADIM
// EÐER ÝLK DENEMEDE SILME VE SATIN ALMA KOMUTLARINI ÇALIÞTIRAMAZSANIZ KITAP EKLEDIKTEN SONRA ARATIN (KODLA) SONRA ÝKÝ FONKSYONDA ÇALIÞIYOR
//YANÝ SIRALAMASI ÞÖYLE
// Kitap Ekle --> Kitap Arat (kodla aratmanýz gerekmekte) --> Kitap Çýkar ya da Kitap Satýn Al 
//BU SIRALAMAYLA ÇALIÞTIRIRSANIZ FONKSYONLARIN ÇALIÞTIÐINI GÖRECEKSÝNÝZ

//ELIMDEN GELEN BUYDU ILGINIZE TEÞEKKÜRLER..

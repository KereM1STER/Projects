//KODUMUZUN BEL KEMI�I OLAN MAIN FONKSYONUMUZ
int main()
{
    //GEREKL� DE���KENLER� TANIMLIYORUZ
    kitap* K[100];
    int i = 0, r, t, k,  p ,  secim, secim2, kodarat;
    char isimarat[20];
    
    cout << "------------$$$$$-------------" << endl;
    cout << "------------------------------" << endl;
    cout << "---KUTUPHANEYE HOS GELDINIZ---" << endl;
    cout << "------------------------------" << endl;
    cout << "------------$$$$$-------------" << endl;
menu:while (1) {
	//MEN�M�Z� OLU�TURUYORUZ
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
        //MEN� SE��M�NDEN SONRA K�TAP EKLEME FONKSYONUNU �A�IRIYORUZ
        K[i] = new kitap;
        K[i]->addbook();
        i++;
        
        goto menu;
    menu2:case 2:
        //BURADA K�TAP ARATMA KISMIMIZ ���N TEKRAR MEN� OLU�TURUYORUZ KODLA YA DA �S�MLE
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
                	
                    cout << "Kitap Bulunamad�";
                    goto menu;
                }

            }
            
        case 3:
	        sleep(1.5);
	        cout << "Men�ye D�n�l�yor.. ";
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
        // K�TAP S�LMEM�ZE YARAYAN FONKS�YONU TANIMLIYORUZ
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
// 201216064 KEREM TABANCA ADLI ��RENC�N�N PROJES�
//PROGRAMIN ���NDE BAZI BUGLAR BULUNMAKTA ��Z�MLER�N� NE YAZIK K� YAPAMADIM
// E�ER �LK DENEMEDE SILME VE SATIN ALMA KOMUTLARINI �ALI�TIRAMAZSANIZ KITAP EKLEDIKTEN SONRA ARATIN (KODLA) SONRA �K� FONKSYONDA �ALI�IYOR
//YAN� SIRALAMASI ��YLE
// Kitap Ekle --> Kitap Arat (kodla aratman�z gerekmekte) --> Kitap ��kar ya da Kitap Sat�n Al 
//BU SIRALAMAYLA �ALI�TIRIRSANIZ FONKSYONLARIN �ALI�TI�INI G�RECEKS�N�Z

//ELIMDEN GELEN BUYDU ILGINIZE TE�EKK�RLER..

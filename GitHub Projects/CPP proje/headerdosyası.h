
//SINIFIMIZI OLU�TURDUK
class kitap {
private:
char* isim;
int* kod;
public:
kitap() {


    isim = new char[20];
    kod = new int;
}
// GEREKL� FONKSYONLARI SINIFIMIZA EKLED�K
void addbook();
void kitapgoster();
int search(char[]);
void kitapsil();
int koddanbul(int);
void satin_al();
void cagir();

};



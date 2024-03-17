#include <iostream> // Library untuk input/output stream
using namespace std;

// Fungsi utama, program dimulai dari sini
int main() {
    // Kode program ditulis di dalam fungsi main()

    // Output teks ke layar
    cout << "Halo, dunia!" << endl;

    // Variabel dan tipe data
    int angka = 10;
    float angka_desimal = 3.14;
    char karakter = 'A';
    bool benar = true;

    // Operasi matematika
    int hasil_penjumlahan = 5 + 3;
    int hasil_pengurangan = 5 - 3;
    int hasil_perkalian = 5 * 3;
    int hasil_pembagian = 6 / 3;
    int sisa_pembagian = 7 % 3;

    // Percabangan if-else
    if (angka > 0) {
        cout << "Angka positif" << endl;
    } else if (angka < 0) {
        cout << "Angka negatif" << endl;
    } else {
        cout << "Angka nol" << endl;
    }

    // Perulangan while
    int i = 0;
    while (i < 5) {
        cout << "Nilai i: " << i << endl;
        i++;
    }

    // Perulangan for
    for (int j = 0; j < 5; j++) {
        cout << "Nilai j: " << j << endl;
    }

    return 0; // Mengembalikan nilai 0 untuk menandakan program berakhir dengan sukses
}

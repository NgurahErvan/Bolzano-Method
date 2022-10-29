# Implementasi Metode Bolzano
> Praktikum 1 Komputasi Numerik D

***

## Anggota Kelompok
1. I Gusti Ngurah Ervan Juli Ardana (5025211205)
2. I Gusti Agung Ngurah Adhi Sanjaya (5025211056)
3. Rayhan Almer Kusumah (5025211115)

---

### Metode Bolzano
Metode Bolzano merupakan salah satu metode yang sering digunakan untuk mencari akar-akar persamaan nonlinier melalui beberapa proses iterasi. Kita memerlukan dua buah variabel yang bernama `x1` dan `x2`. kedua variabel tersebut harus:
>`f(x1) > 0`\
`f(x2) < 0`

Maupun Sebaliknya:

>`f(x2) > 0`\
`f(x1) < 0`

Intinya kedua variabel tersebut jika f(x) nya dikalikan maka harus menghasilkan bilangan negatif. jika tidak maka kita harus mencoba kedua variabel yang baru. Kemudian kita harus mencari variabel xTengah dengan rumus:

>`xTengah = (x1 + x2)/2`

Kemudian xTengah harus menggantikan x1 atau x2 di iterasi selanjutnya dengan syarat:

> jika `f(XTengah) * f(X1) > 0`, maka `X1 = XTengah`\
jika `f(XTengah) * f(X1) < 0`, maka `X2 = XTengah`

diatas merupakan proses 1 iterasi. lakukan iterasi tersebut berulang ulang hingga `f(Xtengah)` mendekati `0` 

---
### Implementasi Metode Bolzano dengan Python
Berikut merupakan implementasi Metode Bolzano dengan bahasa Phyton

![bolzanomethod](https://user-images.githubusercontent.com/114007640/198838613-cefe2431-1191-4a58-9baf-4b7fe408408f.png)

Output yang akan dikeluarkan jika menggunakan fungsi `x**3 +x**2 - 3 *x -3` dan `x1 = 1 ` dan `x2 = 2`  yaitu:

![Output](https://user-images.githubusercontent.com/114007640/198838883-1f7f5ea7-957e-4b6c-a087-f0a9f4889906.png)

![Figure_1](https://user-images.githubusercontent.com/114007640/198838983-bc727485-0d6b-4c69-9631-17be57333eab.png)



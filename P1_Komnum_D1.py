import matplotlib.pyplot as plt
import numpy as np

# Menentukan Fungsi  yang akan digunakan
def f(x):
    return x**3 +x**2 - 3 *x -3
# Implementasi metode bolzano
def bolzano(x1, x2, e):
    iterasi = 1
    statement = True

    print("\n------Akar- akar didapatkan setelah melalui metode bolzano: ---------\n")
    while statement:
        xTengah = (x1 + x2) / 2
        print("Iterasi ke-%d --> x1 = %0.6f || x2 = %0.6f || xTengah = %0.6f || f(x1) = %0.6f || f(xTengah) = %0.6f" % (iterasi, x1,  x2, xTengah, f(x1) , f(xTengah)))

        #Mengganti nilai x1 dan x2 dengan nilai tengah sesuai nilai f(xTengah)
        if f(x1) * f(xTengah) < 0:
            x2 = xTengah
        else:
            x1 = xTengah

        iterasi += 1
        
        statement = abs(f(xTengah)) > e

    # print("\nRequired Root is : %0.8f" % x2)
    return xTengah

# menentukan x1 , x2 dan e nya
# e merupakan perbedaan maksimal antara metode bolzano dengan akar sebenernya
x1 = 1
x2 = 2
e = 0.1

# memeriksa jika x1 dan x2 yg dimasukan bernilai benar ( menghasilkan perbedaan tanda)
if f(x1) * f(x2) > 0.0:
    print("Tolong Berikan x1 dan x2 yang sesuai")
else:
    root = bolzano(x1, x2, e)
    print("\n Akar yg didapatkan yaitu : %0.8f" % root)

#mendeklarasikan x dan y untuk di plot nanti
x = np.arange(x1, x2, e)
y = f(x)

#animator
plt.xlabel("Koordinat x")
plt.ylabel("Koordinat y")
plt.title("Grafik Metode Bolzano")

def Graph():
    plt.plot(x, y, color = "#13EAC9", label="Grafik Fungsi", zorder=0)
    plt.axvline(x=root, ymin=0, ymax=1, color="green", label="Fungsi", zorder=1)
    plt.scatter(root, f(root), color="blue", linewidths=0.5, label="akar", zorder=2)
    plt.legend()
    plt.show()
Graph()

#sourceCode:
# https://www.codesansar.com/numerical-methods/bisection-method-python-program.htm

#sourceCode:
# https://www.codesansar.com/numerical-methods/bisection-method-python-program.htm

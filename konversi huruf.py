from tkinter import Variable

def konversiHurufKapital(huruf):
    hurufKapital = ""
    for i in huruf:
        if i == " ":
            hurufKapital += i
        else:
            hurufKapital += i.upper()
    return hurufKapital

huruf = input("Masukkan kata: ")
hasil = konversiHurufKapital(huruf)
print(hasil)

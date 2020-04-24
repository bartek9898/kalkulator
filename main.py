from tkinter import *
from math import *

root=Tk()

root.title("Moj Kalkulator")
root.resizable(0,0)

dzialanie=''


def wpisz(event,liczba):
    ekran.config(state='normal')

    global dzialanie
    dzialanie=ekran.get()
    ekran.delete(0, END)
    ekran.insert(0, str(dzialanie)+str(liczba))

    ekran.config(state='disabled')


def ln(liczba):
    return log(liczba,e)


def oblicz(event):
    ekran.config(state='normal')

    global dzialanie
    dzialanie=ekran.get()



    dzialanie=dzialanie.replace('ctg(','1/tan(')
    dzialanie=dzialanie.replace('rad(','radians(')
    dzialanie=dzialanie.replace('log(','log10(')
    dzialanie=dzialanie.replace('\/(','sqrt(')
    dzialanie=dzialanie.replace('%','/100')
    dzialanie=dzialanie.replace('^','**')
    dzialanie=dzialanie.replace('!(','factorial(')



    try:
        dzialanie=eval(dzialanie)
    except:
        dzialanie='Błąd'

    ekran.delete(0, END)
    ekran.insert(0, dzialanie)

    ekran.config(state='disabled')

def czysc(event):
    ekran.config(state='normal')
    ekran.delete(0, END)
    ekran.config(state='disabled')

def usun(event):
    ekran.config(state='normal')

    global dzialanie
    dzialanie=ekran.get()

    dzialanie = dzialanie.replace(dzialanie[len(dzialanie) - 1], "")

    ekran.delete(0,END)
    ekran.insert(0,dzialanie)

    ekran.config(state='disabled')

'''ekran'''
ekran=Entry(root,width=40,borderwidth=5,font=('Verdana',15),state='disabled')
ekran.grid(row=0,column=0,columnspan=5)



'''moduł zaawansowany'''

sinus=Button(root,padx=37,pady=3,borderwidth=4,text="sin", bg="grey")
cosinus=Button(root,padx=36,pady=3,borderwidth=4,text="cos", bg="grey")
tangens=Button(root,padx=37,pady=3,borderwidth=4,text="tan", bg="grey")
cotangens=Button(root,padx=37,pady=3,borderwidth=4,text="ctg", bg="grey")
radius=Button(root,padx=37,pady=3,borderwidth=4,text='rad', bg="grey")

sinus.grid(row=1,column=0)
cosinus.grid(row=1,column=1)
tangens.grid(row=1,column=2)
cotangens.grid(row=1,column=3)
radius.grid(row=1,column=4)

silnia=Button(root,padx=44,pady=3,borderwidth=4,text="!", bg="grey")
pierwiastek=Button(root,padx=37,pady=3,borderwidth=4,text="\/x", bg="grey")
potegowanie=Button(root,padx=36,pady=3,borderwidth=4,text="x^y", bg="grey")
logarytm_dziesietny=Button(root,padx=36,pady=3,borderwidth=4,text="log", bg="grey")
logarytm_naturalny=Button(root,padx=39,pady=3,borderwidth=4,text="ln", bg="grey")

logarytm_naturalny.grid(row=2,column=0)
logarytm_dziesietny.grid(row=2,column=1)
silnia.grid(row=2,column=2)
pierwiastek.grid(row=2,column=3)
potegowanie.grid(row=2,column=4)

nawias_lewy=Button(root,padx=43,pady=3,borderwidth=4,text="(", bg="grey")
nawias_prawy=Button(root,padx=44,pady=3,borderwidth=4,text=")", bg="grey")
procent=Button(root,padx=40,pady=3,borderwidth=4,text='%', bg="grey")
liczba_pi=Button(root,padx=40,pady=3,borderwidth=4,text="pi", bg="grey")
liczba_eulera=Button(root,padx=41,pady=3,borderwidth=4,text="e", bg="grey")

liczba_eulera.grid(row=3,column=0)
liczba_pi.grid(row=3,column=1)
procent.grid(row=3,column=2)
nawias_lewy.grid(row=3,column=3)
nawias_prawy.grid(row=3,column=4)

'''moduł liczb'''

liczba1=Button(root,padx=42,pady=20,borderwidth=4,text="1", bg="white")
liczba2=Button(root,padx=42,pady=20,borderwidth=4,text="2", bg="white")
liczba3=Button(root,padx=42,pady=20,borderwidth=4,text="3", bg="white")

liczba1.grid(row=4,column=0)
liczba2.grid(row=4,column=1)
liczba3.grid(row=4,column=2)

liczba4=Button(root,padx=42,pady=20,borderwidth=4,text="4", bg="white")
liczba5=Button(root,padx=42,pady=20,borderwidth=4,text="5", bg="white")
liczba6=Button(root,padx=42,pady=20,borderwidth=4,text="6", bg="white")

liczba4.grid(row=5,column=0)
liczba5.grid(row=5,column=1)
liczba6.grid(row=5,column=2)

liczba7=Button(root,padx=42,pady=20,borderwidth=4,text="7", bg="white")
liczba8=Button(root,padx=42,pady=20,borderwidth=4,text="8", bg="white")
liczba9=Button(root,padx=42,pady=20,borderwidth=4,text="9", bg="white")

liczba7.grid(row=6,column=0)
liczba8.grid(row=6,column=1)
liczba9.grid(row=6,column=2)

liczba0=Button(root,padx=94,pady=20,borderwidth=4,text="0", bg="white")
przecinek=Button(root,padx=43,pady=20,borderwidth=4,text=".", bg="white")

liczba0.grid(row=7,column=0,columnspan=2)
przecinek.grid(row=7,column=2)

'''moduł operacji'''

dzielenie=Button(root,padx=43,pady=20,borderwidth=4,text="/", bg="blue")
mnozenie=Button(root,padx=43,pady=20,borderwidth=4,text="*", bg="blue")
odejmowanie=Button(root,padx=43,pady=20,borderwidth=4,text="-", bg="blue")
dodawanie=Button(root,padx=41,pady=20,borderwidth=4,text="+", bg="blue")

dzialanie=Button(root,padx=42,pady=52,borderwidth=4,text="=", bg="navy blue")

wyczysc=Button(root,padx=31,pady=20,borderwidth=4,text="czyść", bg="turquoise")
usun_znak=Button(root,padx=37,pady=20,borderwidth=4,text='<x]', bg="turquoise")


dodawanie.grid(row=4,column=3)
odejmowanie.grid(row=4,column=4)
mnozenie.grid(row=5,column=3)
dzielenie.grid(row=6,column=3)

dzialanie.grid(row=5,column=4,rowspan=2)

wyczysc.grid(row=7,column=3)
usun_znak.grid(row=7,column=4)


liczba1.bind("<Button-1>",lambda f:wpisz(ekran,1))
liczba2.bind("<Button-1>",lambda f:wpisz(ekran,2))
liczba3.bind("<Button-1>",lambda f:wpisz(ekran,3))
liczba4.bind("<Button-1>",lambda f:wpisz(ekran,4))
liczba5.bind("<Button-1>",lambda f:wpisz(ekran,5))
liczba6.bind("<Button-1>",lambda f:wpisz(ekran,6))
liczba7.bind("<Button-1>",lambda f:wpisz(ekran,7))
liczba8.bind("<Button-1>",lambda f:wpisz(ekran,8))
liczba9.bind("<Button-1>",lambda f:wpisz(ekran,9))
liczba0.bind("<Button-1>",lambda f:wpisz(ekran,0))

dodawanie.bind("<Button-1>",lambda f:wpisz(ekran,'+'))
odejmowanie.bind("<Button-1>",lambda f:wpisz(ekran,'-'))
mnozenie.bind("<Button-1>",lambda f:wpisz(ekran,'*'))
dzielenie.bind("<Button-1>",lambda f:wpisz(ekran,'/'))
przecinek.bind("<Button-1>",lambda f:wpisz(ekran,'.'))
sinus.bind("<Button-1>",lambda f:wpisz(ekran,'sin('))
cosinus.bind("<Button-1>",lambda f:wpisz(ekran,'cos('))
tangens.bind("<Button-1>",lambda f:wpisz(ekran,'tan('))
cotangens.bind("<Button-1>",lambda f:wpisz(ekran,'ctg('))
radius.bind("<Button-1>",lambda f:wpisz(ekran,'rad('))
logarytm_naturalny.bind("<Button-1>",lambda f:wpisz(ekran,'ln('))
logarytm_dziesietny.bind("<Button-1>",lambda f:wpisz(ekran,'log('))
silnia.bind("<Button-1>",lambda f:wpisz(ekran,'!(')) #####################################
pierwiastek.bind("<Button-1>",lambda f:wpisz(ekran,'\/('))
potegowanie.bind("<Button-1>",lambda f:wpisz(ekran,'^')) #################################
liczba_eulera.bind("<Button-1>",lambda f:wpisz(ekran,'e'))
liczba_pi.bind("<Button-1>",lambda f:wpisz(ekran,'pi'))
procent.bind("<Button-1>",lambda f:wpisz(ekran,'%'))
nawias_lewy.bind("<Button-1>",lambda f:wpisz(ekran,'('))
nawias_prawy.bind("<Button-1>",lambda f:wpisz(ekran,')'))

dzialanie.bind("<Button-1>",oblicz)

wyczysc.bind("<Button-1>",czysc)
usun_znak.bind("<Button-1>",usun)


root.mainloop()
import requests
from bs4 import BeautifulSoup
from tkinter import *


def takeSecond(elem):#fokusira se na broj 
    return elem[1]


def odst():#updejtuje lejbl
    global l1
    k=8
    for i in vrednosti:
        l1 = Label(window, text=i[0]+" "+str(i[1]), font=('Helvetica', 12, 'bold'))
        l1.grid(row=k, column=1, rowspan=1)
        k+=2

window = Tk()
window.title("Prodajni kurs Dolara")


url = "https://www.kamatica.com/kursna-lista/valuta-usd#"

rikvest = requests.get(url)

cont = rikvest.content

soup = BeautifulSoup(cont,"lxml")

nedelja_stednje = soup.find("div",{"class":"nedelja-stednje col-sm-8 nopadding"})

imena = nedelja_stednje.find_all("div",{"class":"result"})

imena = imena[6:]#od 6og indeksa krecu banke pre toga su one menjacnice

vrednosti=[]

for ime in imena:
    ime=ime.find_all("li")
    cifra = ime[-3].text
    ime = ime[0].span.text
    lista=list([ime,float(cifra.replace(",","."))])
    vrednosti.append(lista)
        
vrednosti.sort(key=takeSecond, reverse=True)

        

b1 = Button(window, text="Pare", command=odst, width='10', height='3')
b1.grid(row=3, column=2, rowspan=3)


l1 = Label(window, text="Prodajni Kurs $ po Bankama")
l1.grid(row=1, column=1, rowspan= 5)
window.mainloop()

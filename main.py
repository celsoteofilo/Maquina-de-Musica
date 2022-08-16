from tkinter import *
import os
from app.controllers.commands import CommandsMusic
commandos = CommandsMusic()

janela = Tk()
janela.title ('VIdeo Music ')
janela.geometry('500x300')

frame = Frame( janela )


botao = Button(janela, text= 'ESCOLHER')
botao.grid(column= 0, row=10)


botao = Button(janela, text= 'CORRIGIR')
botao.grid(column= 1, row=10)


botao = Button(janela, text= 'TOCAR ')
botao.grid(column= 2, row=10)

botao = Button(janela, text= ' TELA')
botao.grid(column= 3, row=10)

botao = Button(janela, text= 'SAIR')
botao.grid(column=2, row=20)



Texto_play = Label(janela, text= 'PARA TOCAR: ')
Texto_play.grid(column=2, row=0)
Texto_play.grid(padx=2,pady=0)

myList = os.listdir('app/music/')

myListBox = Listbox(frame)

def clickEvent(e):
    w = e.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    commandos.play(value)
    pass

for file in myList:
    myListBox.insert(END, file)

myListBox.bind('<<ListboxSelect>>', clickEvent)


myListBox.grid(  padx = 30, pady = 30  )
frame.grid( padx = 30, pady = 30 )

janela.mainloop()



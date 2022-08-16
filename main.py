from tkinter import *
from app.controllers.commands import CommandsMusic
commandos = CommandsMusic()

janela = Tk()
janela.title ('VIdeo Music ')
janela.geometry('500x300')


botao = Button(janela, text= 'PLAY')
botao.grid(column= 30, row=40)

botao = Button(janela, text= 'STOP')
botao.grid(column= 30, row=80)


botao = Button(janela, text= 'NEXT')
botao.grid(column= 40, row=50)

botao = Button(janela, text= ' COME BACK')
botao.grid(column= 10, row=50)

botao = Button(janela, text= 'SAIR')
botao.grid(column= 30, row=90)



Texto_play = Label(janela, text= 'PARA TOCAR: ' )
Texto_play.grid(column=30, row=0)
Texto_play.grid(padx= 30,pady=0)



janela.mainloop()


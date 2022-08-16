from tkinter import *
from app.controllers.commands import CommandsMusic
commandos = CommandsMusic()

janela = Tk()
janela.title ('VIdeo Music ')
janela.geometry('300x300')


botao = Button(janela, text= 'PLAY', ) # crinado o botao , A funcao comando busca a funcao criada
botao.grid(column= 30, row=40)# aqui apliquei a mesma funcao no grid


Texto_play = Label(janela, text= 'PARA TOCAR: ' )
Texto_play.grid(column=30, row=0)
Texto_play.grid(padx= 30,pady=10)



janela.mainloop()


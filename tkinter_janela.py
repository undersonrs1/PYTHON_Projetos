from tkinter import Tk, Label # chama tkinter, importa Tk para desenvolver janela

root = Tk() # associa objeto a Tk

hello = Label (master = root, text = 'Hello World') # chama funcao Label para escrita dentro da janela, chamando a janela root como parametro que diz em que janela a frase contida em text sesa exibida

hello.pack() #empacotamento de todos os componentes dentro da janela criada

root.mainloop()


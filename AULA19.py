from tkinter import * 

windown = Tk()
windown.geometry('500x200')
windown.title('Isso é uma janela')
label = Label(windown, text=('Olá mundo'))
label.configure(justify='center')
label.pack()
windown.configure(borderwidth='5') 
windown.configure(bg='yellow') 
btn  = Button(text='clique aqui')
btn.pack()
btn.configure(width=10)
btn.configure(border=5)
btn.configure(font='Arial')
btn.place(x = 30, y=50)



windown.mainloop()







# from tkinter import *  # importando a biblioteca

# janela = Tk() # função principal
# janela.geometry('1200x600') #manipulando o tamanho da tel


# janela.mainloop() 

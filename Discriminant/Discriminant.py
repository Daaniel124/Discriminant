from tkinter import *

window = Tk()
window.title('Квадратное уравнение')
window.geometry('600x300')

lbl1 = Label(window, text = 'Решение квадратного уравнения', font = 'Arial 20')
lbl2 = Label(window, text = 'Введите значения:', font = 'Arial 15')
lbl3 = Label(window, text = 'x**2', font = 'Arial 12')
ent1 = Entry(winfow, bg = 'lightblue', width = 5, font = 'Arial 12')

lbl1.pack()
lbl2.pack(side = LEFT)
window.mainloop()
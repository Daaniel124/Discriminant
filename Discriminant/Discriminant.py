from tkinter import *
from math import *

def discriminant(a: int,b: int,c: int):
    """ Решаем уравнение и выводим текст

    :param a int: Число a
    :param b int: Число b
    :param c int: Число c
    """
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = f"Дискриминант равен {D} \n x1 = {round(x1, 2)} \n x2 = {round(x2, 2)}"      
    else:
        text = f" Дискриминант равен {D} \n Уравнение не имеет корней" 
    return text

def textOutput(event):
    ''' Берет данные из ячеек и функции discriminant()
    Выводит текст в lbl7
    '''
    try:
        a = int(ent1.get())
        b = int(ent2.get())
        c = int(ent3.get())
        text = discriminant(a, b, c)
        lbl7.configure(text = text)
    except ValueError:
        text = 'Введены не все данные.'
    lbl7.configure(text = text)


#--------------

#Создаем элементы
window = Tk()
window.title('Квадратное уравнение')
window.geometry('500x300')

frm = Frame(window)
frm2 = Frame(window)

lbl1 = Label(window, text = 'Решение квадратного уравнения', font = 'Arial 15')
lbl2 = Label(window, text = 'Введите значения:', font = 'Arial 12')

lbl3 = Label(frm, text = 'x**2 + ', font = 'Arial 15')
lbl4 = Label(frm, text = 'x + ', font = 'Arial 15')
lbl5 = Label(frm, text = '= 0', font = 'Arial 15')

lbl6 = Label(frm2, text = 'Решение', font = 'Arial 15')
lbl7 = Label(frm2, text = ' ', font = 'Arial 12')

ent1 = Entry(frm, bg = 'lightblue', width = 5, font = 'Arial 15')
ent2 = Entry(frm, bg = 'lightgreen', width = 5, font = 'Arial 15')
ent3 = Entry(frm, bg = 'lightyellow', width = 5, font = 'Arial 15')

btn = Button(window, text = 'Решить', font = 'Arial 15', fg = 'red', bg = 'lightblue', width = 9, height = 2)

#------------------------------

#Собираем интерфейс
btn.bind('<Button-1>', textOutput)
ent1.bind('<Return>')
ent2.bind('<Return>')
ent3.bind('<Return>')

lbl1.pack()
lbl2.pack()

frm.pack(padx = 10, pady = 20)
ent1.pack(side = LEFT)
lbl3.pack(side = LEFT)
ent2.pack(side = LEFT)
lbl4.pack(side = LEFT)
ent3.pack(side = LEFT)
lbl5.pack(side = LEFT)

btn.pack()
frm2.pack(padx = 10, pady = 10)
lbl6.pack()
lbl7.pack()

window.mainloop()
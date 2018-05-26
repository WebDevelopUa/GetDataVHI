# coding=utf-8
# tkinter (toolkit to interface, набор инструментов для интерфейса)
# делаем доступными функции модуля gui после установки модуля в проект
from tkinter import *

# модуля диалоговых окон, который обозначьте кратким псевдонимом box
import tkinter.messagebox as box

# вызов конструктора для создания объекта окна
window = Tk()

# заголовок для этого окна
window.title('Пример графического интерфейса Python')

# инструкция с вызовом конструктора, создающего объект Label
label = Label(window, text='Введите Ваше имя')

# Объект фрейм создается при помощи конструктора Frame()
frame = Frame(window)
entry = Entry(frame)


# функция для отображения данных из поля ввода
def dialog():
    box.showinfo('Приветствие', 'Привет, ' + entry.get())


# кнопка, при нажатии на которую будет вызываться функция
btn = Button(frame, text='+', command=dialog)

# менеджер размещений для добавления метки на окно
label.pack(padx=15, pady=10)

# кнопка и поле ввода на фрейм с параметрами их расположения на фрейме
btn.pack(side=RIGHT, padx=5)
entry.pack(side=LEFT)
frame.pack(padx=150, pady=10)

# обязательная инструкция с циклом обработки событий окна
window.mainloop()

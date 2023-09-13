from tkinter import *


window = Tk()
window.title(' Algorithms in Python - Squares')
window.geometry('600x450+500+60')
window.geometry('600x450+500+60')
paramN, paramLg, parX, parY = 6, 250, 15, 15        # default values

stringN = Label(window, text=' N=')                 # tag 'N='
stringN.grid(column=0, row=1, padx=5, pady=5)
editN = Entry(window, width=6)                      # edit field 'Alpha'
editN.insert(END, '6')                              # insert default value '6'
editN.grid(column=1, row=1)                         # second column, second row

string2 = Label(window, text=' lg=')                # tag 'lg='
string2.grid(column=0, row=2)
editLg = Entry(window, width=6)                     # edit field 'lg'
editLg.insert(END, '240')                           # insert default value '240'
editLg.grid(column=1, row=2, padx=5, pady=5)

string3 = Label(window, text=' x=')                 # tag 'x='
string3.grid(column=3, row=1)
editX = Entry(window, width=6)                      # edit field 'y'
editX.insert(END, '15')                             # insert default value '15'
editX.grid(column=4, row=1, padx=5, pady=5)

string4 = Label(window, text=' y=')                 # tag 'y='
string4.grid(column=3, row=2)
editY = Entry(window, width=6)                      # edit field 'y'
editY.insert(END, '15')                             # insert default value '15'
editY.grid(column=4, row=2, padx=5, pady=5)
canv = Canvas(bg='white', width=300, height=300)    # painting field (canvas)


def clicked_clear():
    editN.delete(0, END)                            # clear content of editAlpha field
    editLg.delete(0, END)                           # clear content of editLg field
    editX.delete(0, END)                            # clear content of editX field
    editY.delete(0, END)                            # clear content of editY field
    canv.delete('all')                              # clear painting field


clear_button = Button(window, text=' Clear ', command=clicked_clear)
clear_button.grid(column=1, row=0, padx=5, pady=5)


def paint_suqares(paramN, paramLg, x, y):
    if paramN > 0:
        canv.create_line(x, y, x + paramLg, y)
        canv.create_line(x + paramLg, y, x + paramLg, y + paramLg)
        canv.create_line(x + paramLg, y + paramLg, x, y + paramLg)
        canv.create_line(x, y + paramLg, x, y + paramLg / 2)
        canv.create_line(x, y + paramLg / 2, x + paramLg / 2, y + paramLg)
        canv.create_line(x + paramLg / 2, y + paramLg, x + paramLg, y + paramLg / 2)
        canv.create_line(x + paramLg, y + paramLg / 2, x + paramLg / 2, y)
        canv.create_line(x + paramLg / 2, y, x + paramLg / 4, y + paramLg / 4)
        paint_suqares(paramN - 1, paramLg / 2, x + paramLg / 4, y + paramLg / 4)
        canv.create_line(x + paramLg / 4, y + paramLg / 4, x, y + paramLg / 2)
        canv.create_line(x, y + paramLg / 2, x, y)

    canv.grid(column=5, row=3, padx=1, pady=1)


def draw_click():
    canv.delete('all')                                  # clear painting field
    paramN = int(editN.get())                           # read N values
    paramLg = int(editLg.get())                         # read Lg values
    parX = int(editX.get())                             # read x values
    parY = int(editY.get())                             # read y values

    print(paramLg, paramN, parX, parY)
    paint_suqares(paramN, paramLg, parX, parY)


draw_button = Button(window, text=' Draw ', command=draw_click) # draw button
draw_button.grid(column=0, row=0)
window.mainloop()

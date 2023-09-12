from tkinter import *

window = Tk()
window.title('Recurrent spiral')
window.geometry('550x400+500+60')

#default values
paramAlpha = 20
paramLg = 180

stringAlpha = Label(window, text=' alpha=')       # tag 'alpha='
stringAlpha.grid(column=0, row=1, padx=5, pady=5) # cell side gap
editAlpha = Entry(window, width=6)                # 'Alpha' edit field
editAlpha.insert(END, '20')                       # insert default value '20' into our field
editAlpha.grid(column=1, row=1)                   # 2nd column, 2nd row

string2 = Label(window,text=' lg=')               # 'lg=' tag
string2.grid(column=0, row=2)
editLg = Entry(window, width=6)                   # edit field 'lg'
editLg.insert(END, '180')                         # set default value '180'
editLg.grid(column=1, row=2, padx=5, pady=5)

canv = Canvas(bg='white', width=300, height=300)  # painting field(canvas)

def clicked_clear():
    editAlpha.delete(0, END)                      # clear content of editAlpha field
    editLg.delete(0, END)                         # clear content of editLg field
    canv.delete('all')                            # clear painting field

button_clear = Button(window, text=' Clear ', command=clicked_clear)
button_clear.grid(column=1, row=0, padx=5, pady=5)

def draw_spiral(paramAlpha, paramLg, x, y):
    if paramLg > 0 and paramLg > paramAlpha:
        canv.create_line(x, y, x + paramLg, y)
        canv.create_line(x + paramLg, y, x + paramLg, y + paramLg)
        canv.create_line(x + paramLg, y + paramLg, x + paramAlpha, y + paramLg)
        canv.create_line(x + paramAlpha, y + paramLg, x + paramAlpha, y + paramAlpha)
        draw_spiral(paramAlpha, paramLg - 2*paramAlpha, x + paramAlpha, y + paramAlpha)

    canv.grid(column=2, row=2, padx=1, pady=1)

def clicked_draw():
    canv.delete('all')                            # clear painting field
    paramAlpha = int(editAlpha.get())             # read alpha value
    paramLg = int(editLg.get())                   # read Lg value

    print(paramLg, paramAlpha)

    draw_spiral(paramAlpha, paramLg, 5, 5)        # call algorithm

button_draw = Button(window, text=' Draw ', command=clicked_draw)
button_draw.grid(column=0, row=0)
window.mainloop()                                 # after closing window pass it

from textblob import TextBlob

from tkinter import *

def Auto_correct():
    corrected_words = []
    text = Input_text.get(1.0, END).split(" ")
    for i in text:
        corrected_words.append(TextBlob(i).correct())
    Output_text.delete(1.0, END)
    for i in corrected_words:
        Output_text.insert(END, i + " ")


def Clear():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)


mainwin = Tk()
mainwin.geometry('1400x520')
mainwin.resizable(False, False)

mainwin.title("Auto Correct")
mainwin.config(bg='#82CEC7')

Label(mainwin, text="Enter Text", font='arial 18 bold', bg= '#82CEC7').place(x=250, y=90)

Input_text = Text(mainwin, font='arial 13', bg='white', height=11, wrap=WORD, padx=5, pady=5, width=50, insertbackground='black')

Inpu…
[11:12 am, 06/07/2023] AYUSH SHARMA: from textblob import TextBlob

from tkinter import *

def Auto_correct():
    corrected_words = []
    text = Input_text.get(1.0, END).split(" ")
    for i in text:
        corrected_words.append(TextBlob(i).correct())
    Output_text.delete(1.0, END)
    for i in corrected_words:
        Output_text.insert(END, i + " ")


def Clear():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)


mainwin = Tk()
mainwin.geometry('1400x520')
mainwin.resizable(False, False)

mainwin.title("Auto Correct")
mainwin.config(bg='#E6E6FA')

Label(mainwin, text="Enter Text", font='arial 18 bold', bg= '#E6E6FA').place(x=250, y=90)

Input_text = Text(mainwin, font='arial 13', bg='white', height=11, wrap=WORD, padx=5, pady=5, width=50, insertbackground='black')

Input_text.place(x=30, y=130)

Label(mainwin, text="Output", font='arial 18 bold', bg= '#E6E6FA').place(x=1010, y=90)

Output_text = Text(mainwin, font='arial 13', bg='white', height=11, wrap=WORD, padx=5, pady=5, width=50, insertbackground='black')

Output_text.place(x=750, y=130)

auto_correct_btn = Button(mainwin, text="Correct", bg='#E6E6FA', width=40, font='arial 18 bold', pady=3, command=Auto_correct)

auto_correct_btn.place(x=320, y=440)

c1 = Button(mainwin, text="Clear", width=10, pady=3, bg='#E6E6FA', font='arial 18 bold', command=Clear)

c1.place(x=1170, y=440)

mainwin.mainloop()

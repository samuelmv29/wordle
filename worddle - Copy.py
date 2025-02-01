from tkinter import *
from pydictionary import Dictionary
import tkinter.font as font
import time



root = Tk()
root.geometry("520x670")
root.resizable(0,0)


#fonts
font_main = font.Font(family = "Ariel", size = 30, weight = "bold")
font_entry = font.Font(family = "Ariel", size = 15, weight = "bold")
font_title = font.Font(family = "Cooper Black", size = 60, weight = "bold")
font_game = font.Font(family = "Comic Sans MS", size = 60, weight = "bold")
font_game_2 = font.Font(family = "Comic Sans MS", size = 40, weight = "bold")
font_game_8 = font.Font(family = "Comic Sans MS", size = 17, weight = "bold")
font_game_3 = font.Font(family = "Ariel", size = 30, weight = "bold")
font_game_4 = font.Font(family = "Ariel", size = 20, weight = "bold")
font_game_5 = font.Font(family = "Ariel", size = 13, weight = "bold")
font_game_6 = font.Font(family = "Ariel", size = 18, weight = "bold")

frame1 = Frame(root, bg = "gray12")
frame1.pack(fill = "both", expand = True)

#title
label_title = Label(frame1, text = "Samwle", font = font_title, fg = "white", bg = "gray12")
label_title.place(x = 95, y = 10)

#state
initial_key = 0
row_count = 0
#rows
a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d1,d2,d3,d4,d5,e1,e2,e3,e4,e5,f1,f2,f3,f4,f5 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

row1 =[a1,a2,a3,a4,a5]
row2 = [b1,b2,b3,b4,b5]
row3=[c1,c2,c3,c4,c5]
row4=[d1,d2,d3,d4,d5]
row5=[e1,e2,e3,e4,e5]
row6 = [f1,f2,f3,f4,f5]

rows = [row1,row2,row3,row4,row5,row6]
entered_row = 0
word = "hello"

def enter_key(key):
    global initial_key, row_count
    print(entered_row)
    if entered_row == 6:
        pass
    else:
        if row_count !=6:
            if initial_key == 5:
                pass
            else:
                ((rows[row_count])[initial_key]) = key
                ((boxes[row_count*5+initial_key])["text"]) = key
                initial_key+=1



def backspace_function(key):
    global initial_key
    initial_key-=1
    if entered_row == 6:
        pass
    else:
        if initial_key == -1:
            initial_key = 0
        ((boxes[row_count*5+initial_key])["text"]) = ""
        ((rows[row_count])[initial_key]) = ""
     
def enter_function(key):
    global row_count, initial_key,entered_row, i
    entered_word = ""
    if initial_key ==5:
        for num2 in range(0,5):
            letter = ((boxes[row_count*5+num2])["text"])
            entered_word+=letter
        dictionary = Dictionary(entered_word)
        dictionary_result=dictionary.meanings()
        if dictionary_result[:1]== "No":
            label_correct = Label(frame1, text = "Word doesn't exist", font = font_game_4, borderwidth = 6, relief = "raised", width = 24)
            label_correct.place(x = 40, y = 590)
            label_correct.after(3000,label_correct.destroy)
        else:
            for num in range(0,5):
                if entered_word[num] in word:

                    if entered_word[num] == word[num]:
                        (boxes[(row_count*5)+num])["bg"] = "green"
                        (eval(entered_word[num]))["bg"] = "green"
                    else:
                        (boxes[(row_count*5)+num])["bg"] = "light green"
                        (eval(entered_word[num]))["bg"] = "light green"
                else:
                    (boxes[(row_count*5)+num])["bg"] = "gray24"
                    (eval(entered_word[num]))["bg"] = "gray24"
            initial_key = 0
            row_count +=1
            entered_row+=1
            if row_count == 7:
                row_count = 6
                entered_row = 6

            if entered_word == word:
                entered_row = 6
                label_correct = Label(frame1, text = "Correct!", font = font_game_3, borderwidth = 10, relief = "raised", width = 12)
                label_correct.place(x = 100, y = 590)


ys = 120
boxes = []
for row in rows:
    xs = 140
    for box in row:
        entry_box = Label(frame1,text = box, font = font_game_4, width = 2, relief = "sunken",borderwidth = 4, bg = "gray12", fg = "white")
        entry_box.place(x = xs, y = ys)
        boxes.append(entry_box)
        xs+=50
    ys+=50
  
a = Button(frame1,text = "a", command = lambda: enter_key("a"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("a",lambda event: enter_key("a"))

b = Button(frame1,text = "b", command = lambda: enter_key("b"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("b",lambda event: enter_key("b"))

c = Button(frame1,text = "c", command = lambda: enter_key("c"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("c",lambda event: enter_key("c"))

d = Button(frame1,text = "d", command = lambda: enter_key("d"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("d",lambda event: enter_key("d"))

e = Button(frame1,text = "e", command = lambda: enter_key("e"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("e",lambda event: enter_key("e"))

f = Button(frame1,text = "f", command = lambda: enter_key("f"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("f",lambda event: enter_key("f"))

g = Button(frame1,text = "g", command = lambda: enter_key("g"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("g",lambda event: enter_key("g"))

h = Button(frame1,text = "h", command = lambda: enter_key("h"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("h",lambda event: enter_key("h"))

i = Button(frame1,text = "i", command = lambda: enter_key("i"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("i",lambda event: enter_key("i"))


j = Button(frame1,text = "j", command = lambda: enter_key("j"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("j",lambda event: enter_key("j"))

k = Button(frame1,text = "k", command = lambda: enter_key("k"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("k",lambda event: enter_key("k"))

l = Button(frame1,text = "l", command = lambda: enter_key("l"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("l",lambda event: enter_key("l"))

m = Button(frame1,text = "m", command = lambda: enter_key("m"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("m",lambda event: enter_key("m"))

n = Button(frame1,text = "n", command = lambda: enter_key("n"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("n",lambda event: enter_key("n"))

o = Button(frame1,text = "o", command = lambda: enter_key("o"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("o",lambda event: enter_key("o"))

p = Button(frame1,text = "p", command = lambda: enter_key("p"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("p",lambda event: enter_key("p"))

q = Button(frame1,text = "q", command = lambda: enter_key("q"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("q",lambda event: enter_key("q"))

r = Button(frame1,text = "r", command = lambda: enter_key("r"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("r",lambda event: enter_key("r"))

s = Button(frame1,text = "s", command = lambda: enter_key("s"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("s",lambda event: enter_key("s"))

t = Button(frame1,text = "t", command = lambda: enter_key("t"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("t",lambda event: enter_key("t"))

u = Button(frame1,text = "u", command = lambda: enter_key("u"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("u",lambda event: enter_key("u"))

v = Button(frame1,text = "v", command = lambda: enter_key("v"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("v",lambda event: enter_key("v"))

w = Button(frame1,text = "w", command = lambda: enter_key("w"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("w",lambda event: enter_key("w"))

x = Button(frame1,text = "x", command = lambda: enter_key("x"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("x",lambda event: enter_key("x"))

y = Button(frame1,text = "y", command = lambda: enter_key("y"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("y",lambda event: enter_key("y"))

z = Button(frame1,text = "z", command = lambda: enter_key("z"), font = font_entry, width = 2, bg = "gray59", fg = "white")
root.bind("z",lambda event: enter_key("z"))

backspace = Button(frame1,text = "←", command = lambda: backspace_function("←"), font = font_entry, width = 4, bg = "gray59", fg = "white")
root.bind("<BackSpace>",lambda event: backspace_function("←"))

enter = Button(frame1,text = "↵", command = lambda: enter_function("↵"), font = font_entry, width = 4, bg = "gray59", fg = "white")
root.bind("<Return>",lambda event: enter_function("↵"))

row_letter_1 = [q,w,e,r,t,y,u,i,o,p]
row_letter_2 = [a,s,d,f,g,h,j,k,l]
row_letter_3=[z,x,c,v,b,n,m,enter]
xl = 80
yl = 450
for num5 in row_letter_1:
    num5.place(x = xl, y = yl)
    xl += 35
yl = 492
xl = 99
for num6 in row_letter_2:
    num6.place(x = xl, y = yl)
    xl += 35

yl = 534
xl = 130
for num7 in row_letter_3:
    num7.place(x = xl, y = yl)
    xl += 35

backspace.place(x = 71,y = 534)

root.mainloop()









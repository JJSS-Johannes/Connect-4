from tkinter import *
import functools
import os

master = Tk()
master.geometry('280x270')
master.resizable(width = 0, height = 0)
master.title("4 Gewinnt")
fields = []
buttons = []
for i in range(0,6):
    for j in range(0,7):
        b = Button(master, text="", border=1, state="disabled", bg="white")
        b.place(x=40*j, y=40*i+30, width=40, height = 40)
        fields.append(b)


for i in range(0,7):
    l = Button(master, text=i+1, bg="yellow")
    l.place(x=40*i, y=0, width = 40, height = 30)
    buttons.append(l)

fwheight = [0,0,0,0,0,0,0]
cc = "yellow"
def set_col(num):
    global cc
    field_to_change = (42 - (fwheight[num]*7)) - (7-num)
    fields[field_to_change].config(bg=cc)
    if cc == "yellow":
        cc = "red"
        for i in range(len(buttons)):
            buttons[i].config(bg="red")
    else:
        cc = "yellow"
        for i in range(len(buttons)):
            buttons[i].config(bg="yellow")
    fwheight[num] += 1
    for i in range(len(fwheight)):
        if fwheight[i] >= 6:
            buttons[i].config(state="disabled")
    check()

def check():
    bg = []
    gelb = ['yellow', 'yellow', 'yellow', 'yellow']
    rot = ['red', 'red', 'red', 'red']
    testi = [0,7,14,21]
    testl = [3,9,15,21]
    testj = [0,8,16,24]
    for i in range(len(fields)):
        bg.append(fields[i].cget('bg'))
    for i in range(0,4):
        if bg[0+i:4+i] == gelb or bg[0+i:4+i] == rot:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    for i in range(0,4):
        if bg[7+i:11+i] == gelb or bg[7+i:11+i] == rot:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    for i in range(0,4):
        if bg[14+i:18+i] == gelb or bg[14+i:18+i] == rot:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    for i in range(0,4):
        if bg[21+i:25+i] == gelb or bg[21+i:25+i] == rot:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    for i in range(0,4):
        if bg[28+i:32+i] == gelb or bg[28+i:32+i] == rot:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    for i in range(0,4):
        if bg[35+i:39+i] == gelb or bg[35+i:39+i] == rot:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    test = []
    for l in range(0,3):
        for k in range(0,7):
            pp = []
            for i in range(0,4):
                pp.append(bg[testi[i]+k])
            test.append(pp)
            if test[k+(l*7)] == rot or test[k+(l*7)] == gelb:
                for j in range(0,7):
                    buttons[j].config(state="disabled")
        for m in range(len(testi)):
            testi[m] += 7
    test2 = []
    for n in range(0,3):
        for k in range(0,4):
            pp = []
            for i in range(0,4):
                pp.append(bg[testl[i]+k])
            test2.append(pp)
        for m in range(len(testl)):
            testl[m] += 7
    for p in range(len(test2)):
        if test2[p] == rot or test2[p] == gelb:
            for j in range(0,7):
                buttons[j].config(state="disabled")
    test3 = []
    for n in range(0,3):
        for k in range(0,4):
            pp = []
            for i in range(0,4):
                pp.append(bg[testj[i]+k])
            test3.append(pp)
        for m in range(len(testj)):
            testj[m] += 7
    for p in range(len(test3)):
        if test3[p] == rot or test3[p] == gelb:
            for j in range(0,7):
                buttons[j].config(state="disabled")
for i in range(0,7):
    buttons[i].config(command = functools.partial(set_col, i))
def on_destroy():
    master.destroy()
    os._exit(0)
master.protocol("WM_DELETE_WINDOW", on_destroy)
master.mainloop()   

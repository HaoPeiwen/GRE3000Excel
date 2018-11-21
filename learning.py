import csv, re, sys
from tkinter import *
from tkinter import messagebox
from subprocess import run
import os

class words:
    def __init__(self):
        self.words = []
        self.ptr = -1
        self.maxword = 199
        self.forget = []
        self.interface = 1 # 0 for word, 1 for meaning

wordlis = words()
wordproperty = re.compile(r'[a-z]+\.')


def remember():
    if wordlis.interface == 0:
        refresh_mean()
        wordlis.interface = 1
    else:
        wordlis.interface = 0
        if wordlis.ptr in wordlis.forget:
            wordlis.forget.remove(wordlis.ptr)
        nextword()


def forget():
    if wordlis.interface == 0:
        refresh_mean()
        wordlis.interface = 1
    else:
        wordlis.interface = 0
        if wordlis.ptr not in wordlis.forget and wordlis.ptr <200 and wordlis.ptr >=0:
            wordlis.forget.append(wordlis.ptr)
            print(wordlis.words[wordlis.ptr])
        nextword()

def search():
    word = wordlis.words[wordlis.ptr][0]
    run('wd '+word, shell=True)


def nextword():
    wordlis.ptr += 1
    refresh_word()


def Previous():
    wordlis.ptr -= 1
    refresh_word()

def refresh_word():
    #try:
    word = wordlis.words[wordlis.ptr][0]
    text_word.set(word)
    for i in text_mean:
        i.set('')
    #except:
    #    print(wordlis.ptr)
        #save()

def refresh_mean():
    try:
        meaning = wordlis.words[wordlis.ptr][1].replace(' ', '').replace('&amp;', '&').replace('amp', '')
        m = wordproperty.findall(meaning)
        m = list(set(m))  # unduplicated
        for i in m:
            meaning = meaning.replace(i, ' '+i)
        m = meaning[1:].split(' ')
        for i in range(len(m)):
            try:
                text_mean[i].set(m[i])
            except:
                text_mean.append(StringVar())
                text_mean[i].set(m[i])
                Label(window, textvariable=text_mean[i], font=(
                    "Times New Roman", 20), compound='center').pack()
    except:
        pass

def save():
    with open('/review/'+csvname+ '_recall.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i in wordlis.forget:
            writer.writerow(wordlis.words[i])
    messagebox.showinfo("Completed", "Saved as list1_recall.csv")


window = Tk()
window.title('GRE Rekill You 3000')
window.geometry('700x400')

text_word = StringVar()
text_word.set('abandon')
text_mean = []
text_mean.append(StringVar())
text_mean[0].set('v./n.放纵')
text_mean.append(StringVar())
text_mean[1].set('v.放弃')


Label(window, text=' ', font=(
    "Times New Roman", 25), compound='center').pack()
Label(window, textvariable=text_word, font=(
    "Times New Roman", 25), compound='center').pack()
Label(window, textvariable=text_mean[0], font=(
    "Times New Roman", 18), compound='center').pack()
Label(window, textvariable=text_mean[1], font=(
    "Times New Roman", 18), compound='center').pack()
    
btn_pre = Button(window, text='Previous', font=("Courier New", 14), command=Previous)
btn_pre.place(x=120, y=320)
btn_forg = Button(window, text='Forget', font=(
    "Courier New", 14), command=forget)
btn_forg.place(x=300, y=320)
btn_rem = Button(window, text='Remember',
                    font=("Courier New", 14), command=remember)
btn_rem.place(x=450, y=320)

btn_ser = Button(window, text='Search',
                    font=("Courier New", 14), command=remember)
btn_ser.place(x=300, y=280)

# btn_pre.bind_all('<KeyPress-Down>', Previous) 
# btn_forg.bind_all('<KeyPress-Left>', forget) 
# btn_rem.bind_all('<KeyPress-Right>', remember) 

def eventhandler(event):
    if event.keysym == 'Left':
        Previous()
    elif event.keysym == 'Right':
        remember()
    elif event.keysym == 'Down':
        forget()
    elif event.keysym == 'Up':
        search()

btn = Button(window)
btn_forg.bind_all('<KeyPress>', eventhandler)






if __name__ == "__main__":
    csvname = './wordcsv/再要你命3000---' + sys.argv[1]
    with open(csvname + '.csv', 'r', encoding='gbk') as f:
        reader = csv.reader(f)
        for row in reader:
            wordlis.words.append(row[1:])
    window.mainloop()

#Project 4.

""" Text to speach Mini Project """

from tkinter import *
from gtts import gTTS
import os

scr = Tk()
scr.geometry("510x300")
scr.config(bg="blue")
scr.title("Text to Speach")


def text_speach():
    
    language="en"

#Passing the text and language to be engine
#here we mark slow=False which tells  to module
#that converted audioshould be high speed
    t=e.get()
    myobj=gTTS(text=t,lang=language,slow=False)

#Saving the converted audio in amp3 file named
#welcome
    myobj.save("E://welcome.mp3")

#Playing the converted file
    os.system("E://welcome.mp3")

Label = Label(scr,text="Wright Something",font=("Time New Roman",25,"bold"),
                   bg="blue",fg="white")
Label.place(x=100,y=20,height=50,width=300)

e = Entry(scr,font=("Time New Roman",20,"bold"))
e.place(x=50,y=80,height=50,width=400)


button = Button(scr,text="Speak",font=("Time New Roman",20,"bold"),
                    bg="yellow",command=text_speach)
button.place(x=150,y=180,height=50,width=200)

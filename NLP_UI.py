

import tkinter
from tkinter import *
##from NLPCodeFinal.py import get_tweets(user, query)
import NLPCodeFinal as fl

gui = tkinter.Tk()
global var2

E1 = Entry(gui)
sentence = ''
def generate():
    subject = E1.get()
    global sentence
    sentence = fl.final_tweet(var2.get(), subject)
    text.delete('1.0', END)
    text.insert(INSERT, sentence)

def tweet():
    subject = E1.get();
    fl.tweet_generated(sentence[:280])

gen_tweet = tkinter.Button(gui, text ="Generate Tweet", command = generate)
tweet = tkinter.Button(gui, text = "Tweet", command = tweet)

text = tkinter.Text(gui)

L1 = tkinter.Label(gui, text="User: ")

var2 = IntVar()


def user_or():
    print('fuck')

R_User = Radiobutton(gui, text="User", variable=var2, value=0, command=user_or)
R_Hashtag = Radiobutton(gui, text="Hashtag", variable=var2, value=1, command=user_or)



## pack UI widgets
E1.pack(side = RIGHT)
L1.pack(side = RIGHT)
R_User.pack(anchor = E)
R_Hashtag.pack(anchor = E)
text.pack()
gen_tweet.pack()
tweet.pack()

gui.mainloop()

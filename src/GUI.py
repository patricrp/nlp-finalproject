from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import funconstructor as fc

class Classifier():

    def __init__(self ):
        self.window = Tk()
        self.window.title('Content Classifier')
        self.canvas=Canvas(self.window, height=600, width=1200)
        self.canvas.pack()


        #Image
        self.image=PIL.Image.open('images/robotic.jpg')
        self.background_img=ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.window, image=self.background_img)
        self.background_label.place(relx=0.5, rely=0.35, relwidth=1, relheight=1)

        #Title
        self.label1 = Label(self.window, text = 'Content Classifier', fg = 'black')
        self.label1.place(relx=0.5, rely=0.3,relwidth=0.75, relheight=0.09,anchor='n')
        self.label1.config(font=('Roboto', 60))

        #Buttom
        self.frame1 = Frame(self.window, bg='black', bd=1)
        self.frame1.place(relx=0.3, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')

        self.button1 = Button(self.frame1, text='Select a csv of publications', font=('Roboto', 12))
        self.button1.place(relx=0, relheight=1, relwidth=1)
        self.button1.configure(activebackground='black', foreground='black', bg='black', relief='sunken', command=callback1) #path1

        self.frame2 = Frame(self.window, bg='black', bd=1)
        self.frame2.place(relx=0.7, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')

        self.button2 = Button(self.frame2, text='Select a csv of categories', font=('Roboto', 12))
        self.button2.place(relx=0, relheight=1, relwidth=1)
        self.button2.configure(activebackground='black', foreground='black', bg='black', relief='sunken', command=callback2) #path2

        self.frame3 = Frame(self.window, bg='black', bd=1)
        self.frame3.place(relx=0.5, rely=0.85, relwidth=0.125, relheight=0.05, anchor='n')

        self.button3 = Button(self.frame3, text='Analyze it!', font=('Roboto', 12))
        self.button3.place(relx=0, relheight=1, relwidth=1)
        self.button3.configure(activebackground='black', foreground='black', bg='black', relief='raised', command=classify)



paths = []

def callback1():
    name1= fd.askopenfilename() 
    return paths.append(name1)

def callback2():
    name2= fd.askopenfilename() 
    return paths.append(name2)


def classify():
    mb.showinfo('Getting ready','Be patient while the model is training. You will find the classified csv and the report on the output folder')
    return fc.dataReady(paths[0], paths[1])

c = Classifier()
c.window.mainloop()

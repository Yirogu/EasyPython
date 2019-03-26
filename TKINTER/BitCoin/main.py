import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
class SeaofBTCapp(tk.Tk) :

    def __init__ (self,*args,**kwargs) :

        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.title(self,"BitCoin")
        container = tk.Frame(self)
        img = tk.PhotoImage(file='icon.gif')
        # tk.Tk.wm_iconbitmap(self,'@icon.gif')
        self.tk.call('wm','iconphoto',self._w,img)


        container.pack(side='top',fill='both', expand = True )

        container.grid_rowconfigure(0,weight =1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        for F in (StartPage,PageOne,PageTwo) :

            frame  = F(container,self)

            self.frames[F] = frame

            frame.grid(row = 0 ,column = 0, sticky = "nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame =self.frames[cont]
        frame.tkraise()

def qf (param):
    print(param)

class StartPage(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Start Page",font =LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text = "Visit page1",
        command = lambda :controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self,text = "Visit page 2",
        command = lambda :controller.show_frame(PageTwo))
        button2.pack()
        #
        # button3 = tk.Button(self,text = "Visit page1",
        # command = lambda :controller.show_frame(PageOne))
        # button3.pack()

class PageOne(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page One :)",font =LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text = "Back to Home",
        command = lambda :controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self,text = "PageTwo",
        command = lambda :controller.show_frame(PageTwo))
        button2.pack()
        # tk.frame()
class PageTwo(tk.Frame) :
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Page Two :)",font =LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text = "PageOne",
        command = lambda :controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self,text = "Back to Home",
        command = lambda :controller.show_frame(StartPage))
        button2.pack()






app =SeaofBTCapp()
app.mainloop()

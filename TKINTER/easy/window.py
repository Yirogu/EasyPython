from tkinter import*
from PIL import Image,ImageTk
class Window(Frame) :

    def __init__(self,master = None) :
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Gui")
        self.pack(fill=BOTH,expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = 'Save')
        file.add_command(label = 'Exit',command = self.client_exit)
        menu.add_cascade(label = 'File',menu = file)

        edit = Menu(menu)
        edit.add_command(label='Show Image',command=self.showImg)
        edit.add_command(label='Show Text',command=self.showTxt)
        menu.add_cascade(label = 'Edit', menu = edit)


    def client_exit (self):
        exit()


    def showImg(self) :
        load =Image.open('Images/pick.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self,image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self,text = "hey there good looking")
        text.pack()



root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()

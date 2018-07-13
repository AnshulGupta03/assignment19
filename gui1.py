#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
from tkinter import *

root = Tk()
root.title('user friendly')
root.configure(background = 'red')

newL = Label(root,text = 'Hello world.',bg = 'YELLOW')
newL.pack()

newB = Button(root,text = 'Exit',command=root.destroy)
newB.pack()

root.mainloop()


#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.

from tkinter import *

def action():
    print("action performed")

root = Tk()
root.title('user friendly')
root.configure(background = 'red')

newL = Label(root,text = 'Hello baby.',bg = 'YELLOW')
newL.pack()

newB = Button(root,text = 'Exit',command=action)
newB.pack()

root.mainloop()


#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

from tkinter import *
def func():
    mylabelL.configure(text = 'Learn to stay happy')

root = Tk()
root.configure(background= 'pink')

myframeF = Frame(root,height = 100,width= 500,bg = 'green')
myframeF.pack(fill=X)

mylabelL = Label(myframeF,text = "What to do?",bg = 'yellow')
mylabelL.pack()

button1B= Button(myframeF,bg = 'purple',text = 'exit',command= root.destroy)
button1B.pack()
button2B = Button(myframeF,bg = 'orange',text = 'change text',command=func)
button2B.pack()


root.mainloop()



# Q4.Write a python program using tkinter interface to take an input in the GUI program and print it.
from tkinter import *

root  = Tk()

def func():
    print("name=%s"%(e1.get()))
    print("age=%s"%(e2.get()))

l1 = Label(root,text = 'name').grid(row = 0,column = 0)
l2 = Label(root,text = 'age').grid(row = 1,column = 0)

e1= Entry(root)
e1.grid(row = 0,column = 1)

e2 = Entry(root)
e2.grid(row = 1,column = 1)


b1 = Button(root,text = 'submit',command = func)
b1.grid(row = 2,column = 1)

root.mainloop()





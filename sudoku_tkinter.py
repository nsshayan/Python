from Tkinter import *

game = Tk()
game.title("Sudoku")
#game.resizable(1000,1000)
'''L1 = Label(top,text="User name")
L1.pack(side=LEFT)
E1 = Entry(top, bd =5)
E1.pack(side=RIGHT)'''
topFrame = Frame(game)
topFrame.pack()
bottomFrame = Frame(game)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg="red")
button2 = Button(topFrame, text = "Button 2", fg="blue")
button3 = Button(topFrame, text = "Button 3", fg="green")
button4 = Button(bottomFrame, text = "Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side = LEFT)
button4.pack(side=BOTTOM)

# Code to add widgets will go here...
game.mainloop()
    


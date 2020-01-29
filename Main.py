from Grabber import execute
from tkinter import *

class Application(Frame):
    gen = IntVar
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def sel(self):
        print("clicked")
        self.gen = self.gen.get

    def submitValues(self):
        print(self.gen)

    def create_widgets(self):
        self.lblTitle = Label(self, text="Pokemon Party Optimizer", background = "white", font=("Impact", 28))
        self.lblTitle.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")

        ## Radio Buttons for Gen Selection
        self.optionAll = Radiobutton(self, text = "All Generations", background = "white", font = ("Impact"), variable=self.gen, value = 0, command=self.sel)
        self.optionAll.grid(row = 1, column = 0, columnspan = 1, sticky = "nsew")

        self.option1 = Radiobutton(self, text = "Gen 1", background = "white", font = ("Impact"), variable=self.gen, value = 1, command=self.sel)
        self.option1.grid(row = 1, column = 1, columnspan = 1, sticky = "nsew")

        self.option2 = Radiobutton(self, text = "Gen 2", background = "white", font = ("Impact"), variable=self.gen, value = 2, command=self.sel)
        self.option2.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew")

        self.option3 = Radiobutton(self, text = "Gen 3", background = "white", font = ("Impact"), variable=self.gen, value = 3, command=self.sel)
        self.option3.grid(row = 2, column = 1, columnspan = 1, sticky = "nsew")

        self.optionAll = Radiobutton(self, text = "Gen 4", background = "white", font = ("Impact"), variable=self.gen, value = 4, command=self.sel)
        self.optionAll.grid(row = 3, column = 0, columnspan = 1, sticky = "nsew")

        self.optionAll = Radiobutton(self, text = "Gen 5", background = "white", font = ("Impact"), variable=self.gen, value = 5, command=self.sel)
        self.optionAll.grid(row = 3, column = 1, columnspan = 1, sticky = "nsew")

        self.optionAll = Radiobutton(self, text = "Gen 6", background = "white", font = ("Impact"), variable=self.gen, value = 6, command=self.sel)
        self.optionAll.grid(row = 4, column = 0, columnspan = 1, sticky = "nsew")

        self.optionAll = Radiobutton(self, text = "Gen 7", background = "white", font = ("Impact"), variable=self.gen, value = 7, command=self.sel)
        self.optionAll.grid(row = 4, column = 1, columnspan = 1, sticky = "nsew")

        self.submit = Button(self, text="Submit", background="black", foreground="white", font = "Impact", command = self.submitValues)
        self.submit.grid(row = 5, column = 0, columnspan = 4, sticky = "nsew")



##id = int(input("Please enter 0 for Speed, 1 for special-defense, 2 for special-attack, 3 for defense, 4 for attack, 5 for hp: "))
##gen = int(input("Please enter which gen of pokemon you would like to see or 0 for all gens: "))

root = Tk()
root.title("Pokemon Party Optimizer")
root.geometry("1200x800")
root.resizable(width = TRUE, height = TRUE)
root.configure(background = "white")

app = Application(root)
root.mainloop()
from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.geometry("900x600")
root.title("Classes")

gui = ["label","button","dropdown"]

dropdown = ttk.Combobox(root, state="readonly", values = gui)
dropdown.pack()

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
    
    def createLabel(self):
        label = Label(root,text ="A new label has been created using class", fg="red")
        label.pack()
    
    def createButton(self):
        btn = Button(root, fg="red", command = self.messagebox(), text = "press here")
        btn.pack()
    
    def createDropdown(self):
        combo = [1,2,3]
        dropdown1 = ttk.Combobox(root,state="readonly", fg="red", values = combo)
        dropdown1.pack()
    
    def choose(self):
        global dropdown
        element = dropdown.get()
        if(element =="label"):
            self.createLabel()
        elif(element == "button"):
            self.createButton()
        elif(element == "dropdown"):
            self.createDropdown()
    
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")

obj_of_CreateElements = CreateElements()

btn = Button(root, text="Click to create label and button element", command = obj_of_CreateElements)
btn.pack(padx=20,pady=10)

root.mainloop()
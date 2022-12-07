from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])

    if file== "":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file== None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])

        if file== "":
            file = None
        else:
            # Save as a new File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            # Renaming as filename
            root.title(os.path.basename(file) + " - Notepad")

    else:
#        Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()




def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("About Us", "This Notepad is Designed by Karan Singh 20CS33,B.tech 3rd Year Student ,in 2022.\nCopyRight@2022 : KaranSingh\nAll Rights Reserved")


if __name__ == '__main__':
    root=Tk()
    root.geometry("500x500")
    root.title("Untitled-Notepad")

    # changing icon but not responsding
    icon0=Image.open("1.ico")
    icon=ImageTk.PhotoImage(icon0)
    root.iconphoto(False, icon)

    # Add TextArea
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    # Creating MenuBar
    MainMenu = Menu(root)

    # File Menu Starts Here
    FileMenu = Menu(MainMenu, tearoff=0)

    # open new file
    FileMenu.add_command(label="New", command=newFile)

    # To open Already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # To save current File
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MainMenu.add_cascade(label="File", menu=FileMenu)
    # File Menu Ends Here


    # Edit Menu Starts Here
    EditMenu = Menu(MainMenu, tearoff=0)

    # Providing Cut,Copy,Paste features
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MainMenu.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends Here


    # Help Menu Starts Here
    HelpMenu = Menu(MainMenu, tearoff=0)

    HelpMenu.add_command(label="About Notepad",command=about)
    MainMenu.add_cascade(label="About",menu=HelpMenu)
    # Help Menu Ends Here

    # Adding ScrollBar
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)


    root.config(menu=MainMenu)

    root.mainloop()
    
# Coded by - Karan Singh 

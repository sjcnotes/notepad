from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)
def openFile():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files","*.*"),
                                     ("Text Documents",
"*.txt")])
    if file == "":
        file= None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",
                           filetypes=[("All Files","*.*"),
                                     ("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #save a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("file saved")
    else:
            #save a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
    
def quitApp():
    pass
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("NotePad","Notepad developed By Raushan Kumar")

if __name__ =='__main__':
    #basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    #root.wm_iconbitmap("2.png")
    root.geometry("644x788")
    
    #add text area
    TextArea = Text(root,font="lucuda 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    
    #lets code a menu bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar,tearoff=0)
    #to open new file
    FileMenu.add_command(label="New",command=newFile)
    #to open already existing file
    FileMenu.add_command(label="Open",command = openFile)
    #to save the current file
    FileMenu.add_command(label = "Save",command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit",command=quitApp)
    MenuBar.add_cascade(label = "File",menu=FileMenu)
    #file menu starts
    EditMenu = Menu(MenuBar,tearoff=0)
    #to give a feature of cut copy and paste
    EditMenu.add_command(label = "Cut",command=cut)
    EditMenu.add_command(label = "Copy",command=copy)
    EditMenu.add_command(label = "Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    
    #edit menu ends
  
    
    #Help menu starts
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label = "About NotePad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    
    
    #help menu ends
    root.config(menu=MenuBar)
    
    #adding scrollbar using rules from tkinter 
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    
    root.mainloop()

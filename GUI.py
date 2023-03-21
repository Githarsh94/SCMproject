from tkinter import *
from main import *
root = Tk()

def encryptscreen():
    global userinput
    userinput = Entry(root,width=50)
    userinput.grid(row=1,column=1)
    Decryptscreenbutton.grid_remove()
    Encryptscreenbutton.grid_remove()
    Encryption = Button(root, text="Encrypt", command=Encrypt)
    Encryption.grid(row=1,column=0)
def Encrypt():
    label2 = Label(root, text=encrypt(userinput.get()))
    label3 = Label(root, text="")
    label2.grid(row=2,column=1)
def main():
    global Encryptscreenbutton
    global Decryptscreenbutton
    label1 = Label(root, text="Welcome to #404 ED Tool")
    Encryptscreenbutton = Button(root, text="Encryption", command=encryptscreen)
    Decryptscreenbutton = Button(root, text="Decryption")

    label1.grid(row=0,column=0)
    Encryptscreenbutton.grid(row=1,column=0)
    Decryptscreenbutton.grid(row=2,column=0)

main()



root.mainloop()



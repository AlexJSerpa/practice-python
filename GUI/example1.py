from tkinter import *

root = Tk()

root.title("Example title")

root.resizable(0, 1)

#photo = PhotoImage(file='samurai_python.png')
#root.iconphoto(False, photo)

root.iconbitmap('@samurai_python.xbm')

root.geometry("1080x720")

root.config(bg="blue")

root.mainloop()
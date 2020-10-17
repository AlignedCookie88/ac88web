import ac88web as wb
import tkinter as tk
import random as rd
from tkinter import simpledialog
from tkinter import filedialog as fd
import yaml

root = tk.Tk()
root.title("Website Editor | AC88 Web")
root.resizable(False, False)

title = "My website"
font = "Arial"
file = None

def test():
    global title, font, bodybox, root
    port = rd.randint(81, 1000)
    root.title(f"Testing site on port {port} | Website Editor | AC88 Web")
    print(f"Testing site on port {port}")
    body = bodybox.get(0.0, tk.END).strip()
    html = wb.compilecode(title, body, font=font)
    wb.run(port, html, onlylh=True)
    root.title("Website Editor | AC88 Web")

def settitle():
    global title
    toset = simpledialog.askstring("Set Title", "Set title to:", parent=root)
    if type(toset)==str:
        title = toset

def setfont():
    global font
    toset = simpledialog.askstring("Set Font", "Set font to:", parent=root)
    if type(toset)==str:
        font = toset

def save():
    global bodybox
    if file==None:
        saveas()
        return
    f = open(file, mode="w")
    f.truncate(0)
    savedict = {"title": title, "font": font, "body": bodybox.get(0.0, tk.END)}
    yaml.dump(savedict, f)
    f.close()

def saveas():
    global bodybox, file
    f = fd.asksaveasfile(title="Save As", filetypes=[("AC88 Website", ".acws")])
    file = f.name
    f.truncate(0)
    savedict = {"title": title, "font": font, "body": bodybox.get(0.0, tk.END)}
    yaml.dump(savedict, f)
    f.close()

def openf():
    global bodybox, file, title, font
    f = fd.askopenfile(title="Open", filetypes=[("AC88 Website", ".acws")])
    file = f.name
    opendict = yaml.load(f, Loader=yaml.FullLoader)
    title = opendict["title"]
    font = opendict["font"]
    bodybox.delete(0.0, tk.END)
    bodybox.insert(tk.END, opendict["body"])
    f.close()

def new():
    global title, font, bodybox, file
    file = None
    title="My website"
    font="Arial"
    bodybox.delete(0.0, tk.END)
    bodybox.insert(tk.END, "<h1>My website</h1>\n<h2>Code here!</h2>") 

menubar = tk.Menu(root)
root.config(menu=menubar)

fileMenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Save", command=save)
fileMenu.add_command(label="Save As", command=saveas)
fileMenu.add_command(label="Open", command=openf)
fileMenu.add_command(label="New", command=new)

siteMenu = tk.Menu(menubar)
menubar.add_cascade(label="Site", menu=siteMenu)

siteMenu.add_command(label="Font", command=setfont)
siteMenu.add_command(label="Title", command=settitle)
siteMenu.add_command(label="Test", command=test)

bodybox = tk.Text(root, width=90, height=25)
bodybox.grid(column=0, row=1, columnspan=2)
bodybox.insert(tk.END, "<h1>My website</h1>\n<h2>Code here!</h2>")

root.mainloop()

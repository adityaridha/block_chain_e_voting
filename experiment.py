import hashlib
from tkinter import *



root = Tk()
org_str = StringVar()
org_str.set('')



t = Entry(root, textvariable = org_str)
t.pack()

temp = str(org_str)
hash_object = hashlib.sha256(temp.encode('utf-8'))
hex_dig = hash_object.hexdigest()
org_str.set(hex_dig)

l = Label(root, textvariable = org_str, width=100)
l.pack()

root.mainloop()

# from tkinter import *
# from time import sleep
#
# root = Tk()
# var = StringVar()
# var.set('hello')
#
# l = Label(root, textvariable = var)
# l.pack()
#
# for i in range(6):
#     sleep(1) # Need this to slow the changes down
#     var.set('goodbye' if i%2 else 'hello')
#     root.update_idletasks()
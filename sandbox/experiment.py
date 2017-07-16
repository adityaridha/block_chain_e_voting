import hashlib
from tkinter import *

#
#
# root = Tk()
# org_str = StringVar()
# org_str.set('')
#
#
#
# t = Entry(root, textvariable = org_str)
# t.pack()
#
# temp = str(org_str)
# hash_object = hashlib.sha256(temp.encode('utf-8'))
# hex_dig = hash_object.hexdigest()
# org_str.set(hex_dig)
#
# l = Label(root, textvariable = org_str, width=100)
# l.pack()
#
# root.mainloop()

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

import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()

    self.node_1_ahok_count, self.node_2_ahok_count, self.node_3_ahok_count, self.node_4_ahok_count,
    self.node_1_anies_count, self.node_2_anies_count, self.node_3_anies_count, self.node_4_anies_count
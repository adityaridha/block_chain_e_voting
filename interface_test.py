import csv
import hashlib
from tkinter import ttk
from tkinter import *
from collections import Counter
import datetime

# Create root
self.root = Tk()
self.root.geometry('1000x500+0+0')

# Create canvas
self.canvas = Canvas(self.root)
self.canvas.pack(side=TOP, fill=BOTH, expand=TRUE)

# Create scrollbars
self.xscrollbar = Scrollbar(self.root, orient=HORIZONTAL, command=self.canvas.xview)
self.xscrollbar.pack(side=BOTTOM, fill=X)
self.yscrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
self.yscrollbar.pack(side=RIGHT, fill=Y)

# Attach canvas to scrollbars
self.canvas.configure(xscrollcommand=self.xscrollbar.set)
self.canvas.configure(yscrollcommand=self.yscrollbar.set)

# Create frame inside canvas
self.frame = Frame(self.canvas)
self.canvas.create_window((0,0), window=self.frame, anchor=NW)
self.frame.bind('<Configure>', self.set_scrollregion)

# Write db contents to canvas
self.print_dbcontents()

# Invoke main loop
self.root.mainloop()

def set_scrollregion(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox('all'))
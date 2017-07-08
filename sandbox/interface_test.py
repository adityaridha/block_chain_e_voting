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



    # self.tree = ttk.Treeview(self.master, height=20)
    # self.tree.pack(side="right")
    #
    # self.vsb = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
    # self.vsb.pack(side='right', fill='y')
    # self.tree.configure(yscrollcommand=self.vsb.set)
    #
    # self.tree["columns"] = ("#1", "#2")
    # self.tree.heading("#0", text="Voter")
    # self.tree.heading("#1", text="Pilihan")
    # self.tree.heading("#2", text="Time stamp")
    # self.tree.column("#1", width=100)
    # self.tree.column("#2", width=120)
    #
    # with open("data.csv") as file:
    #     data_pointer = csv.reader(file, delimiter=",")
    #     list_data = list(data_pointer)
    #
    # count_vote = []
    # for index, data in enumerate(list_data):
    #     if data != [] :
    #         count_vote.append(data[1])
    #         self.tree.insert("", index, text=data[0], values=(data[1], data[2]))
    #
    # cf_ahok = Counter(count_vote).get('Ahok')
    # cf_anies = Counter(count_vote).get('Anies')
    # print(cf_ahok)
    # print(cf_anies)
    #
    # self.tree.pack()
    # self.tree.place(x=700, y=50)

    # You have to use lambda to pass paramater to the function that set as command parameter
    #
    # A = Button(root, text="Ahok-Djarot", command = lambda : self.choose_option(candidate='Ahok'), width=35, height=15, bg="red")
    # A.place(x=50, y=50)
    #
    # B = Button(root, text="Anies-Sandi", command = lambda : self.choose_option(candidate='Anies'), width=35, height=15, bg="blue")
    # B.place(x=320, y=50)
    #
    # self.cf_ahok_view = Label(root, text=cf_ahok, font=("Calibri", 44))
    # self.cf_ahok_view.place(x=120, y=350)
    #
    # self.cf_anies_view = Label(root, text=cf_anies, font=("Calibri", 44))
    # self.cf_anies_view.place(x=420, y=350)
import csv
import hashlib
from tkinter import *
from tkinter import font
from collections import Counter
import datetime

class Pemilu:

    def __init__(self, master):


        self.root = master
        self.myvar = ''
        self.main_frame = Canvas(self.root)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

        self.scroll_bar = Scrollbar(self.root, orient=HORIZONTAL)
        self.scroll_bar.pack(side=BOTTOM, fill=X)

        self.main_frame.configure(xscrollcommand=self.scroll_bar.set)
        self.my_font = font.Font(family="Segoe UI", size=9)



        ''' NODE #1 widget declaration'''

        node_1_margin_x = 10
        node_2_margin_x = 350

        labelframe = LabelFrame(self.main_frame, text="NODE #1", width=330, height=280)
        labelframe.place(x=node_1_margin_x, y=20)

        self.ahok_label = Label(text="Ahok")
        self.ahok_label.place(x=node_1_margin_x+20, y=50)

        self.ahok_entry = Entry(self.main_frame, width=40)
        self.ahok_entry.place(x=node_1_margin_x+60, y=50)

        self.anies_label = Label(text="Anies")
        self.anies_label.place(x=node_1_margin_x+20, y=76)

        self.anies_entry = Entry(self.main_frame, width=40)
        self.anies_entry.place(x=node_1_margin_x+60, y=76)

        self.gen_label = Label(text="Genesis")
        self.gen_value = Text(self.main_frame, width=40, height=3, font=self.my_font)
        self.gen_label.place(x=node_1_margin_x+10,  y=102)
        self.gen_value.place(x=node_1_margin_x+60, y=102)
        self.gen_value.grid_propagate(False)

        self.gen_value.insert(END, "this is Genesis")
        self.gen_value.configure(state=DISABLED, bg="#d4d6d8")

        height_hash = 162
        self.hash_label = Label(text="Hash")
        self.hash_value = Text(self.main_frame, width=30, height=3)
        self.hash_label.place(x=node_1_margin_x+20,  y=height_hash)
        self.hash_value.place(x=node_1_margin_x+60, y=height_hash)

        height_button = 230
        hash_meth = Button(self.main_frame, text="Hash", command= lambda : self.get_hash(node=1), width=9, height=1)
        send_meth = Button(self.main_frame, text="Broadcast", command= lambda : self.broadcast_hash(node_dest=2), width=9, height=1)
        disable_node = Button(self.main_frame, text="Disable", command=lambda: self.get_hash(node=1), width=9, height=1)
        disable_node.place(x=node_1_margin_x+230, y=height_button)
        hash_meth.place(x=node_1_margin_x+60, y=height_button)
        send_meth.place(x=node_1_margin_x+145, y=height_button)




        ''' NODE #2 widget declaration'''

        margin_2 = node_1_margin_x + 300

        labelframe = LabelFrame(self.main_frame, text="NODE #2", width=330, height=280)
        labelframe.place(x=node_2_margin_x, y=20)

        self.ahok_label_2 = Label(text="Ahok")
        self.ahok_label_2.place(x=60+margin_2, y=50)

        self.ahok_entry_2 = Entry(self.main_frame, width=40)
        self.ahok_entry_2.place(x=100+margin_2, y=50)

        self.anies_label_2 = Label(text="Anies")
        self.anies_label_2.place(x=60+margin_2, y=76)

        self.anies_entry_2 = Entry(self.main_frame, width=40)
        self.anies_entry_2.place(x=100+margin_2, y=76)

        self.prev_label_2 = Label(text="Hash #1")
        self.prev_value_2 = Text(self.main_frame, width=30, height=3)
        self.prev_label_2.place(x=50+margin_2,  y=102)
        self.prev_value_2.place(x=100+margin_2, y=102)

        height_hash = 162
        self.hash_label_2 = Label(text="Hash")
        self.hash_value_2 = Text(self.main_frame, width=30, height=3)
        self.hash_label_2.place(x=60+margin_2,  y=height_hash)
        self.hash_value_2.place(x=100+margin_2, y=height_hash)

        height_button = 230
        hash_meth_2 = Button(self.main_frame, text="Hash", command= lambda : self.get_hash(node=2), width=9, height=1)
        send_meth_2 = Button(self.main_frame, text="Broadcast", command=lambda : self.broadcast_hash(node_dest=3), width=9, height=1)
        disable_node = Button(self.main_frame, text="Disable", command=lambda: self.get_hash(node=1), width=9, height=1)
        disable_node.place(x=270 + margin_2, y=height_button)
        hash_meth_2.place(x=100+margin_2, y=height_button)
        send_meth_2.place(x=185+margin_2, y=height_button)

        ''' NODE #3 widget declaration'''

        margin_3 = margin_2*2+30

        labelframe = LabelFrame(self.main_frame, text="NODE #3", width=330, height=280)
        labelframe.place(x=40 + margin_3, y=20)

        self.ahok_label_3 = Label(text="Ahok")
        self.ahok_label_3.place(x=60 + margin_3, y=50)

        self.ahok_entry_3 = Entry(self.main_frame, width=40)
        self.ahok_entry_3.place(x=100 + margin_3, y=50)

        self.anies_label_3 = Label(text="Anies")
        self.anies_label_3.place(x=60 + margin_3, y=76)

        self.anies_entry_3 = Entry(self.main_frame, width=40)
        self.anies_entry_3.place(x=100 + margin_3, y=76)

        self.prev_label_3 = Label(text="Hash #2")
        self.prev_value_3 = Text(self.main_frame, width=30, height=3)
        self.prev_label_3.place(x=50 + margin_3, y=102)
        self.prev_value_3.place(x=100 + margin_3, y=102)

        height_hash = 162
        self.hash_label_3 = Label(text="Hash")
        self.hash_value_3 = Text(self.main_frame, width=30, height=3)
        self.hash_label_3.place(x=60 + margin_3, y=height_hash)
        self.hash_value_3.place(x=100 + margin_3, y=height_hash)

        height_button = 230
        hash_meth_3 = Button(self.main_frame, text="Hash", command=lambda: self.get_hash(node=3), width=9, height=1)
        send_meth_3 = Button(self.main_frame, text="Broadcast", command=lambda: self.broadcast_hash(node_dest=4), width=9, height=1)
        disable_node = Button(self.main_frame, text="Disable", command=lambda: self.get_hash(node=1), width=9, height=1)
        disable_node.place(x=270 + margin_3, y=height_button)
        hash_meth_3.place(x=100 + margin_3, y=height_button)
        send_meth_3.place(x=185 + margin_3, y=height_button)

        ''' NODE #4 widget declaration'''

        margin_4 = margin_2*3+60

        labelframe = LabelFrame(self.main_frame, text="NODE #4", width=330, height=280)
        labelframe.place(x=40 + margin_4, y=20)

        self.ahok_label_4 = Label(text="Ahok")
        self.ahok_label_4.place(x=60 + margin_4, y=50)

        self.ahok_entry_4 = Entry(self.main_frame, width=40)
        self.ahok_entry_4.place(x=100 + margin_4, y=50)

        self.anies_label_4 = Label(text="Anies")
        self.anies_label_4.place(x=60 + margin_4, y=76)

        self.anies_entry_4 = Entry(self.main_frame, width=40)
        self.anies_entry_4.place(x=100 + margin_4, y=76)

        self.prev_label_4 = Label(text="Hash #3")
        self.prev_value_4 = Text(self.main_frame, width=30, height=3)
        self.prev_label_4.place(x=50 + margin_4, y=102)
        self.prev_value_4.place(x=100 + margin_4, y=102)

        height_hash = 162
        self.hash_label_4 = Label(text="Hash")
        self.hash_value_4 = Text(self.main_frame, width=30, height=3)
        self.hash_label_4.place(x=60 + margin_4, y=height_hash)
        self.hash_value_4.place(x=100 + margin_4, y=height_hash)

        height_button = 230
        hash_meth_4 = Button(self.main_frame, text="Hash", command=lambda: self.get_hash(node=4), width=9, height=1)
        send_meth_4 = Button(self.main_frame, text="Broadcast", command=lambda : self.broadcast_hash(), width=9, height=1)
        disable_node = Button(self.main_frame, text="Disable", command=lambda: self.get_hash(node=1), width=9, height=1)
        disable_node.place(x=270 + margin_4, y=height_button)
        hash_meth_4.place(x=100 + margin_4, y=height_button)
        send_meth_4.place(x=185 + margin_4, y=height_button)

        self.scroll_bar.config(command=self.main_frame.xview())

        '''Database Layout'''

        Label(text="Database Node#1").place(x=node_1_margin_x, y=320)
        Label(text="Ahok").place(x=240, y=320)
        Label(text="Anies").place(x=290, y=320)

        node_1_y_level = 350
        node_1_x_level_one = 240
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = 180

        self.node_1_db = Text(self.main_frame, width=20, height=9)
        self.node_1_db.place(x=node_1_margin_x, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_1_y_level)


        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_5_level)

        ''' ################### NODE 2 ################### '''

        add_margin = 340

        Label(text="Database Node#2").place(x=350, y=320)
        Label(text="Ahok").place(x=240+add_margin, y=320)
        Label(text="Anies").place(x=290+add_margin, y=320)

        node_1_y_level = 350
        node_1_x_level_one = 240+add_margin
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = node_1_x_level_one - 60

        self.node_1_db = Text(self.main_frame, width=20, height=9)
        self.node_1_db.place(x=10+add_margin, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_1_y_level)


        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_5_level)

        ''' ################### NODE 3 ################### '''

        add_margin = 340+340

        Label(text="Database Node#3").place(x=10+add_margin, y=320)
        Label(text="Ahok").place(x=240+add_margin, y=320)
        Label(text="Anies").place(x=290+add_margin, y=320)

        node_1_y_level = 350
        node_1_x_level_one = 240+add_margin
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = node_1_x_level_one - 60

        self.node_1_db = Text(self.main_frame, width=20, height=9)
        self.node_1_db.place(x=10+add_margin, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_1_y_level)


        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_5_level)

        ''' ################### NODE 4 ################### '''

        add_margin = 340+340+340

        Label(text="Database Node#4").place(x=10+add_margin, y=320)
        Label(text="Ahok").place(x=240+add_margin, y=320)
        Label(text="Anies").place(x=290+add_margin, y=320)

        node_1_y_level = 350
        node_1_x_level_one = 240+add_margin
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = node_1_x_level_one - 60

        self.node_1_db = Text(self.main_frame, width=20, height=9)
        self.node_1_db.place(x=10+add_margin, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_1_y_level)


        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_2_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_3_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_4_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_one, y=node_5_level)
        self.node_1_db = Text(self.main_frame, width=5, height=1)
        self.node_1_db.place(x=node_1_x_level_two, y=node_5_level)


        Button(text='Generate Data', width=15, height=2, bg='#f8c659').place(x=node_1_margin_x, y=node_5_level+100)



    def get_hash(self,node):
        if node == 1:
            val = self.ahok_entry.get() +','+ self.anies_entry.get()+','+self.gen_value.get("1.0",END)
            print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value.delete("1.0",END)
            self.hash_value.insert(END, hash_hex)
            print(hash_hex)
        if node == 2:
            val = self.ahok_entry_2.get() +','+ self.anies_entry_2.get()+','+self.prev_value_2.get("1.0",END)
            print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_2.delete("1.0",END)
            self.hash_value_2.insert(END, hash_hex)
            print(hash_hex)
        if node == 3:
            val = self.ahok_entry_3.get() +','+ self.anies_entry_3.get()+','+self.prev_value_3.get("1.0",END)
            print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_3.delete("1.0",END)
            self.hash_value_3.insert(END, hash_hex)
            print(hash_hex)
        if node == 4:
            val = self.ahok_entry_4.get() +','+ self.anies_entry_4.get()+','+self.prev_value_4.get("1.0",END)
            print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_4.delete("1.0",END)
            self.hash_value_4.insert(END, hash_hex)
            print(hash_hex)

    def broadcast_hash(self,node_dest):

        if node_dest == 2:
            source_hash = self.hash_value
            prev_hash_value = self.prev_value_2
        if node_dest == 3:
            source_hash = self.hash_value_2
            prev_hash_value = self.prev_value_3
        if node_dest == 4:
            source_hash = self.hash_value_3
            prev_hash_value = self.prev_value_4

        hash_value = source_hash.get(1.0, END)
        prev_hash_value.delete("1.0", END)
        prev_hash_value.insert(END, hash_value)



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

    def choose_option(self, candidate):
        time = datetime.datetime.now().replace(microsecond=0)

        with open('data.csv') as csvfile :
            read_data = csv.reader(csvfile, delimiter=',')
            last_index = len(list(read_data))

        with open('data.csv', 'a', newline='') as csvfile:
            write_csv = csv.writer(csvfile, delimiter = ',')
            if candidate == 'Ahok' :
                write_csv.writerow(['Voter {}'.format(last_index), 'Ahok', time])
                self.tree.insert("", 0, text='Voter {}'.format(last_index+1), values=("Ahok", time))
            if candidate == 'Anies':
                write_csv.writerow(['Voter {}'.format(last_index), 'Anies', time])
                self.tree.insert("", 0, text='Voter {}'.format(last_index+1), values=("Anies", time))

        with open("data.csv") as file:
            data_pointer = csv.reader(file, delimiter=",")
            list_data = list(data_pointer)

        count_vote = []
        for index, data in enumerate(list_data):
            if data != [] :
                count_vote.append(data[1])

        cf_ahok = Counter(count_vote).get('Ahok')
        cf_anies = Counter(count_vote).get('Anies')

        if candidate == 'Ahok': self.cf_ahok_view.configure(text=cf_ahok)
        if candidate == 'Anies': self.cf_anies_view.configure(text=cf_anies)

root = Tk()
root.geometry("1372x700")
root.title('E-VOTING SIMULATION USING BLOCKCHAIN')
# root.resizable(width=False, height=False)
Pemilu(root)
root.mainloop()

import csv
import hashlib
from tkinter import ttk
from tkinter import *
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



        ''' NODE #1 widget declaration'''

        margin_1 = -30

        labelframe = LabelFrame(self.main_frame, text="NODE #1", width=330, height=280)
        labelframe.place(x=40+margin_1, y=20)

        self.ahok_label = Label(text="Ahok")
        self.ahok_label.place(x=60+margin_1, y=50)

        self.ahok_entry = Entry(self.main_frame, width=40)
        self.ahok_entry.place(x=100+margin_1, y=50)

        self.anies_label = Label(text="Anies")
        self.anies_label.place(x=60+margin_1, y=76)

        self.anies_entry = Entry(self.main_frame, width=40)
        self.anies_entry.place(x=100+margin_1, y=76)

        self.gen_label = Label(text="Genesis")
        self.gen_value = Text(self.main_frame, width=30, height=3)
        self.gen_label.place(x=50+margin_1,  y=102)
        self.gen_value.place(x=100+margin_1, y=102)

        height_hash = 162
        self.hash_label = Label(text="Hash")
        self.hash_value = Text(self.main_frame, width=30, height=3)
        self.hash_label.place(x=60+margin_1,  y=height_hash)
        self.hash_value.place(x=100+margin_1, y=height_hash)

        height_button = 230
        hash_meth = Button(self.main_frame, text="Hash", command= lambda : self.get_hash(node=1), width=9, height=1)
        send_meth = Button(self.main_frame, text="Send", command= lambda : self.send_hash(node_dest=2), width=9, height=1)
        hash_meth.place(x=100+margin_1, y=height_button)
        send_meth.place(x=190+margin_1, y=height_button)



        ''' NODE #2 widget declaration'''

        margin_2 = 310

        labelframe = LabelFrame(self.main_frame, text="NODE #2", width=330, height=280)
        labelframe.place(x=40+margin_2, y=20)

        self.ahok_label_2 = Label(text="Ahok")
        self.ahok_label_2.place(x=60+margin_2, y=50)

        self.ahok_entry_2 = Entry(self.main_frame, width=40)
        self.ahok_entry_2.place(x=100+margin_2, y=50)

        self.anies_label_2 = Label(text="Anies")
        self.anies_label_2.place(x=60+margin_2, y=76)

        self.anies_entry_2 = Entry(self.main_frame, width=40)
        self.anies_entry_2.place(x=100+margin_2, y=76)

        self.prev_label_2 = Label(text="Genesis")
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
        send_meth_2 = Button(self.main_frame, text="Send", command=lambda : self.send_hash(node_dest=3), width=9, height=1)
        hash_meth_2.place(x=100+margin_2, y=height_button)
        send_meth_2.place(x=190+margin_2, y=height_button)

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

        self.prev_label_3 = Label(text="Genesis")
        self.prev_value_3 = Text(self.main_frame, width=30, height=3)
        self.prev_label_3.place(x=50 + margin_3, y=102)
        self.prev_value_3.place(x=100 + margin_3, y=102)

        height_hash = 162
        self.hash_label_3 = Label(text="Hash")
        self.hash_value_3 = Text(self.main_frame, width=30, height=3)
        self.hash_label_3.place(x=60 + margin_3, y=height_hash)
        self.hash_value_3.place(x=100 + margin_3, y=height_hash)

        height_button = 230
        hash_meth_3 = Button(self.main_frame, text="Hash", command=self.get_hash, width=9, height=1)
        send_meth_3 = Button(self.main_frame, text="Send", command=self.get_hash, width=9, height=1)
        hash_meth_3.place(x=100 + margin_3, y=height_button)
        send_meth_3.place(x=190 + margin_3, y=height_button)

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

        self.gen_label_4 = Label(text="Genesis")
        self.gen_value_4 = Text(self.main_frame, width=30, height=3)
        self.gen_label_4.place(x=50 + margin_4, y=102)
        self.gen_value_4.place(x=100 + margin_4, y=102)

        height_hash = 162
        self.hash_label_4 = Label(text="Hash")
        self.hash_value_4 = Text(self.main_frame, width=30, height=3)
        self.hash_label_4.place(x=60 + margin_4, y=height_hash)
        self.hash_value_4.place(x=100 + margin_4, y=height_hash)

        height_button = 230
        hash_meth_4 = Button(self.main_frame, text="Hash", command=self.get_hash, width=9, height=1)
        send_meth_4 = Button(self.main_frame, text="Send", command=self.get_hash, width=9, height=1)
        hash_meth_4.place(x=100 + margin_4, y=height_button)
        send_meth_4.place(x=190 + margin_4, y=height_button)

        self.scroll_bar.config(command=self.main_frame.xview())



    def get_hash(self,node):
        if node == 1:
            val = self.ahok_entry.get() +','+ self.anies_entry.get()
            print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value.delete("1.0",END)
            self.hash_value.insert(END, hash_hex)
            # self.hash_value.configure(state=DISABLED, bg='GREY')
            print(hash_hex)
        if node ==2:
            val = self.ahok_entry_2.get() +','+ self.anies_entry_2.get()+','+self.prev_value_2.get("1.0",END)
            print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_2.delete("1.0",END)
            self.hash_value_2.insert(END, hash_hex)
            # self.hash_value.configure(state=DISABLED, bg='GREY')
            print(hash_hex)


    def send_hash(self,node_dest):
        if node_dest==2:
            hash_1 = self.hash_value.get(1.0,END)
            self.prev_value_2.delete("1.0",END)
            self.prev_value_2.insert(END, hash_1)
        if node_dest == 3:
            print(3)
            hash_1 = self.hash_value_2.get(1.0, END)
            self.prev_value_3.delete("1.0", END)
            self.prev_value_3.insert(END, hash_1)


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
root.geometry("1372x600")
Pemilu(root)
root.mainloop()




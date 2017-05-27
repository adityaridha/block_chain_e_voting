import csv
from tkinter import ttk
from tkinter import *
from collections import Counter
import datetime

class Pemilu:

    def __init__(self, master):
        self.master = master

        self.tree = ttk.Treeview(self.master, height=20)
        self.tree.pack(side="right")


        self.vsb = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        self.vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.vsb.set)

        self.tree["columns"] = ("#1", "#2")

        self.tree.heading("#0", text="Voter")
        self.tree.heading("#1", text="Pilihan")
        self.tree.heading("#2", text="Time stamp")
        self.tree.column("#1", width=100)
        self.tree.column("#2", width=120)

        with open("data.csv") as file:
            data_pointer = csv.reader(file, delimiter=",")
            list_data = list(data_pointer)

        count_vote = []
        for index, data in enumerate(list_data):
            if data != [] :
                count_vote.append(data[1])
                self.tree.insert("", index, text=data[0], values=(data[1], data[2]))

        count_result = list(Counter(count_vote))
        count_result_recap = []

        print(count_result)

        for candidate in count_result:
            count_for_candidate = Counter(count_vote).get(candidate)
            count_result_recap.append([candidate, count_for_candidate])

        # print(count_result_recap)

        self.tree.pack()
        self.tree.place(x=700, y=50)

        # You have to use lambda to pass paramater to the function that set as command parameter

        A = Button(root, text="Ahok-Djarot", command = lambda : self.choose_option(candidate='Ahok'), width=35, height=15, bg="red")
        A.place(x=50, y=50)

        B = Button(root, text="Anies-Sandi", command = lambda : self.choose_option(candidate='Anies'), width=35, height=15, bg="blue")
        B.place(x=320, y=50)



    def choose_option(self, candidate):
        time = datetime.datetime.now().replace(microsecond=0)

        with open('data.csv') as csvfile :
            read_data = csv.reader(csvfile, delimiter=',')
            last_index = len(list(read_data))
            print(last_index)

        with open('data.csv', 'a', newline='') as csvfile:
            write_csv = csv.writer(csvfile, delimiter = ',')
            if candidate == 'Ahok' :
                write_csv.writerow(['Voter {}'.format(last_index), 'Ahok', time])
                self.tree.insert("", 0, text='Voter {}'.format(last_index), values=("Ahok", time))
            if candidate == 'Anies':
                write_csv.writerow(['Voter {}'.format(last_index), 'Anies', time])
                self.tree.insert("", 0, text='Voter {}'.format(last_index), values=("Anies", time))

root = Tk()
root.geometry("1150x600")
Pemilu(root)
root.mainloop()




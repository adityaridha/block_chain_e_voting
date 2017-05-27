# from cryptography.hazmat.primitives import serialization as crypto_serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.backends import default_backend as crypto_default_backend
#
# key = rsa.generate_private_key(
#     backend=crypto_default_backend(),
#     public_exponent=65537,
#     key_size=512
# )
# private_key = key.private_bytes(
#     crypto_serialization.Encoding.PEM,
#     crypto_serialization.PrivateFormat.PKCS8,
#     crypto_serialization.NoEncryption())
#
# public_key = key.public_key().public_bytes(
#     crypto_serialization.Encoding.OpenSSH,
#     crypto_serialization.PublicFormat.OpenSSH
# )
#
# print(private_key)
# print(public_key)



import tkinter as tk
from tkinter import ttk


from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()


root = Tk()
root.geometry("1550x600")
tree = ttk.Treeview(root, height = 23)
tree["columns"]=("#1","#2")

tree.heading("#0", text = "Voter")
tree.heading("#1", text="Pilihan")
tree.heading("#2", text="Time stamp")
tree.column("#1", width=100)
tree.column("#2", width=150)



def choose_ahok():
    # msg = messagebox.showinfo( "Pemilu 2019", "Anda yakin untuk memilih Ahok ?")
    # with open('data.csv') as csvfile:
    #     readcsv = csv.reader(csvfile, delimiter=',')
    #     voting_count = len(list(readcsv))
    # print(voting_count)
    # hash_object = hashlib.sha256(b'Hello, World')
    # hash_dig = hash_object.hexdigest()

    time = datetime.datetime.now().replace(microsecond=0)
    with open('data.csv', 'a', newline='') as csvfile:
        registration_data = csv.writer(csvfile, delimiter=',')
        registration_data.writerow(["Nama","Ahok", time])

    with open('data.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            print(row)

    root.mainloop()

def choose_anis():
   # msg = messagebox.showinfo("Pemilu 2019", "Saya pilih Anis")
    pass

def refresh():
    # root.destroy()
    root.mainloop()
    root.geometry("1550x600")






with open("data.csv") as file :
    data_pointer = csv.reader(file, delimiter=",")
    list_data = list(data_pointer)
# print(list_data)

count_vote =[]
for i, data in enumerate(list_data):
    # print(data)
    # print(data[1])
    count_vote.append(data[1])
    tree.insert("" , i,    text=data[0], values=(data[1],data[2]))

count_result = list(Counter(count_vote))
count_result_recap = []

for candidate in count_result :
    count_for_candidate = Counter(count_vote).get(candidate)
    count_result_recap.append([candidate, count_for_candidate])

# print(count_result_recap)

tree.pack()
tree.place(x= 700, y=50)
#
A = Button(root, text = "Ahok-Djarot", command = choose_ahok, width=35, height=15, bg="red")
A.place(x = 50,y = 50)

B = Button(root, text = "Anies-Sandi", command = choose_anis, width=35, height=15, bg="blue")
B.place(x = 320,y = 50)

root.mainloop()

# top.mainloop()
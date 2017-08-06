import csv
import hashlib
import os
import binascii
from datetime import datetime
import time
import ecdsa
import sqlite3
from tkinter import *
from tkinter import font, ttk
from collections import Counter
from random import randint
from ecdsa import BadSignatureError
from ecdsa import SigningKey, VerifyingKey


class Pemilu:

    def __init__(self, master):


        self.root = master
        self.myvar = ''
        self.main_frame = Canvas(self.root)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

        '''scroll bar still not working'''
        # self.scroll_bar = Scrollbar(self.root, orient=VERTICAL)
        # self.scroll_bar.pack(side=RIGHT, fill=Y)
        # self.main_frame.configure(xscrollcommand=self.scroll_bar.set)

        self.my_font = font.Font(family="Segoe UI", size=7)

        ''' NODE #1 widget declaration'''

        node_1_margin_x = 10
        node_2_margin_x = 350

        height_frame = 330
        labelframe = LabelFrame(self.main_frame, text="NODE #1", width=330, height=height_frame)
        labelframe.place(x=node_1_margin_x, y=20)

        self.ahok_label = Label(text="Cand #1")
        self.ahok_label.place(x=node_1_margin_x+5, y=50)

        self.node_1_ahok_count = Entry(self.main_frame, width=40)
        self.node_1_ahok_count.place(x=node_1_margin_x+60, y=50)

        self.anies_label = Label(text="Cand #2")
        self.anies_label.place(x=node_1_margin_x+5, y=76)

        self.node_1_anies_count = Entry(self.main_frame, width=40)
        self.node_1_anies_count.place(x=node_1_margin_x+60, y=76)

        self.gen_label = Label(text="Genesis")
        self.gen_value = Text(self.main_frame, width=30, height=3, bg='#F0F0F0')
        self.gen_value.grid_propagate(False)
        self.gen_label.place(x=node_1_margin_x+10,  y=102)
        self.gen_value.place(x=node_1_margin_x+60,  y=102)

        self.gen_value.insert(END, "this is Genesis ")
        self.gen_value.configure(state=DISABLED)

        height_hash = 162
        self.hash_label = Label(text="Hash")
        self.hash_value = Text(self.main_frame, width=30, height=3)
        self.hash_label.place(x=node_1_margin_x+20,  y=height_hash)
        self.hash_value.place(x=node_1_margin_x+60, y=height_hash)

        height_key = 225
        self.key_label = Label(text="Key")
        self.node_1_key_value = Text(self.main_frame, width=30, height=3)
        self.key_label.place(x=node_1_margin_x + 20, y=height_key)
        self.node_1_key_value.place(x=node_1_margin_x + 60, y=height_key)
        self.node_1_key_value.delete('1.0', END)
        self.node_1_key_value.insert('1.0',open("certificate/private_1.pem").read())

        height_button = 300
        self.hash_meth = Button(self.main_frame, text="Hash", command=lambda: self.get_hash(node=1), width=9, height=1)
        self.send_meth = Button(self.main_frame, text="Broadcast", command=lambda: self.broadcast_hash(node_dest=2), width=9, height=1)
        self.disb_node = Button(self.main_frame, text="Disable", command=lambda: self.disable_node(node=1, sync=False), fg='white', bg='#91181e', width=9, height=1)
        self.disb_node.place(x=node_1_margin_x+230, y=height_button)
        self.hash_meth.place(x=node_1_margin_x+60, y=height_button)
        self.send_meth.place(x=node_1_margin_x+145, y=height_button)

        ''' NODE #2 widget declaration'''

        margin_2 = node_1_margin_x + 300

        labelframe = LabelFrame(self.main_frame, text="NODE #2", width=330, height=height_frame)
        labelframe.place(x=node_2_margin_x, y=20)

        self.ahok_label_2 = Label(text="Cand #1")
        self.ahok_label_2.place(x=45+margin_2, y=50)

        self.node_2_ahok_count = Entry(self.main_frame, width=40)
        self.node_2_ahok_count.place(x=100+margin_2, y=50)

        self.anies_label_2 = Label(text="Cand #2")
        self.anies_label_2.place(x=45+margin_2, y=76)

        self.node_2_anies_count = Entry(self.main_frame, width=40)
        self.node_2_anies_count.place(x=100+margin_2, y=76)

        self.prev_label_2 = Label(text="Hash #1")
        self.prev_value_2 = Text(self.main_frame, width=30, height=3)
        self.prev_label_2.place(x=50+margin_2,  y=102)
        self.prev_value_2.place(x=100+margin_2, y=102)

        height_hash = 162
        self.hash_label_2 = Label(text="Hash")
        self.hash_value_2 = Text(self.main_frame, width=30, height=3)
        self.hash_label_2.place(x=60 + margin_2,  y=height_hash)
        self.hash_value_2.place(x=100 + margin_2, y=height_hash)

        self.key_label = Label(text="Key")
        self.node_2_key_value = Text(self.main_frame, width=30, height=3)
        self.key_label.place(x=60 + margin_2, y=height_key)
        self.node_2_key_value.place(x=100 + margin_2, y=height_key)
        self.node_2_key_value.insert(END,open("certificate/private_2.pem").read())

        self.hash_meth_2 = Button(self.main_frame, text="Hash", command=lambda: self.get_hash(node=2), width=9, height=1)
        self.send_meth_2 = Button(self.main_frame, text="Broadcast", command=lambda: self.broadcast_hash(node_dest=3), width=9, height=1)
        self.disb_node_2 = Button(self.main_frame, text="Disable", command=lambda: self.disable_node(node=2, sync=False), fg='white', bg='#91181e', width=9, height=1)
        self.disb_node_2.place(x=270 + margin_2, y=height_button)
        self.hash_meth_2.place(x=100+margin_2, y=height_button)
        self.send_meth_2.place(x=185+margin_2, y=height_button)

        ''' NODE #3 widget declaration'''

        margin_3 = margin_2*2+30

        labelframe = LabelFrame(self.main_frame, text="NODE #3", width=330, height=height_frame)
        labelframe.place(x=40 + margin_3, y=20)

        self.ahok_label_3 = Label(text="Cand #1")
        self.ahok_label_3.place(x=45 + margin_3, y=50)

        self.node_3_ahok_count = Entry(self.main_frame, width=40)
        self.node_3_ahok_count.place(x=100 + margin_3, y=50)

        self.anies_label_3 = Label(text="Cand #2")
        self.anies_label_3.place(x=45 + margin_3, y=76)

        self.node_3_anies_count = Entry(self.main_frame, width=40)
        self.node_3_anies_count.place(x=100 + margin_3, y=76)

        self.prev_label_3 = Label(text="Hash #2")
        self.prev_value_3 = Text(self.main_frame, width=30, height=3)
        self.prev_label_3.place(x=50 + margin_3, y=102)
        self.prev_value_3.place(x=100 + margin_3, y=102)

        height_hash = 162
        self.hash_label_3 = Label(text="Hash")
        self.hash_value_3 = Text(self.main_frame, width=30, height=3)
        self.hash_label_3.place(x=60 + margin_3, y=height_hash)
        self.hash_value_3.place(x=100 + margin_3, y=height_hash)

        self.key_label = Label(text="Key")
        self.node_3_key_value = Text(self.main_frame, width=30, height=3)
        self.key_label.place(x=60 + margin_3, y=height_key)
        self.node_3_key_value.place(x=100 + margin_3, y=height_key)
        self.node_3_key_value.insert(END,open("certificate/private_3.pem").read())

        self.hash_meth_3 = Button(self.main_frame, text="Hash", command=lambda: self.get_hash(node=3), width=9, height=1)
        self.send_meth_3 = Button(self.main_frame, text="Broadcast", command=lambda: self.broadcast_hash(node_dest=4), width=9, height=1)
        self.disb_node_3 = Button(self.main_frame, text="Disable", command=lambda: self.disable_node(node=3, sync=False), fg='white', bg='#91181e', width=9, height=1)
        self.disb_node_3.place(x=270 + margin_3, y=height_button)
        self.hash_meth_3.place(x=100 + margin_3, y=height_button)
        self.send_meth_3.place(x=185 + margin_3, y=height_button)

        ''' NODE #4 widget declaration'''

        margin_4 = margin_2*3+60

        labelframe = LabelFrame(self.main_frame, text="NODE #4", width=330, height=height_frame)
        labelframe.place(x=40 + margin_4, y=20)

        self.ahok_label_4 = Label(text="Cand #1")
        self.ahok_label_4.place(x=45 + margin_4, y=50)

        self.node_4_ahok_count = Entry(self.main_frame, width=40)
        self.node_4_ahok_count.place(x=100 + margin_4, y=50)

        self.anies_label_4 = Label(text="Cand #2")
        self.anies_label_4.place(x=45 + margin_4, y=76)

        self.node_4_anies_count = Entry(self.main_frame, width=40)
        self.node_4_anies_count.place(x=100 + margin_4, y=76)

        self.prev_label_4 = Label(text="Hash #3")
        self.prev_value_4 = Text(self.main_frame, width=30, height=3)
        self.prev_label_4.place(x=50 + margin_4, y=102)
        self.prev_value_4.place(x=100 + margin_4, y=102)

        height_hash = 162
        self.hash_label_4 = Label(text="Hash")
        self.hash_value_4 = Text(self.main_frame, width=30, height=3)
        self.hash_label_4.place(x=60 + margin_4, y=height_hash)
        self.hash_value_4.place(x=100 + margin_4, y=height_hash)

        self.key_label = Label(text="Key")
        self.node_4_key_value = Text(self.main_frame, width=30, height=3)
        self.key_label.place(x=60 + margin_4, y=height_key)
        self.node_4_key_value.place(x=100+margin_4, y=height_key)
        self.node_4_key_value.insert(END,open("certificate/private_4.pem").read())

        self.hash_meth_4 = Button(self.main_frame, text="Hash", command=lambda: self.get_hash(node=4), width=9, height=1)
        self.send_meth_4 = Button(self.main_frame, text="Broadcast", command=lambda: self.broadcast_hash(node_dest=5), width=9, height=1)
        self.disb_node_4 = Button(self.main_frame, text="Disable", command=lambda: self.disable_node(node=4, sync=False), fg='white', bg='#91181e', width=9, height=1)
        self.disb_node_4.place(x=270 + margin_4, y=height_button)
        self.hash_meth_4.place(x=100 + margin_4, y=height_button)
        self.send_meth_4.place(x=185 + margin_4, y=height_button)

        # self.scroll_bar.config(command=self.main_frame.xview())

        '''Database Layout'''

        database_header_height = 370
        header_height = 400

        Label(text="Database Node #1").place(x=node_1_margin_x, y=database_header_height)
        Label(text="Cand #1").place(x=237, y=header_height)
        Label(text="Cand #2").place(x=290, y=header_height)

        Label(text="Verification check : ").place(x=node_1_margin_x, y=header_height)
        self.verif_label_1 = Label(text="-")
        self.verif_label_1.place(x=110 + node_1_margin_x, y=header_height)

        Label(text="DB size : ").place(x=node_1_margin_x, y=header_height+190)
        self.db_size = Label(text="-")
        self.db_size.place(x=50 + node_1_margin_x, y=header_height+190)
        Label(text="bytes").place(x=node_1_margin_x + 85, y=header_height + 190)


        node_1_y_level = 430
        node_1_x_level_one = 240
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = 180

        self.node_1_db = Text(self.main_frame, width=32, height=12, font=self.my_font)
        self.node_1_db.place(x=node_1_margin_x, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_1_db_ahok_1 = Entry(self.main_frame, width=7)
        self.node_1_db_ahok_1.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_1_db_anies_1 = Entry(self.main_frame, width=7)
        self.node_1_db_anies_1.place(x=node_1_x_level_two, y=node_1_y_level)

        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_1_db_ahok_2 = Entry(self.main_frame, width=7)
        self.node_1_db_ahok_2.place(x=node_1_x_level_one, y=node_2_level)
        self.node_1_db_anies_2 = Entry(self.main_frame, width=7)
        self.node_1_db_anies_2.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_1_db_ahok_3 = Entry(self.main_frame, width=7)
        self.node_1_db_ahok_3.place(x=node_1_x_level_one, y=node_3_level)
        self.node_1_db_anies_3 = Entry(self.main_frame, width=7)
        self.node_1_db_anies_3.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_1_db_ahok_4 = Entry(self.main_frame, width=7)
        self.node_1_db_ahok_4.place(x=node_1_x_level_one, y=node_4_level)
        self.node_1_db_anies_4 = Entry(self.main_frame, width=7)
        self.node_1_db_anies_4.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_1_db_ahok_total = Entry(self.main_frame, width=7)
        self.node_1_db_ahok_total.place(x=node_1_x_level_one, y=node_5_level)
        self.node_1_db_anies_total = Entry(self.main_frame, width=7)
        self.node_1_db_anies_total.place(x=node_1_x_level_two, y=node_5_level)

        ''' ################### NODE 2 ################### '''

        add_margin = 340

        Label(text="Database Node #2").place(x=350, y=database_header_height)
        Label(text="Cand #1").place(x=235+add_margin, y=header_height)
        Label(text="Cand #2").place(x=290+add_margin, y=header_height)

        Label(text="Verification check : ").place(x=350, y=header_height)
        self.verif_label_2 = Label(text="-")
        self.verif_label_2.place(x=120 + add_margin, y=header_height)

        node_1_x_level_one = 240+add_margin
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = node_1_x_level_one - 60

        self.node_2_db = Text(self.main_frame, width=32, height=12, font=self.my_font)
        self.node_2_db.place(x=10+add_margin, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_2_db_ahok_1 = Entry(self.main_frame, width=7)
        self.node_2_db_ahok_1.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_2_db_anies_1 = Entry(self.main_frame, width=7)
        self.node_2_db_anies_1.place(x=node_1_x_level_two, y=node_1_y_level)

        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_2_db_ahok_2 = Entry(self.main_frame, width=7)
        self.node_2_db_ahok_2.place(x=node_1_x_level_one, y=node_2_level)
        self.node_2_db_anies_2 = Entry(self.main_frame, width=7)
        self.node_2_db_anies_2.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_2_db_ahok_3 = Entry(self.main_frame, width=7)
        self.node_2_db_ahok_3.place(x=node_1_x_level_one, y=node_3_level)
        self.node_2_db_anies_3 = Entry(self.main_frame, width=7)
        self.node_2_db_anies_3.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_2_db_ahok_4 = Entry(self.main_frame, width=7)
        self.node_2_db_ahok_4.place(x=node_1_x_level_one, y=node_4_level)
        self.node_2_db_anies_4 = Entry(self.main_frame, width=7)
        self.node_2_db_anies_4.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_2_db_ahok_total = Entry(self.main_frame, width=7)
        self.node_2_db_ahok_total.place(x=node_1_x_level_one, y=node_5_level)
        self.node_2_db_anies_total = Entry(self.main_frame, width=7)
        self.node_2_db_anies_total.place(x=node_1_x_level_two, y=node_5_level)

        ''' ################### NODE 3 ################### '''

        add_margin = 340+340

        Label(text="Database Node #3").place(x=10+add_margin, y=database_header_height)
        Label(text="Cand #1").place(x=235+add_margin, y=header_height)
        Label(text="Cand #2").place(x=290+add_margin, y=header_height)

        Label(text="Verification check : ").place(x=10+add_margin, y=header_height)
        self.verif_label_3 = Label(text="-")
        self.verif_label_3.place(x=120 + add_margin, y=header_height)

        node_1_x_level_one = 240+add_margin
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = node_1_x_level_one - 60

        self.node_3_db = Text(self.main_frame, width=32, height=12, font=self.my_font)
        self.node_3_db.place(x=10+add_margin, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_3_db_ahok_1 = Entry(self.main_frame, width=7)
        self.node_3_db_ahok_1.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_3_db_anies_1 = Entry(self.main_frame, width=7)
        self.node_3_db_anies_1.place(x=node_1_x_level_two, y=node_1_y_level)

        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_3_db_ahok_2 = Entry(self.main_frame, width=7)
        self.node_3_db_ahok_2.place(x=node_1_x_level_one, y=node_2_level)
        self.node_3_db_anies_2 = Entry(self.main_frame, width=7)
        self.node_3_db_anies_2.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_3_db_ahok_3 = Entry(self.main_frame, width=7)
        self.node_3_db_ahok_3.place(x=node_1_x_level_one, y=node_3_level)
        self.node_3_db_anies_3 = Entry(self.main_frame, width=7)
        self.node_3_db_anies_3.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_3_db_ahok_4 = Entry(self.main_frame, width=7)
        self.node_3_db_ahok_4.place(x=node_1_x_level_one, y=node_4_level)
        self.node_3_db_anies_4 = Entry(self.main_frame, width=7)
        self.node_3_db_anies_4.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_3_db_ahok_total = Entry(self.main_frame, width=7)
        self.node_3_db_ahok_total.place(x=node_1_x_level_one, y=node_5_level)
        self.node_3_db_anies_total = Entry(self.main_frame, width=7)
        self.node_3_db_anies_total.place(x=node_1_x_level_two, y=node_5_level)

        ''' ################### NODE 4 ################### '''

        add_margin = 340+340+340

        Label(text="Database Node #4").place(x=10+add_margin, y=database_header_height)
        Label(text="Cand #1").place(x=235+add_margin, y=header_height)
        Label(text="Cand #2").place(x=290+add_margin, y=header_height)

        Label(text="Verification check : ").place(x=10+add_margin, y=header_height)
        self.verif_label_4 = Label(text="-")
        self.verif_label_4.place(x=120+add_margin, y=header_height)

        node_1_x_level_one = 240+add_margin
        node_1_x_level_two = node_1_x_level_one + 50
        node_index_label = node_1_x_level_one - 60

        self.node_4_db = Text(self.main_frame, width=32, height=12, font=self.my_font)
        self.node_4_db.place(x=10+add_margin, y=node_1_y_level)

        Label(text="Node#1").place(x=node_index_label, y=node_1_y_level)
        self.node_4_db_ahok_1 = Entry(self.main_frame, width=7)
        self.node_4_db_ahok_1.place(x=node_1_x_level_one, y=node_1_y_level)
        self.node_4_db_anies_1 = Entry(self.main_frame, width=7)
        self.node_4_db_anies_1.place(x=node_1_x_level_two, y=node_1_y_level)

        node_2_level = node_1_y_level + 30
        Label(text="Node#2").place(x=node_index_label, y=node_2_level)
        self.node_4_db_ahok_2 = Entry(self.main_frame, width=7)
        self.node_4_db_ahok_2.place(x=node_1_x_level_one, y=node_2_level)
        self.node_4_db_anies_2 = Entry(self.main_frame, width=7)
        self.node_4_db_anies_2.place(x=node_1_x_level_two, y=node_2_level)

        node_3_level = node_2_level + 30
        Label(text="Node#3").place(x=node_index_label, y=node_3_level)
        self.node_4_db_ahok_3 = Entry(self.main_frame, width=7)
        self.node_4_db_ahok_3.place(x=node_1_x_level_one, y=node_3_level)
        self.node_4_db_anies_3 = Entry(self.main_frame, width=7)
        self.node_4_db_anies_3.place(x=node_1_x_level_two, y=node_3_level)

        node_4_level = node_3_level + 30
        Label(text="Node#4").place(x=node_index_label, y=node_4_level)
        self.node_4_db_ahok_4 = Entry(self.main_frame, width=7)
        self.node_4_db_ahok_4.place(x=node_1_x_level_one, y=node_4_level)
        self.node_4_db_anies_4 = Entry(self.main_frame, width=7)
        self.node_4_db_anies_4.place(x=node_1_x_level_two, y=node_4_level)

        node_5_level = node_4_level + 30
        Label(text="Total", fg='Blue').place(x=node_index_label, y=node_5_level)
        self.node_4_db_ahok_total = Entry(self.main_frame, width=7)
        self.node_4_db_ahok_total.place(x=node_1_x_level_one, y=node_5_level)
        self.node_4_db_anies_total = Entry(self.main_frame, width=7)
        self.node_4_db_anies_total.place(x=node_1_x_level_two, y=node_5_level)

        ''' counter view '''

        self.count_label = Label(text="-", font=("Helvetica", 30))
        self.count_label.place(x=1040, y=540 + 100)
        self.remaining = 0
        self.iter = 0
        self.node_down = []
        self.last_validated = ''
        self.flag = None

        Button(text='Generate Data', width=15, height=2, bg='#f8c659', command=self.generate_data).place(x=node_1_margin_x, y=node_5_level+100)
        Button(text='Sync Data', width=15, height=2, bg='#f8c659', command= lambda: self.countdown(3)).place(x=node_1_margin_x+120, y=node_5_level + 100)
        Button(text='Clear DB', width=15, height=2, bg='#f8c659', command= self.clear_interface).place(x=node_1_margin_x+240, y=node_5_level + 100)

        ''' clear DB '''
        self.clear_db()

    def get_hash(self, node):
        if node == 1:
            val = self.gen_value.get("1.0", 'end-2c') + ',' + self.node_1_ahok_count.get() + ',' + self.node_1_anies_count.get()
            # print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            # print(hash_hex)
            self.hash_value.delete("1.0", END)
            self.hash_value.insert(END, hash_hex)
        if node == 2:
            val = self.prev_value_2.get("1.0", 'end-2c') + ',' + self.node_2_ahok_count.get() + ',' + self.node_2_anies_count.get()
            # print(val)
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_2.delete("1.0", END)
            self.hash_value_2.insert(END, hash_hex)
        if node == 3:
            val = self.prev_value_3.get("1.0", 'end-2c') + ',' + self.node_3_ahok_count.get() + ',' + self.node_3_anies_count.get()
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_3.delete("1.0", END)
            self.hash_value_3.insert(END, hash_hex)
        if node == 4:
            val = self.prev_value_4.get("1.0", 'end-2c') + ',' + self.node_4_ahok_count.get() + ',' + self.node_4_anies_count.get()
            string_bytes = bytes(val, 'utf-8')
            hash_data = hashlib.sha256(string_bytes)
            hash_hex = hash_data.hexdigest()
            self.hash_value_4.delete("1.0",END)
            self.hash_value_4.insert(END, hash_hex)

    def broadcast_hash(self, node_dest):

        if node_dest == 2:
            source_hash = self.hash_value
            prev_hash_value = self.gen_value
            ahok_count = self.node_1_ahok_count
            anies_count = self.node_1_anies_count
            key = self.node_1_key_value.get('1.0', 'end-1c')

            list_db_ahok = [self.node_1_db_ahok_1, self.node_2_db_ahok_1, self.node_3_db_ahok_1, self.node_4_db_ahok_1]
            list_db_anies = [self.node_1_db_anies_1, self.node_2_db_anies_1, self.node_3_db_anies_1, self.node_4_db_anies_1]

        if node_dest == 3:
            source_hash = self.hash_value_2
            prev_hash_value = self.prev_value_2
            ahok_count = self.node_2_ahok_count
            anies_count = self.node_2_anies_count
            key = self.node_2_key_value.get('1.0', 'end-1c')

            list_db_ahok = [self.node_1_db_ahok_2, self.node_2_db_ahok_2, self.node_3_db_ahok_2, self.node_4_db_ahok_2]
            list_db_anies = [self.node_1_db_anies_2, self.node_2_db_anies_2, self.node_3_db_anies_2, self.node_4_db_anies_2]

        if node_dest == 4:
            source_hash = self.hash_value_3
            prev_hash_value = self.prev_value_3
            ahok_count = self.node_3_ahok_count
            anies_count = self.node_3_anies_count
            key = self.node_3_key_value.get('1.0', 'end-1c')

            list_db_ahok = [self.node_1_db_ahok_3, self.node_2_db_ahok_3, self.node_3_db_ahok_3, self.node_4_db_ahok_3]
            list_db_anies = [self.node_1_db_anies_3, self.node_2_db_anies_3, self.node_3_db_anies_3, self.node_4_db_anies_3]

        if node_dest == 5:
            ahok_count = self.node_4_ahok_count
            anies_count = self.node_4_anies_count
            key = self.node_4_key_value.get('1.0', 'end-1c')
            source_hash = self.hash_value_4
            prev_hash_value = self.prev_value_4

            list_db_ahok = [self.node_1_db_ahok_4, self.node_2_db_ahok_4, self.node_3_db_ahok_4, self.node_4_db_ahok_4]
            list_db_anies = [self.node_1_db_anies_4, self.node_2_db_anies_4, self.node_3_db_anies_4, self.node_4_db_anies_4]

        ''' lock data '''
        elements = [source_hash, prev_hash_value, ahok_count,anies_count]
        for element in elements:
            element.configure(state=DISABLED, bg='#F0F0F0')

        ''' security verification '''
        verif_stat = self.verification(key, node_dest)

        if verif_stat == True:
            ''' precheck database '''
            with open('database/database_node1.csv') as csvfile:
                pointer_data = csv.reader(csvfile, delimiter=',')
                data = list(pointer_data)

            is_duplicated = False
            z=0
            if len(data) != 0 :
                while z < len(data):
                    if data[z][0] == 'id: Database{}'.format(node_dest-1):
                        is_duplicated = True
                        print('Data dari Node {} sudah terdaftar'.format(node_dest-1))
                    z += 1
            print('pre check database done')

            ''' broadcast data prev Hash '''
            list_node = [2, 3, 4]
            if node_dest in list_node :
                prev_hash_frames = [self.prev_value_2, self.prev_value_3, self.prev_value_4]
                for frame in prev_hash_frames:
                    hash_value = source_hash.get(1.0, END)
                    frame.delete("1.0", END)
                    frame.insert(END, hash_value)
            print('broadcast to other node done')
            ''' populate data to database UI '''
            for db in list_db_ahok:
                db.delete("0", END)
                db.insert(END, ahok_count.get())

            for db in list_db_anies:
                db.delete("0", END)
                db.insert(END, anies_count.get())
            print('populate database to UI done')

            ''' create signature '''
            data_hash = source_hash.get('1.0',END)
            data_hash_uni = data_hash.encode('utf-8')
            sk = SigningKey.from_pem(open('certificate/private_{}.pem'.format(node_dest-1)).read())
            sig = sk.sign(data_hash_uni)  ### result with /x /x
            sig = binascii.hexlify(sig)   ### hex readeble
            print('create signature done')

            ''' store data to real DB'''
            self.store_data(node_dest-1, prev_hash_value.get('1.0', 'end-2c'),
                            ahok_count.get(), anies_count.get(), sig)

            ''' save to database '''
            if is_duplicated == False :
                i=1
                while i < 5 :
                    with open('database/database_node{}.csv'.format(i), 'a', newline='') as csvfile:
                        write_csv = csv.writer(csvfile, delimiter = ',')
                        write_csv.writerow(['sourceId: Node {}'.format(node_dest-1),
                                            'nextNode: Node {}'.format(node_dest),
                                            'previous hash: {}'.format(prev_hash_value.get('1.0','end-2c')),
                                            'signature: {}'.format(sig),
                                            'candidate 1: {}'.format(ahok_count.get()),
                                            'candidate 2: {}'.format(anies_count.get()),
                                            'timestamp: {}'.format(datetime.now())])
                    i+=1
                print('save to database done')

        ''' counting data '''
        self.counting_data()

        ''' populate to database UI '''
        self.populate_database()

        ''' check db size '''
        self.check_db_size()

    def generate_data(self):

        frame_list_ahok = [self.node_1_ahok_count, self.node_2_ahok_count, self.node_3_ahok_count, self.node_4_ahok_count]
        frame_list_anies = [self.node_1_anies_count, self.node_2_anies_count, self.node_3_anies_count, self.node_4_anies_count]

        for candidates in zip(frame_list_ahok, frame_list_anies) :
            for candidate in candidates :
                candidate.delete("0", END)
                candidate.insert(END, randint(20,200))

    def counting_data(self):
        ''' counting data '''

        try:
            node_1_count_ahok = int(self.node_1_db_ahok_1.get())
            node_1_count_anies = int(self.node_1_db_anies_1.get())
        except ValueError:
            node_1_count_ahok = 0
            node_1_count_anies = 0

        try:
            node_2_count_ahok = int(self.node_1_db_ahok_2.get())
            node_2_count_anies = int(self.node_1_db_anies_2.get())
        except ValueError:
            node_2_count_ahok = 0
            node_2_count_anies = 0

        try:
            node_3_count_ahok = int(self.node_1_db_ahok_3.get())
            node_3_count_anies = int(self.node_1_db_anies_3.get())
        except ValueError:
            node_3_count_ahok = 0
            node_3_count_anies = 0

        try:
            node_4_count_ahok = int(self.node_1_db_ahok_4.get())
            node_4_count_anies = int(self.node_1_db_anies_4.get())
        except ValueError:
            node_4_count_ahok = 0
            node_4_count_anies = 0

        total_ahok = node_1_count_ahok + node_2_count_ahok + node_3_count_ahok + node_4_count_ahok
        total_anies = node_1_count_anies + node_2_count_anies + node_3_count_anies + node_4_count_anies

        total_ahok_frame = [self.node_1_db_ahok_total,
                            self.node_2_db_ahok_total,
                            self.node_3_db_ahok_total,
                            self.node_4_db_ahok_total]

        total_anies_frame = [self.node_1_db_anies_total,
                             self.node_2_db_anies_total,
                             self.node_3_db_anies_total,
                             self.node_4_db_anies_total]

        # totals_frame = [total_ahok_frame, total_anies_frame]

        for db in total_ahok_frame:
            db.delete("0", END)
            db.insert(END, total_ahok)

        for db in total_anies_frame:
            db.delete("0", END)
            db.insert(END, total_anies)

    def read_database(self):
        list_database = ["database/database_node1.csv",
                         "database/database_node2.csv",
                         "database/database_node3.csv",
                         "database/database_node4.csv"]
        data_shell = []
        for database in list_database :
            with open(database) as voting_database :
                voting_data = csv.reader(voting_database, delimiter=',')
                data_shell.append(list(voting_data))


        return data_shell

    def populate_database(self):
        voting_data = list(self.read_database())  # read across all database
        # print(voting_data)
        dbf_lists = [self.node_1_db, self.node_2_db, self.node_3_db, self.node_4_db]
        for dbf in dbf_lists:
            dbf.delete("1.0", END)

        i = 0
        while i < len(voting_data[0]):
            db_instance_data = voting_data[0][i]
            # print(db_instance_data)
            x = 0
            while x < len(db_instance_data):
                if x != 0:
                    for dbf in dbf_lists:
                        dbf.insert(END, '\n')
                for dbf in dbf_lists:
                    dbf.insert(END, db_instance_data[x])

                if x == 6:  ### WARNING ! if data that stored in database change it should be change
                    for dbf in dbf_lists:
                        dbf.insert(END, '\n')
                        dbf.insert(END, "################################")
                        dbf.see(END)
                x += 1
            i += 1

    def disable_node(self, node, sync = False):

        if node == 1:
            ahok_count = self.node_1_ahok_count
            anies_count = self.node_1_anies_count
            prev_hash = self.gen_value
            hash_rslt = self.hash_value
            key = self.node_1_key_value
            send = self.send_meth
            hash = self.hash_meth
            dsb_button = self.disb_node

        if node == 2:
            ahok_count = self.node_2_ahok_count
            anies_count = self.node_2_anies_count
            prev_hash = self.prev_value_2
            hash_rslt = self.hash_value_2
            key = self.node_2_key_value
            send = self.send_meth_2
            hash = self.hash_meth_2
            dsb_button = self.disb_node_2

        if node == 3:
            ahok_count = self.node_3_ahok_count
            anies_count = self.node_3_anies_count
            prev_hash = self.prev_value_3
            hash_rslt = self.hash_value_3
            key = self.node_3_key_value
            send = self.send_meth_3
            hash = self.hash_meth_3
            dsb_button = self.disb_node_3

        if node == 4:
            ahok_count = self.node_4_ahok_count
            anies_count = self.node_4_anies_count
            prev_hash = self.prev_value_4
            hash_rslt = self.hash_value_4
            key = self.node_4_key_value
            send = self.send_meth_4
            hash = self.hash_meth_4
            dsb_button = self.disb_node_4

        form_elements = [ahok_count, anies_count, prev_hash, hash_rslt]
        button_elements = [send, hash, key]

        if send['state'] == "normal" :
            for element in form_elements:
                element.configure(state=DISABLED, bg="#F0F0F0")
            if sync == False:
                for element in button_elements:
                    element.configure(state=DISABLED)
                dsb_button.configure(text='Enable', bg='green')
                return

        if send['state'] == "disabled" :
            for element in form_elements:
                element.configure(state=NORMAL, bg="#FFFFFF")
            for element in button_elements:
                element.configure(state=NORMAL)
            dsb_button.configure(text='Disable', bg='#91181e')
            print("jadi aktif")
            return

    def countdown(self, remaining = None, iter=None):

        nodes_state = [self.send_meth['state'], self.send_meth_2['state'], self.send_meth_3['state'], self.send_meth_4['state']]

        db_ahok_1 = [self.node_1_db_ahok_1, self.node_2_db_ahok_1, self.node_3_db_ahok_1, self.node_4_db_ahok_1]
        db_ahok_2 = [self.node_1_db_ahok_2, self.node_2_db_ahok_2, self.node_3_db_ahok_2, self.node_4_db_ahok_2]
        db_ahok_3 = [self.node_1_db_ahok_3, self.node_2_db_ahok_3, self.node_3_db_ahok_3, self.node_4_db_ahok_3]
        db_ahok_4 = [self.node_1_db_ahok_4, self.node_2_db_ahok_4, self.node_3_db_ahok_4, self.node_4_db_ahok_4]

        db_anies_1 = [self.node_1_db_anies_1, self.node_2_db_anies_1, self.node_3_db_anies_1, self.node_4_db_anies_1]
        db_anies_2 = [self.node_1_db_anies_2, self.node_2_db_anies_2, self.node_3_db_anies_2, self.node_4_db_anies_2]
        db_anies_3 = [self.node_1_db_anies_3, self.node_2_db_anies_3, self.node_3_db_anies_3, self.node_4_db_anies_3]
        db_anies_4 = [self.node_1_db_anies_4, self.node_2_db_anies_4, self.node_3_db_anies_4, self.node_4_db_anies_4]

        source_data_ahok = [self.node_1_ahok_count.get(), self.node_2_ahok_count.get(), self.node_3_ahok_count.get(), self.node_4_ahok_count.get()]
        source_data_anies = [self.node_1_anies_count.get(), self.node_2_anies_count.get(), self.node_3_anies_count.get(), self.node_4_anies_count.get()]

        prev_hash_frames = [self.gen_value,self.prev_value_2, self.prev_value_3, self.prev_value_4]
        source_hash_frames = [self.hash_value, self.hash_value_2, self.hash_value_3, self.hash_value_4]

        node_keys = [self.node_1_key_value, self.node_2_key_value, self.node_3_key_value, self.node_4_key_value]

        list_db_ahok = [db_ahok_1, db_ahok_2, db_ahok_3, db_ahok_4]
        list_db_anies = [db_anies_1, db_anies_2, db_anies_3, db_anies_4]

        if remaining is not None:
            self.remaining = remaining

        if iter is not None:
            self.iter = iter

        if self.remaining <= 0:
            self.count_label.configure(text="Broadcast node")

            ''' verification '''
            key = node_keys[self.iter].get('1.0', 'end-1c')
            verif = self.verification(key,self.iter+2)

            self.get_hash(node=self.iter + 1)

            ''' UI populate'''
            if nodes_state[self.iter] == 'disabled' or verif == False:  ### block color with red
                if nodes_state[self.iter] == 'disabled':
                    verif_labels = [self.verif_label_1, self.verif_label_2, self.verif_label_3, self.verif_label_4]
                    for label in verif_labels:
                        label.configure(text='data not received', fg='white', bg='Red')

                for db in list_db_ahok[self.iter]:
                    db.delete('0', END)
                    db.configure(bg='red')

                for db in list_db_anies[self.iter]:
                    db.delete('0', END)
                    db.configure(bg='red')

                print("disini nge populate merah")
                self.node_down.append(self.iter+1)

            else:
                for db in list_db_ahok[self.iter] :             ### broadcast to database
                    db.delete('0',END)
                    db.insert(END, source_data_ahok[self.iter])
                    db.configure(bg='green', fg='white')

                for db in list_db_anies[self.iter] :
                    db.delete('0',END)
                    db.insert(END, source_data_anies[self.iter])
                    db.configure(bg='green', fg='white')

                self.get_hash(node=self.iter+1)
                self.disable_node(node=self.iter+1, sync=TRUE)

                for frame in prev_hash_frames:                  ### broadcast to node frame
                    frame.delete('1.0',END)
                    frame.insert(END,source_hash_frames[self.iter].get('1.0',END))

                self.counting_data()

                ''' create signature '''
                data_hash = source_hash_frames[self.iter].get('1.0', END)
                data_hash_uni = data_hash.encode('utf-8')
                sk = SigningKey.from_pem(open('certificate/private_{}.pem'.format(self.iter + 1)).read())
                sig = sk.sign(data_hash_uni)  ### result with /x /x
                sig = binascii.hexlify(sig)  ### hex readeble


                ''' real store db'''
                print("save to DB")
                self.store_data(self.iter + 1,
                                prev_hash_frames[self.iter].get("1.0","end-2c"),
                                source_data_ahok[self.iter],
                                source_data_anies[self.iter],
                                sig)

                ''' save to database '''
                i = 1
                while i < 5:
                    with open('database/database_node{}.csv'.format(i), 'a', newline='') as csvfile:
                        write_csv = csv.writer(csvfile, delimiter=',')
                        write_csv.writerow(['sourceId: Node {}'.format(self.iter + 1),
                                            'nextNode: Node {}'.format(self.iter + 2),
                                            'prev hash: {}'.format(self.get_last_hash()),
                                            'signature: {}'.format(sig),
                                            'ahok: {}'.format(source_data_ahok[self.iter]),
                                            'anies: {}'.format(source_data_anies[self.iter]),
                                            'timestamp: {}'.format(time.time())])
                    i += 1

                ''' populate to database UI '''
                self.populate_database()

                ''' check db size '''
                self.check_db_size()

            self.remaining = 3
            y = self.iter+1
            if self.iter == 3:
                self.count_label.configure(text="broadcast done")
                return

            self.root.after(1000, lambda: self.countdown(remaining=self.remaining, iter=y))

        else:
            self.count_label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.root.after(1000, self.countdown)
            # print(self.iter)

        # print(self.node_down)

    def clear_db(self):
        ''' clean db file '''
        list_db = ["database/database_node1.csv",
                   "database/database_node2.csv",
                   "database/database_node3.csv",
                   "database/database_node4.csv"]

        for db in list_db:
            open(db, 'w').close()

        ''' clear db real '''
        try:
            conn = sqlite3.connect('database/node_1_db.db')
            c = conn.cursor()
            c.execute('DELETE FROM votingDataDB')
            conn.commit()
        except sqlite3.OperationalError:
            print("init Database")

        ''' get db size '''
        self.check_db_size()

    def clear_interface(self):

        self.check_db_size()
        self.clear_db()

        ''' clean db raw view '''
        dbf_lists = [self.node_1_db, self.node_2_db, self.node_3_db, self.node_4_db]
        for dbf in dbf_lists:
            dbf.delete("1.0", END)

        ''' clear node count'''
        count_frames = [self.node_1_anies_count, self.node_2_anies_count, self.node_3_anies_count, self.node_4_anies_count,
                       self.node_1_ahok_count, self.node_2_ahok_count, self.node_3_ahok_count, self.node_4_ahok_count]
        for frame in count_frames:
            frame.configure(state=NORMAL, bg='#FFFFFF', fg='black')
            frame.delete('0',END)

        ''' clear hash'''
        hash_frame = [self.hash_value, self.hash_value_2, self.hash_value_3, self.hash_value_4,
                      self.prev_value_2, self.prev_value_3, self.prev_value_4]
        for frame in hash_frame:
            frame.configure(state=NORMAL, bg='#FFFFFF', fg='black')
            frame.delete('1.0',END)

        ''' clear db instance '''
        db_frames_1 = [self.node_1_db_ahok_1, self.node_1_db_ahok_2, self.node_1_db_ahok_3, self.node_1_db_ahok_4,
                       self.node_2_db_ahok_1, self.node_2_db_ahok_2, self.node_2_db_ahok_3, self.node_2_db_ahok_4,
                       self.node_3_db_ahok_1, self.node_3_db_ahok_2, self.node_3_db_ahok_3, self.node_3_db_ahok_4,
                       self.node_4_db_ahok_1, self.node_4_db_ahok_2, self.node_4_db_ahok_3, self.node_4_db_ahok_4,
                       self.node_1_db_ahok_total, self.node_2_db_ahok_total, self.node_3_db_ahok_total,
                       self.node_4_db_ahok_total]

        db_frames_2 = [self.node_1_db_anies_1, self.node_1_db_anies_2, self.node_1_db_anies_3, self.node_1_db_anies_4,
                       self.node_2_db_anies_1, self.node_2_db_anies_2, self.node_2_db_anies_3, self.node_2_db_anies_4,
                       self.node_3_db_anies_1, self.node_3_db_anies_2, self.node_3_db_anies_3, self.node_3_db_anies_4,
                       self.node_4_db_anies_1, self.node_4_db_anies_2, self.node_4_db_anies_3, self.node_4_db_anies_4,
                       self.node_1_db_anies_total, self.node_2_db_anies_total, self.node_3_db_anies_total,
                       self.node_4_db_anies_total]

        db_frames = [db_frames_1, db_frames_2]

        for db_frame in db_frames :
            for db in db_frame:
                db.delete('0', END)
                db.configure(bg='#FFFFFF')

        ''' clear verif '''
        verif_frame = [self.verif_label_1, self.verif_label_2, self.verif_label_3, self.verif_label_4]
        for verif in verif_frame:
            verif.configure(text='-', bg='#F0F0F0', fg='black')

        self.check_db_size()
        self.iter = 0

    def verification(self, key, node):

        input_certificate = key
        curr_node = node - 2
        verif_labels = [self.verif_label_1, self.verif_label_2, self.verif_label_3, self.verif_label_4]

        security_valid = False

        ''' key verification '''
        certificates = ['private_1.pem', 'private_2.pem', 'private_3.pem', 'private_4.pem']
        for certificate in certificates:
            with open('certificate/{}'.format(certificate)) as file:
                db_certificate = file.read()
                if input_certificate == db_certificate:
                    print("security OK")
                    security_valid = True
                    for label in verif_labels:
                        label.configure(text='Verification success', fg='white', bg='green')

        if security_valid == False:
            for label in verif_labels:
                label.configure(text='Unknown key', fg='white', bg='Red')
            return False

        ''' verificaton hash '''
        list_prev = [self.gen_value, self.prev_value_2, self.prev_value_3, self.prev_value_4]
        if curr_node == 0:
            print('always pass this is genesis')
            return True

        else:
            if self.get_last_hash() == list_prev[curr_node].get('1.0', 'end-2c'):
                print('PREV HASH VALID')
                return True
            else:
                print('PREV HASH VALUE NOT VALID')
                for label in verif_labels:
                    label.configure(text='Invalid prevhash', fg='white', bg='Red')
                return False

    def check_db_size(self):
        dbs = os.path.getsize('database/database_node1.csv')
        self.db_size.configure(text=dbs)

    def store_data(self, node, prev_hash, candidate1, candidate2, signature):
        date = time.time()
        conn = sqlite3.connect('database/node_1_db.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS votingDataDB('
                  'nodeID INT, '
                  'prevHash TEXT, '
                  'candidate1 INT, '
                  'candidate2 INT, '
                  'timestamp TEXT, '
                  'signature TEXT)')


        c.execute("INSERT INTO votingDataDB (nodeID, prevHash, candidate1, candidate2, timestamp, signature)"
                  "VALUES(?, ?, ?, ?, ?, ?)", (node, prev_hash, candidate1, candidate2, date, signature))
        # conn.execute("VACUUM")
        conn.commit()

    def get_last_hash(self):
        conn = sqlite3.connect('database/node_1_db.db')
        c = conn.cursor()
        c.execute('SELECT * FROM votingDataDB WHERE nodeID =(SELECT MAX(nodeID) FROM votingDataDB)')
        last_block = c.fetchall()[0]
        val = last_block[1] + ',' + str(last_block[2]) + ',' + str(last_block[3])
        string_bytes = bytes(val, 'utf-8')
        hash_data = hashlib.sha256(string_bytes)
        hash_hex = hash_data.hexdigest()
        return  hash_hex



root = Tk()
root.geometry("1372x720")
root.title('E-VOTING SIMULATION USING BLOCKCHAIN')
# root.resizable(width=False, height=False)
Pemilu(root)
root.mainloop()

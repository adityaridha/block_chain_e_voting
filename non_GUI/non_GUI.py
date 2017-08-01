import hashlib
import binascii
import time
import csv
import os
import subprocess
import sys
from colorama import init, Fore, Back, Style
from terminaltables import AsciiTable
from random import randint
from ecdsa import BadSignatureError
from ecdsa import SigningKey, VerifyingKey


init() #colorama init

def create_hash(prev_hash, cand1, cand2):
    val = prev_hash + cand1 + cand2
    string_bytes = bytes(val, 'utf-8')
    hash_data = hashlib.sha256(string_bytes)
    hash_hex = hash_data.hexdigest()
    return hash_hex

def create_signature(hash_data):
    data_hash_uni = hash_data.encode('utf-8')
    sk = SigningKey.from_pem(open('certificate/private_1.pem').read())
    sig = sk.sign(data_hash_uni)
    sig = binascii.hexlify(sig)
    return sig

def store_to_csv(block_data):
    with open('non_GUI/database_node.csv', 'a', newline='') as csvfile:
        write_csv = csv.writer(csvfile, delimiter=',')
        write_csv.writerow(block_data)

table_data = [["NodeID","PrevHash","Cand 1","Cand 2","Hash","Signature","TimeStamp"]]
prev_hash_list = []

open('non_GUI/database_node.csv', 'w').close()  ### clear database
try:
    node_count = input("Berapa jumlah block node yang ingin disimulasi: ")
    print ("Membuat block...")
    i=0
    jumlah_node = int(node_count)
except ValueError:
    print("Input must be an Integer")
    sys.exit()


start_time = time.time()
while i < jumlah_node:
    if i == 0:
        prev_hash="Genesis"
    else:
        prev_hash = prev_hash_list[i-1]

    nodeID = i+1
    cand_1 = str(randint(30, 99))
    cand_2 = str(randint(30, 99))
    hash_data = create_hash(prev_hash, cand_1, cand_2)
    prev_hash_list.append(hash_data)
    signature = create_signature(hash_data)
    time_stamp = int(time.time())
    block_data_to_db = [nodeID, prev_hash, cand_1, cand_2, signature, time_stamp]
    block_data_to_view = [nodeID, prev_hash, cand_1, cand_2, hash_data, str(signature), time_stamp] ### menampilkan hash unutk keperluan view aja
    table_data.append(block_data_to_view)
    store_to_csv(block_data_to_db)
    i+=1
end_time = time.time()
execution_time = end_time - start_time
dbs = os.path.getsize('non_GUI/database_node.csv')
table = AsciiTable(table_data)
print(table.table)
print("Database Size : {}".format(dbs))
print("average node data : {}".format(dbs/jumlah_node))
print("Creation Time : {} second".format(execution_time))
print("\n")
print(Fore.RED + "Creation data done, Do you want to manipulate the Database? [Y/N]")
open_db = input()
if open_db == 'Y' or open_db == 'y' :
    subprocess.run(["notepad","non_GUI/database_node.csv"])
else:
    print("Database not manipulated")

print("Start verification...")
start_time = time.time()
guess_hash_list = []
with open("non_GUI/database_node.csv") as f:
    list_data= csv.reader(f, delimiter=",")
    for node_id, data in enumerate(list_data):
        guess_hash = create_hash(data[1], data[2], data[3])
        hash_bytes = bytes(guess_hash, 'utf-8')
        sig = data[4]
        sig = bytes(sig[2:-1], 'utf-8')
        switch = True
        try :
            sig = binascii.unhexlify(sig)
        except binascii.Error:
            switch = False
            print("BAD SIGNATURE !! Node {} Corrupt...............".format(node_id+1))

        if switch == True:
            try:
                vk = VerifyingKey.from_pem(open("certificate\public_1.pem").read())
                vk.verify(sig, hash_bytes)
                print("good signature")
            except BadSignatureError:
                print("BAD SIGNATURE !! Node {} Corrupt...............".format(node_id+1))

end_time = time.time()
verif_time = end_time - start_time
print("Verification time : {}".format(verif_time))
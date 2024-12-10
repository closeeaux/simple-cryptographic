keysize = 16



import random
import string
import ctypes
from time import sleep
from datetime import datetime
import ctypes
import threading
import ast


import sys
import os

custom_lib_path = os.path.join(os.path.dirname(__file__), "lib")

if custom_lib_path not in sys.path:
    sys.path.append(custom_lib_path)

import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from tkinter import ttk, messagebox

class NOTIFYICONDATA(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint32),
        ("hWnd", ctypes.c_void_p),
        ("uID", ctypes.c_uint32),
        ("uFlags", ctypes.c_uint32),
        ("uCallbackMessage", ctypes.c_uint32),
        ("hIcon", ctypes.c_void_p),
        ("szTip", ctypes.c_wchar * 128),
        ("dwState", ctypes.c_uint32),
        ("dwStateMask", ctypes.c_uint32),
        ("szInfo", ctypes.c_wchar * 256),
        ("uTimeoutOrVersion", ctypes.c_uint32),
        ("szInfoTitle", ctypes.c_wchar * 64),
        ("dwInfoFlags", ctypes.c_uint32),
        ("guidItem", ctypes.c_ubyte * 16),
        ("hBalloonIcon", ctypes.c_void_p),
    ]

NIF_INFO = 0x10
NIIF_INFO = 0x01

def show_balloon_notification(title, message):
    shell32 = ctypes.windll.shell32
    nid = NOTIFYICONDATA()
    nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
    nid.hWnd = None
    nid.uID = 1
    nid.uFlags = NIF_INFO
    nid.szInfoTitle = title
    nid.szInfo = message
    nid.uTimeoutOrVersion = 10
    nid.dwInfoFlags = NIIF_INFO

    
    shell32.Shell_NotifyIconW(0x0, ctypes.byref(nid))
    shell32.Shell_NotifyIconW(0x1, ctypes.byref(nid)) 

    
    ctypes.windll.kernel32.Sleep(5000)  

   
    shell32.Shell_NotifyIconW(0x2, ctypes.byref(nid))

def show_message(title, message):
    thread = threading.Thread(target=show_balloon_notification, args=(title, message))
    thread.daemon = True
    thread.start()
    
    

NIF_INFO = 0x10
NIIF_INFO = 0x01

def show_message(title, message):
    shell32 = ctypes.windll.shell32
    user32 = ctypes.windll.user32
    
   
    nid = NOTIFYICONDATA()
    nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
    nid.hWnd = None  
    nid.uID = 1
    nid.uFlags = NIF_INFO
    nid.szInfoTitle = title
    nid.szInfo = message
    nid.uTimeoutOrVersion = 10  
    nid.dwInfoFlags = NIIF_INFO

   
    shell32.Shell_NotifyIconW(0x0, ctypes.byref(nid))
    shell32.Shell_NotifyIconW(0x1, ctypes.byref(nid))  
    

    shell32.Shell_NotifyIconW(0x2, ctypes.byref(nid))  
    
    
    
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")







letters = {
            "a": 1, 
            "b": 2,
            "c": 3, 
            "d": 4, 
            "e": 5,
            "f": 6, 
            "g": 7, 
            "h": 8, 
            "i": 9, 
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13, 
            "n": 14, 
            "o": 15, 
            "p": 16, 
            "q": 17, 
            "r": 18, 
            "s": 19,
            "t": 20, 
            "u": 21,
            "v": 22, 
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26, 
            "A": 41, 
            "B": 42,
            "C": 43, 
            "D": 44,
            "E": 45,
            "F": 46,
            "G": 47,
            "H": 48, 
            "I": 49, 
            "J": 50, 
            "K": 51,
            "L": 52, 
            "M": 53, 
            "N": 54, 
            "O": 55, 
            "P": 56, 
            "Q": 57, 
            "R": 58, 
            "S": 59, 
            "T": 60,
            "U": 61, 
            "V": 62, 
            "W": 63, 
            "X": 64, 
            "Y": 65, 
            "Z": 66, 
            "1": 27, 
            "2": 28, 
            "3": 29,
            "4": 30, 
            "5": 31, 
            "6": 32, 
            "7": 33, 
            "8": 34, 
            "9": 35, 
            "0": 36
}


def save_config(config_data, file_path='config.py'):
    with open(file_path, 'w') as f:
        f.write(f"letters = {config_data}\n")
        print(file_path)
    print(f"Config file '{file_path}' saved.")

def load_config(file_path='config.py'):

    if not os.path.exists(file_path):
        save_config(letters, file_path) 
        print(f"Config file '{file_path}' created with default data.")
        return letters
    else:
    
        config_dict = {}
        with open(file_path, 'r') as f:
        
            exec(f.read(), config_dict)
        print(f"Config file '{file_path}' loaded.")
        print(config_dict)
        return config_dict



letters = load_config()









import tkinter as tk
from tkinter import ttk, messagebox

def edit_letters_table(letters):
    def refresh_table():
      
        for row in tree.get_children():
            tree.delete(row)

       
        for key, value in letters.items():
            tree.insert("", "end", values=(key, value))

    def add_entry():
        key = key_entry.get()
        value = value_entry.get()

        if not key:
            messagebox.showerror("Error", "Key cannot be empty.")
            return
        if not value.isdigit():
            messagebox.showerror("Error", "Value must be a number.")
            return

        value = int(value)
        if key in letters:
            messagebox.showerror("Error", "Key already exists. Use edit instead.")
        else:
            letters[key] = value
        
        refresh_table()

    def remove_entry():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected.")
            return

        key = tree.item(selected_item, "values")[0]
        del letters[key]
        refresh_table()

    def edit_entry():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected.")
            return

        key = tree.item(selected_item, "values")[0]
        new_value = value_entry.get()

        if not new_value.isdigit():
            messagebox.showerror("Error", "Value must be a number.")
            return

        letters[key] = int(new_value)
        refresh_table()
        
    def on_close():
        if messagebox.askokcancel("Quit", "Do you want to save changes and exit?"):
            root.destroy()
            save_config(letters)
            return letters
            
    root = tk.Tk()
    root.title("Edit Table")

    root.protocol("WM_DELETE_WINDOW", on_close)
    
    columns = ("Key", "Value")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("Key", text="Key")
    tree.heading("Value", text="Value")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    form_frame = tk.Frame(root)
    form_frame.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(form_frame, text="Key:").grid(row=0, column=0, padx=5, pady=5)
    key_entry = tk.Entry(form_frame)
    key_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Value:").grid(row=0, column=2, padx=5, pady=5)
    value_entry = tk.Entry(form_frame)
    value_entry.grid(row=0, column=3, padx=5, pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X, padx=10, pady=5)

    tk.Button(button_frame, text="Add", command=add_entry).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(button_frame, text="Edit", command=edit_entry).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(button_frame, text="Remove", command=remove_entry).pack(side=tk.LEFT, padx=5, pady=5)

  
    refresh_table()

   
    root.mainloop()


def getKeyByValue(Value):
    for i in letters:
        
        if letters[i] == Value:
            return i

class Crypter:
    def __init__(self, text, key, decrypting):
        self.text = text
        self.key = key
        self.decrypting = True


    def genkey(self, length):
        self.key = ""
        currentletter = length
        
        while currentletter > 0:
            key, value = random.choice(list(letters.items()))
            currentletter = currentletter - 1
            self.key = self.key + key
        
        print("key generated:"  + str(self.key))
    def decryptKey(self):
        decrypted = 0
        currentletter = 1
        try:
            for char in self.key:
                decrypted = (letters[char] ^ currentletter) + decrypted
                currentletter = currentletter + 1
                print("decrypted the %s. letter as Number %s" % (currentletter, (letters[char] ^ currentletter)))
            print(f"decrypted key is: {decrypted}")
            return decrypted
        except:
            print("Something else went wrong. Probably the keyvalue isnt definied")
    
            
             
    def decrypt(self, encrypted_text, Lock, modulo1, modulo2, decryptingtable):
        currentchar = 1
        result = []
        for encrypted_char in encrypted_text:
            if decryptingtable[currentchar] != "Not Encrypted":
                
                r = decryptingtable[currentchar]
                print(f"r is {r} char is {currentchar}")
                if r != ":":
                    
                    encrypted_char = int(encrypted_char)
                    Lock = int(Lock)
                    modulo1 = int(modulo1)
                    modulo2 = int(modulo2)
                    r = int(r)
                    
                    decrypted_char = encrypted_char ^ r
                    decrypted_char = (decrypted_char - Lock) // modulo2
                    decrypted_char = (decrypted_char - r) // Lock  
                    original_char = getKeyByValue(int(decrypted_char))

                    print("Decrypted character:", original_char)

                    result.append(original_char)
                    currentchar = currentchar + 1
                
            else:
                print("Unencrypted character detected:", encrypted_char)
                result.append(encrypted_char) 
                currentchar = currentchar + 1
        
        
        stringresult = ""
        for i in result:
            stringresult = stringresult + str(i)
        
        return stringresult

    def encrypt(self, text):
        Lock = random.randint(1, 100)
        r = random.randint(1, 100)
        modulo1 = random.randint(1, 100)
        modulo2 = random.randint(1, 100)

        result = []
        currentchar = 1
        decryptingtable = {}

        for char in text:
            if char in letters:
                    
                    char = letters[char]
                    decryptingtable[currentchar] = random.randint(0, 100)
                    r = decryptingtable[currentchar]
                    encrypted_char = char * Lock + int(r)
                    encrypted_char = encrypted_char * modulo2 + Lock
                    encrypted_char = encrypted_char ^ r
                    print(f"turned {char} into {encrypted_char}",)
                    currentchar = currentchar + 1
                    result.append(encrypted_char)
                
            else:
                    decryptingtable[currentchar] = "Not Encrypted"
                    currentchar = currentchar + 1
                    result.append(char)

        
        print("crypted text generated: \n" + str(result))
        return result, Lock, decryptingtable, modulo1, modulo2
    
    
main = Crypter("", "", True)























def button_decrypt():
    print(f"Button wurde geklickt.")      
    show_message("Mode Changed","Changed to decrypting Mode!")
    main.decrypting= True
    
     
    
def button_encrypt():
    print(f"Button wurde geklickt.") 
    show_message("Mode Changed","Changed to encrypting Mode!")
    
    
    main.decrypting= False

    
root = ctk.CTk()
root.title("Cryptographic System")

root.geometry(f"{1800}x{1000}+0+0")

left_panel = ctk.CTkFrame(root, width=400)
left_panel.place(relx=0.0, rely=0.5, relheight=1.0, anchor="w")

title_label = ctk.CTkLabel(root, text="Cryptographic Software V 0.85", font=("Arial", 40))
title_label.pack(pady=20)


button_left1 = ctk.CTkButton(left_panel, text="Encrypt", command=lambda: button_encrypt(), height = 50)
button_left1.pack(padx=5, pady=5)  


def settings_menu():
    print(letters)
    edit_letters_table(letters)


button_left2 = ctk.CTkButton(left_panel, text="Decrypt", command=lambda: button_decrypt(), height = 50)
button_left2.pack(padx=5, pady=5) 

button_left3 = ctk.CTkButton(left_panel, text="Settings", command=lambda: settings_menu(), height = 50)
button_left3.pack(padx=5, pady=5, side="bottom")  


center_text = ctk.CTkTextbox(root, width=1350, height=700)
center_text.place(relx=1.0, rely=0.0, anchor="ne", x=-140, y=100)  


def action_button():
    print(main.decrypting)  
    
    if main.decrypting == True:
            file_name = file_entry.get()
            directory, filename = os.path.split(file_name)
                
          
            if os.path.isfile(file_name):
                try:
                    with open(file_name, 'r') as file:
                       
                        lines = [file.readline().strip() for _ in range(4)]
                    
                  
                    if len(lines) == 4:
                        Lock = lines[0]
                        decryptingtable_raw = lines[1]
                        modulo1 = lines[2]
                        modulo2 = lines[3]
                        try:
                            decryptingtable = ast.literal_eval(decryptingtable_raw)
                        except Exception as e:
                            raise ValueError(f"Failed to parse 'decryptingtable': {decryptingtable_raw}\nError: {e}")
                                            
                        
                        print("Lock:", Lock)
                        print("decryptingtable:", decryptingtable)
                        print("modulo1:", modulo1)
                        print("modulo2:", modulo2)
                    else:
                        print(f"File does not have 4 lines, found {len(lines)}.")
                except Exception as e:
                    print(f"Error reading file: {e}")
            else:
                print(f"File does not exist: {file_name}")
        
            print("starting decrypting")
            print(f"{center_text.get('1.0', 'end-1c')}")
            result = main.decrypt(ast.literal_eval(center_text.get("1.0", "end-1c")), Lock, modulo1, modulo2, decryptingtable)
            
            center_text.delete(1.0, tk.END) 
            center_text.insert(tk.END, f"{result}") 
        

    else:
        main.genkey(16)
        print("starting encrypting")
        cryptedtext, Lock, decryptingtable, modulo1, modulo2 = main.encrypt(center_text.get("1.0", "end-1c"))


        folderpath = filedialog.askdirectory(title="Select a Folder")
        
        os.makedirs(f"{folderpath}/data_{datetime.now().strftime("%Y%m%d%H%M%S")}", exist_ok=True)

        with open(f"{folderpath}/data_{datetime.now().strftime("%Y%m%d%H%M%S")}/Key.py", "w") as file:
            file.write(f'{Lock}\n')
            file.write(f"{decryptingtable}\n")
            file.write(f'{modulo1}\n')
            file.write(f"{modulo2}\n")
        
        with open(f"{folderpath}/data_{datetime.now().strftime("%Y%m%d%H%M%S")}/message.txt", "w") as file:
            file.write(f'{cryptedtext}\n')
        
        
        show_message("Successfully encrypted",f"Key and Text was saved at: \n {folderpath}/data_{datetime.now().strftime("%Y%m%d%H%M%S")}")
        

        center_text.delete(1.0, tk.END) 
        center_text.insert(tk.END, f"{cryptedtext}")  

                
        print("trying to save file")

def select_file():
    file_path = filedialog.askopenfilename() 
    file_entry.delete(0, "end") 
    file_entry.insert(0, file_path) 




bottom_panel = ctk.CTkFrame(root, height=100)
bottom_panel.pack(side="bottom", padx=10, pady=10)

title_label = ctk.CTkLabel(bottom_panel, text="Choose/Submit Key", font=("Arial", 20))
title_label.pack(pady=10)

input_frame = ctk.CTkFrame(bottom_panel)
input_frame.pack(pady=5)


file_entry = ctk.CTkEntry(input_frame, width=400, placeholder_text="Select Key file...")
file_entry.pack(side="left", padx=5, pady = 5)


file_button = ctk.CTkButton(input_frame, text="Browse", command=select_file)
file_button.pack(side="left", padx=5, pady = 5)



action_button = ctk.CTkButton(bottom_panel, text="Submit", command=action_button)
action_button.pack(pady=5)


root.mainloop()

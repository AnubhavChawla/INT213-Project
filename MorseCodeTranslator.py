import tkinter
from tkinter import *
from tkinter import messagebox

#Defining Characters - Morse code dictionary
Morse_Code_DICT={
'A' : ".-",
'B' : "-...",
'C' : "-.-.",
'D' : "-..",
'E' : ".",
'F' : "..-.",
'G' : "--.",
'H' : "....",
'I' : "..",
'J' : ".---",
'K' : "-.-",
'L' : ".-..",
'M' : "--",
'N' : "-.",
'O' : "---",
'P' : ".--.",
'Q' : "--.-",
'R' : ".-.",
'S' : "...",
'T' : "-",
'U' : "..-",
'V' : "...-",
'W' : ".--",
'X' : "-..-",
'Y' : "-.--",
'Z' : "--..",
'0' : "-----",
'1' : ".----",
'2' : "..---",
'3' : "...--",
'4' : "....-",
'5' : ".....",
'6' : "-....",
'7' : "--...",
'8' : "---..",
'9' : "----."
}

#Error message for empty input
def Loophole_Check():
    input_text_val = input_text.get("1.0","end-1c")
    if input_text_val=="":
        messagebox.askretrycancel("Empty Text!","Enter something to encrypt or decrypt.")
    else:
        pass

#Open New Morse code translator window
def Open_Morse_Code_Translator():
    translator.deiconify()
    login_page.withdraw()

#Login procedure to use Morse code translator    
def login_procedure():
    if((user_id_val.get()=="anubhav11914161" and user_pwd_val.get()=="7528045625") or (user_id_val.get()=="saneet11913912" and user_pwd_val.get()=="9501230787") or (user_id_val.get()=="sachin12000724" and user_pwd_val.get()=="6280823640")):
        Open_Morse_Code_Translator()
    else:
        messagebox.askretrycancel("Unauthorised Access", "Invalid credentials! You may retry or exit the application.")


 
#Encrypt button functioning
def Encrypt_Button_Function():
    Loophole_Check()
    input_text_val = input_text.get("1.0","end-1c")
    input_text_val = input_text_val.upper()
    encrypted_text=""
    for letter in input_text_val:
        if(letter != " "):
            encrypted_text=encrypted_text+Morse_Code_DICT[letter]+" "
        else:
            encrypted_text += " "
    output_text.delete("1.0",END)
    output_text.insert(INSERT,encrypted_text)
    output_text.config(state="normal")


#Decrypt Button functioning
def Decrypt_Button_Function():
    Loophole_Check()
    input_text_val = input_text.get("1.0","end-1c")
    input_text_val +=" "
    key_list = list(Morse_Code_DICT.keys())
    val_list = list(Morse_Code_DICT.values())
    morsecode=""
    decrypted_text=""
    space_found=0
    for letter in input_text_val:
        if(letter != " "):
            morsecode += letter
            space_found = 0
        else:
            space_found += 1
            if (space_found >= 2):
                decrypted_text += " "
            else:
                decrypted_text = decrypted_text + key_list[val_list.index(morsecode)]
                morsecode=""

    output_text.delete("1.0",END)
    output_text.insert(INSERT,decrypted_text)
    output_text.config(state="normal")


#Clear Button functioning                
def Clear_Button_Function():
    input_text.delete("1.0",END)
    output_text.delete("1.0",END)

#User interface creation of Login Page
#Login Page appears first to the user
#Only authorised users can access the Morse code translator using their valid credentials
login_page = Tk()
login_page.configure(bg="#330066")
login_page.title("Morse Code Translator")
login_page.geometry("1200x900+350+50")

header = Label(login_page,text="\u2605 \u265b  Morse Code Translator  \u265b \u2605",background="#2A1B3D",font=('Copperplate Gothic Bold',32,'bold'),foreground='turquoise1',width=46,height=2,relief=RAISED,bd=0)
header.pack()

textarea1 = Text(login_page,font=('Book Antiqua',18,'bold'),bg="#330066",bd=0,foreground='#A4B3B6',height=10)
textarea1.insert(INSERT,"\n\u2022 Morse code is a method used in telecommunication to encode text characters as \tstandardized sequences of two different signal durations, called dots and dashes.\n\u2022 Morse code is named after Samuel Morse, an inventor of the telegraph.")
textarea1.insert(INSERT,"\n\u2022 The International Morse Code encodes the 26 English letters A through Z, some \tnon-English letters, the Arabic numerals and a small set of punctuation and \tprocedural signals (prosigns).\n\u2022 There is no distinction between upper and lower case letters.")
textarea1.configure(state="disabled",wrap=WORD)
textarea1.pack()

user_id_val = StringVar()
user_pwd_val = StringVar()

user_id = Label(login_page,text="User ID:",background="#330066",font=('Copperplate Gothic Bold',24,'bold'),foreground="white",width=10,relief=SUNKEN,bd=0).place(x=100,y=400)
user_id_textbox = Entry(login_page,textvariable=user_id_val,width=45,font=('Times New Roman',24,'bold'),foreground='gray11',bg="orchid1").place(x=375,y=400) 

user_pwd = Label(login_page,text="Password:",background="#330066",font=('Copperplate Gothic Bold',24,'bold'),foreground='white',width=10,relief=RAISED,bd=0).place(x=100,y=475) 
user_pwd_textbox = Entry(login_page,textvariable=user_pwd_val,show="\u2605",width=45,font=('Times New Roman',24,'bold'),foreground='gray11',bg="orchid1").place(x=375,y=475) 

login_button = Button(login_page,text="Login",background="#d83f87",font=('Copperplate Gothic Bold',24,'bold'),foreground='black',width=10,command=login_procedure).place(x=375,y=550)
exit_button = Button(login_page,text="Exit",background="#d83f87",font=('Copperplate Gothic Bold',24,'bold'),foreground='black',width=10,command=login_page.destroy).place(x=675,y=550)


#Translator is the main window
#contains all the functioning of Morse code translator
translator = Toplevel()
translator.withdraw()
translator.title("Morse Code Translator")
translator.configure(bg="#330066")
translator.geometry("1200x900+350+50")
    
header = Label(translator,text="\u2605 \u265b  Morse Code Translator  \u265b \u2605",background="#2A1B3D",font=('Copperplate Gothic Bold',32,'bold'),foreground='turquoise1',width=46,height=2,relief=RAISED,bd=0)
header.pack()

input_label = Label(translator,text="Input:",background="#330066",foreground="white",width=6,font=("Copperplate Gothic Bold",24,'bold'),relief=RAISED,bd=0).place(x=100,y=150)
morse_code_label = Label(translator,text="Output:",background="#330066",foreground="white",width=7,font=("Copperplate Gothic Bold",24,'bold'),relief=RAISED,bd=0).place(x=100,y=510)

input_text = Text(translator,font=('Book Antiqua',16),bd=0,foreground='gray2',bg='orchid1',height=10,width=90,wrap=WORD)
input_text.pack(padx=100,pady=100)

output_text = Text(translator,font=('Book Antiqua',16),bd=0,foreground='gray2',bg='orchid1',height=10,width=90,wrap=WORD)
output_text.pack(padx=100)

encrypt_btn = Button(translator,text="Encrypt Text",background="#d83f87",font=('Copperplate Gothic Bold',18,'bold'),foreground='black',width=15,height=1,command=Encrypt_Button_Function).place(x=100,y=835)
decrypt_btn = Button(translator,text="Decrypt Text",background="#d83f87",font=('Copperplate Gothic Bold',18,'bold'),foreground='black',width=15,command=Decrypt_Button_Function).place(x=425,y=835)
clear_btn = Button(translator,text="Clear",background="#d83f87",font=('Copperplate Gothic Bold',18,'bold'),foreground='black',width=5,command=Clear_Button_Function).place(x=750,y=835)
exit_btn = Button(translator,text="Exit",background="#d83f87",font=('Copperplate Gothic Bold',18,'bold'),foreground='black',width=5,command=translator.destroy).place(x=900,y=835)

login_page.mainloop()
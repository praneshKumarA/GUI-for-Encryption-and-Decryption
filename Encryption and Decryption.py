#Importing required libraries
from tkinter import *
import datetime
import time
import random

#Creating a window
window = Tk()

#Setting title of the window
window.title("Encryption and Decryption")

#Setting the size of the window
window.geometry("1200x6000")

#Creating a frame for the title
f1 = Frame(window, width = 1600, relief = SUNKEN)
f1.pack(side = TOP)

#Creating a frame for the inputs and output
f2 = Frame(window, width = 800, height = 700, relief = SUNKEN)
f2.pack(side = LEFT)

#Storing the current time and date in a variable
localtime = time.asctime(time.localtime(time.time()))

#Creating a label for the title
l1 = Label(f1, font = ("helvetica", 50, "bold italic"), text = "ENCRYPTION & DECRYPTION \n Vigenēre Cipher", fg = 'Black', bd = 10, anchor = W)
l1.grid(row = 0, column = 0)

#Creating a label for time
l2 = Label(f1,font = ("times", 20, "bold underline"), text = localtime, fg = "cyan", bd = 10, anchor = W)
l2.grid(row = 1,column = 0)

#Creating required strings
rand = StringVar()
msg = StringVar()
key = StringVar()
mode = StringVar()
res = StringVar()

#Importing message box library
from tkinter import messagebox

#Exit function with confirmation
def qExit():
    if messagebox.askyesno('QUIT?','Are you sure want to exit?') == True:
        window.destroy()
    else:
        window.mainloop()
    
#Function to reset the window
def reset():
    rand.set("")
    msg.set("")
    key.set("")
    mode.set("")
    res.set("")

#Creating label for name
label1 = Label(f2, font = ("Arial", 15, "bold"), text = "Name", bd = 10, anchor = W)
label1.grid(row = 0, column = 0)

#Creating entry for name
entry1 = Entry(f2, font = ("Arial", 15, "bold"), textvariable = rand, bg = "powder blue", bd = 10, justify = LEFT)
entry1.grid(row = 0, column = 1)

#Creating label for msg
label2 = Label(f2, font = ("Arial", 15, "bold"), text = "Message", bd = 10, anchor = W)
label2.grid(row = 1, column = 0)

#Creating entry for msg
entry2 = Entry(f2, font = ("Arial", 15, "bold"), textvariable = msg, bg = "powder blue", bd = 10, justify = LEFT)
entry2.grid(row = 1, column = 1)

#Creating label for key
label3 = Label(f2, font = ("Arial", 15, "bold"), text = "Key", bd = 10, anchor = W)
label3.grid(row = 2, column = 0)

#Creating entry for key
entry3 = Entry(f2, font = ("Arial", 15, "bold"), textvariable = key, bg = "powder blue", bd = 10, justify = LEFT)
entry3.grid(row = 2, column = 1)

#Creating label for mode
label4 = Label(f2, font = ("Arial", 15, "bold"), text = "Mode(e-Encrypt (or) d-Decrypt)", bd = 10, anchor = W)
label4.grid(row = 3, column = 0)

#Creating entry for mode
entry4 = Entry(f2, font = ("Arial", 15, "bold"), textvariable = mode, bg = "powder blue", bd = 10, justify = LEFT)
entry4.grid(row = 3, column = 1)

##Creating label for result
label5 = Label(f2, font = ("Arial", 15, "bold"), text = "The Result", bd = 10, anchor = W)
label5.grid(row = 2, column = 2)

#Creating entry for result
entry5 = Entry(f2, font = ("Arial", 15, "bold"), textvariable = res, bg = "powder blue", bd = 10, justify = LEFT)
entry5.grid(row = 2, column = 3)

#Importing required library
import base64 as b

#Function to encode
def encode(key, original):
    enc = []
    
    for i in range(len(original)):
        #This loop is to repeat the key as to the length of the original string
        key1 = key[i % len(key)]
        enc1 = chr((ord(original[i]) + ord(key1)) % 256)
    
        enc.append(enc1)
    return b.urlsafe_b64encode("".join(enc).encode()).decode()

#Function to decode
def decode(key, cip):
    dec = []
    
    cip = b.urlsafe_b64decode(cip).decode()
    for i in range(len(cip)):
        #This loop is to repeat the key as to the length of the encoded string
        key2 = key[i % len(key)]
        dec1 = chr((256 + ord(cip[i]) - ord(key2)) % 256)
        
        dec.append(dec1)
    return "".join(dec)

#Function to validate and print the result
def Res():
    #Getting the messages entered in the entries
    original = msg.get()
    k = key.get()
    m = mode.get()
    #Calling the function based on the input given to mode
    if m == 'e' and original != '' and k != '':
        res.set(encode(k, original))
    elif m == 'd' and original  != ''  and k != '':
        res.set(decode(k, original))
    else:
        #To make a message box appear if message and key are empty
        if messagebox.askretrycancel('Error','Try Again?') == True:
            reset()
            window.mainloop()
        else:
            window.destroy()

#Creating show button
ans = Button(f2, padx = 16, pady = 8, fg = "black", font = ("arial", 16, "bold"), bd = 10, width = 10, text = "Show", bg = "red", command = Res, cursor = "hand2")
ans.grid(row = 7, column = 1)

#Creating reset button
reset1 = Button(f2, padx = 16, pady =8, fg = "black", font = ("arial", 16, "bold"), bd = 10, width =10, text = "Reset", bg = "yellow", command = reset, cursor = "hand2")
reset1.grid(row = 7, column = 2)

#Creating exit button
ex = Button(f2, padx = 16, pady =8, fg = "black", font = ("arial", 16, "bold"), bd = 10, width =10, text = "Exit", bg = "Green", command = qExit, cursor = "hand2")
ex.grid(row = 7, column = 3)

#Runs the code in the window
window.mainloop()

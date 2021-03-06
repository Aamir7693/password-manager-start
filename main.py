from tkinter import *
from tkinter import messagebox
import random
import json
webs=""
email=""
password=""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passgenerator():
    global password
    password=""
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    CHARACTERS=[x for x in characters]
    NUMBERS=[0,1,2,3,4,5,6,7,8,9]
    for i in range(12):
        select=random.randint(0,1)
        if select==0:
            character=random.choice(CHARACTERS)
            password+=character
        else:
            number=random.choice(NUMBERS)
            password+=str(number)
    input3.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savedetails():
    newpass=""
    webs=input1.get()
    email=input2.get()
    data = {webs: {
        "Password": password,
        "email": email
    }
    }
    if password:
        newpass=password
    else:
        newpass=input3.get()
    if not webs or not email or not newpass:
        messagebox.showinfo(title="Missing Data",message="Hey you are missing some feilds")
    else:
        is_ok = messagebox.askokcancel(title="SAVE CHECK",
                                       message=f"Website:{webs} \nEmail:{email}\nPassword:{newpass}\nIs it ok to save the details")
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    jdata=json.load(f)
                    jdata.update(data)
            except FileNotFoundError:
                with open("data.json","w") as f:
                    json.dump(data,f,indent=4)
            else:
                with open("data.json", "w") as f:
                    json.dump(jdata, f, indent=4)
            finally:
                input1.delete(0, END)
                input3.delete(0, END)

def getdetails():
    inp=input1.get()
    input2.delete(0,END)

    with open("data.json", "r") as f:
        jdata = json.load(f)
        for website in jdata:
            if inp==website:
                password=jdata[website]["Password"]
                email=jdata[website]["email"]
                messagebox.showinfo(title="Info",message=f"The website email is {email} \n The password used was {password}")
                inp=None
        if inp:
            messagebox.showerror(title="Warning",message=f"The Entered website {inp} does not Exist in database\n ")
            input1.delete(0,END)
            input1.focus()





# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")

canvas=Canvas(width=200,height=200)
window.config(padx=20,pady=20)

logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
label1=Label(text="Website:")
label1.grid(row=1,column=0)
input1=Entry(width=36)
input1.focus()
input1.grid(row=1,column=1,columnspan=2)
label2=Label(text="Email/Username:")
label2.grid(row=2,column=0)
input2=Entry(width=36,)
input2.insert(0,"aamir@gmail.com")
input2.grid(row=2,column=1,columnspan=2)
label3=Label(text="Password:")
label3.grid(row=3,column=0)
input3=Entry(width=25)
input3.grid(row=3,column=1)
button1=Button(text="Generate Password",width=12,font=("arial",7),command=passgenerator)
button1.grid(row=3,column=2)
button2=Button(text="Add",font=("arial",10),command=savedetails)
button2.config(width=38)
button2.grid(row=4,column=1,columnspan=2)
button3=Button(text="Search",font=("arial",7),command=getdetails)
button3.config(width=12)
button3.grid(row=1,column=2)


#------------------------Functions-----------------------------------------------------#








window.mainloop()
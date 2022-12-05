import docx
doc = docx.Document("sample.docx")

def generate_warranty():
    for paragraph in doc.paragraphs:
        if 'paragraph keyword' in paragraph.text:
            paragraph.text = 'change all the paragraph'
    doc.save("new.docx")

generate_warranty()


#I need to attach this file

import smtplib

my_email = "my_email@gmail.com"
password = "password for applications"
my_phone = "my phone number email"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_phone, msg="Subject: None\n\nNone")
    
from tkinter import *
from tkinter import ttk
from datetime import datetime

window = Tk()
window.title("Warranty Card Generator")
window.geometry("500x400")

phones = {

    "iPhone 11": {"memory": ["64 GB", "128 GB"], "color": ["Red", "Black", "White", "Yellow", "Green", "Purple"]},

    "iPhone 12": {"memory": ["64 GB", "128 GB"], "color": ["Black", "Blue", "Purple", "Red", "Green", "White"]},

    "iPhone 13": {"memory": ["64 GB", "128 GB"], "color": ["Red", "Starlight", "Midnight", "Blue" "Pink", "Green"]},
    "iPhone 13 Pro": {"memory": ["128 GB", "256 GB", "512 GB", "1 TB"], "color": ["Graphite", "Silver", "Gold", "Sierra Blue","Alpine Green"]},
    "iPhone 13 Pro Max": {"memory": ["128 GB", "256 GB", "512 GB", "1 TB"], "color": ["Graphite", "Silver", "Gold", "Sierra Blue","Alpine Green"]},
    "iPhone 13 mini": {"memory": ["128 GB"], "color": ["Red", "Starlight", "Midnight", "Blue" "Pink", "Green"]},

    "iPhone 14": {"memory": ["128 GB", "256 GB"], "color": ["Midnight", "Starlight", "Red", "Blue", "Purple"]},
    "iPhone 14 Plus": {"memory": ["128 GB", "256 GB"], "color": ["Midnight", "Starlight", "Red", "Blue", "Purple"]},
    "iPhone 14 Pro": {"memory": ["128 GB", "256 GB", "512 GB", "1 TB"], "color": ["Space Black", "Silver", "Gold", "Deep Purple"]},
    "iPhone 14 Pro Max": {"memory": ["128 GB", "256 GB", "512 GB", "1 TB"], "color": ["Space Black", "Silver", "Gold", "Deep Purple"]}
}


def show_features(e):
    phone_color_choice.config(value=phones[phone_model_choice.get()]["color"])
    phone_color_choice.current(0)
    phone_memory_choice.config(value=phones[phone_model_choice.get()]["memory"])
    phone_memory_choice.current(0)

def generate_description():
    string = phone_model_choice.get() + ", " + phone_color_choice.get() + ", " + phone_memory_choice.get()
    print(string)


# GUI
#Phone Model
phone_model = Label(text="Choose a phone model: ", pady=10)
phone_model.place(x=20, y=10)
phone_model_choice = ttk.Combobox(window, value=list(phones.keys()))
phone_model_choice.place(x=250, y=18)
phone_model_choice.bind("<<ComboboxSelected>>", show_features)

# Phone Color
phone_color = Label(text="Choose a phone color: ", pady=10)
phone_color.place(x=20, y=40)
phone_color_choice = ttk.Combobox(window, value = [""])
phone_color_choice.place(x=250, y=48)

# Phone memory

phone_memory = Label(text="Choose phone memory:", pady=10)
phone_memory.place(x=20, y=70)
phone_memory_choice = ttk.Combobox(window, value = [""])
phone_memory_choice.place(x=250, y=78)

#Current date

today = datetime.now()


date = Label(text="Choose a date: ", pady=10)
date.place(x=20, y=100)

date_day = Entry(width=10)
date_day.insert(0, today.strftime("%d"))
date_day.place(x=250, y=105)

date_month = Entry(width=10)
date_month.insert(0, today.strftime("%m"))
date_month.place(x=290, y=105)

date_year = Entry(width=10)
date_year.insert(0, today.strftime("%Y"))
date_year.place(x=330, y=105)



# Generate Warranty Card Button

generate_button = Button(text="Generate Warranty Card", command=generate_description, pady=20)
generate_button.place(x=100, y=130)




window.mainloop()

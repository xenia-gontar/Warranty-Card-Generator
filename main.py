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

window = Tk()
window.title("Warranty Card Generator")

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
    string = phone_model_choice.get() + phone_color_choice.get() + phone_memory_choice.get()
    print(string)


# GUI
#Phone Model
phone_model = Label(text="Choose a phone model: ")
phone_model.pack()
phone_model_choice = ttk.Combobox(window, value=list(phones.keys()))
phone_model_choice.pack()
phone_model_choice.bind("<<ComboboxSelected>>", show_features)

# Phone Color
phone_color = Label(text="Choose a phone color: ")
phone_color.pack()
phone_color_choice = ttk.Combobox(window, value = [""])
phone_color_choice.pack()

# Phone memory

phone_memory = Label(text="Choose phone memory: ")
phone_memory.pack()
phone_memory_choice = ttk.Combobox(window, value = [""])
phone_memory_choice.pack()

# Generate Warranty Card Button

generate_button = Button(text="Generate warranty card", command=generate_description)
generate_button.pack()




window.mainloop()    

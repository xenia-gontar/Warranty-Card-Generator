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

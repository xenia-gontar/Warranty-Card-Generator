import docx #installed with pip
import re
doc = docx.Document("phones.docx")


for paragraph in doc.paragraphs:
    if re.search(r"\d{4,6}", paragraph.text) != None:
        result = int(re.search(r"\d{4,6}", paragraph.text).group(0))
        if result <= 20000:
            price = result + 3000
            paragraph.text = re.sub('\d{4,6}', '', paragraph.text)
            paragraph.text += f"{price}"
        else:
            price = result + 5000
            paragraph.text = re.sub('\d{4,6}', '', paragraph.text)
            paragraph.text += f"{price}"

doc.save("new.docx")

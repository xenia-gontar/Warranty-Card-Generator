import docx
import re
doc = docx.Document("doc.docx")


for paragraph in doc.paragraphs:
    if re.search(r"\d{5,6}", paragraph.text) != None:
        result = int(re.search(r"\d{5,6}", paragraph.text).group(0))
        price = result + 3500
        result_as_str = str(result)
        paragraph.text = re.sub('\d{5,6}', '', paragraph.text)
        paragraph.text += f"{price}"
        print(paragraph.text)
doc.save("new.docx")

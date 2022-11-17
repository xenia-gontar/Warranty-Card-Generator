import docx
doc = docx.Document("sample.docx")

def generate_warranty():
    for paragraph in doc.paragraphs:
        if 'paragraph keyword' in paragraph.text:
            paragraph.text = 'change all the paragraph'
    doc.save("new.docx")

generate_warranty()
    

import fitz

#PDF READER
def readpdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    nopages = doc.page_count
    content = []
    for i in range(0,nopages):
        page = doc.load_page(i)
        text = page.get_text()
        actual = text.replace("\t"," ")
        content.append(actual)
    return " ".join(content)
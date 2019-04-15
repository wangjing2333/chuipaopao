
# -*- coding:utf-8 -*-
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from urllib.request import urlopen
#fp = open("test.pdf","rb")

fp = urlopen("http://www.tencent.com/zh-cn/articles/8003251479983154.pdf ")
parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize("")

resource = PDFResourceManager()
laparam = LAParams()
device = PDFPageAggregator(resource,laparams=laparam)
interpreter = PDFPageInterpreter(resource,device)


for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for out in layout:
        if hasattr(out, "get_text"):
            print(out.get_text())
        



import pdfplumber
import re
with pdfplumber.open('LAPTOP_invoice.pdf') as pdf:
    page=pdf.pages[0]
    text=page.extract_text()
#print(text)
seller_re=re.compile('limited')
seller_name=''
buyer_re=re.compile('kumar')
buyer_name=''
invoice_re=re.compile('tax invoice')
invoice_NO=''
order_re=re.compile('order date')
date_=''
for line in text.split('\n'):
    if invoice_re.search(line.lower()):
        invoice_NO=line.split('#')[-1]
    if seller_re.search(line.lower()):
        seller_name=(line.split(':')[-1]).split(',')[0]
    if order_re.search(line.lower()):
        date_=line.split(':')[-1]
    if buyer_re.search(line.lower()):
        l1=line.split(' ')[:2]
        buyer_name=" ".join(l1)











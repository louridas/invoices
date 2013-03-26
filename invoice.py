#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import sys
import xml.etree.ElementTree as ET

one_to_twenty_n = [
    'ένα',
    'δύο',
    'τρία',
    'τέσσερα',
    'πέντε',
    'έξι',
    'επτά',
    'οκτώ',
    'εννέα',
    'δέκα',
    'έντεκα',
    'δώδεκα',
    'δεκατρία',
    'δεκατέσσερα',
    'δεκαπέντε',
    'δεκαέξι',
    'δεκαεπτά',
    'δεκαοκτώ',
    'δεκαεννέα'
    ]

one_to_twenty_f = [
    'μία',
    'δύο',
    'τρεις',
    'τέσσερεις',
    'πέντε',
    'έξι',
    'επτά',
    'οκτώ',
    'εννέα',
    'δέκα',
    'έντεκα',
    'δώδεκα',
    'δεκατρείς',
    'δεκατέσσερεις',
    'δεκαπέντε',
    'δεκαέξι',
    'δεκαεπτά',
    'δεκαοκτώ',
    'δεκαεννέα'
    ]

tens = [
    'δέκα',
    'είκοσι',
    'τριάντα',
    'σαράντα',
    'πενήντα',
    'εξήντα',
    'εβδομήντα',
    'ογδόντα',
    'ενενήντα'
    ]

hundreds_n = [
    'εκατό',
    'διακόσια',
    'τριακόσια',
    'τετρακόσια',
    'πεντακόσια',
    'εξακόσια',
    'επτακόσια',
    'οκτακόσια',
    'εννιακόσια'
    ]

hundreds_f = [
    'εκατό',
    'διακόσιες',
    'τριακόσιες',
    'τετρακόσιες',
    'πεντακόσιες',
    'εξακόσιες',
    'επτακόσιες',
    'οκτακόσιες',
    'εννιακόσιες'
    ]

thousands = [
    'χίλια',
    'χιλιάδες'
    ]

millions = [
    'εκατομμύριο',
    'εκατομμύρια'
    ]

billions = [
    'δισεκατομμύριο',
    'δισεκατομμύρια'
    ]

def num_to_text_hundreds(number, f):
    parts = []
    h, mod100 = divmod(number, 100)
    t, mod10 = divmod(mod100, 10)
    if h > 0:
        if h == 1 and mod100 > 0:
            parts.append(hundreds_n[h - 1] + 'ν')
        else:
            if f == True:
                parts.append(hundreds_f[h - 1])
            else:
                parts.append(hundreds_n[h - 1])
    if t > 1:
        parts.append(tens[t - 1])
        if f == True:
            parts.append(one_to_twenty_f[mod10 - 1])
        else:
            parts.append(one_to_twenty_n[mod10 - 1])
    elif t == 1:
        if f == True:
            parts.append(one_to_twenty_f[10 * t + mod10 - 1])
        else:
            parts.append(one_to_twenty_n[10 * t + mod10 - 1])
    elif mod10 > 0:
        if f == True:
            parts.append(one_to_twenty_f[10 * t + mod10 - 1])
        else:
            parts.append(one_to_twenty_n[10 * t + mod10 - 1])        
    return ' '.join(parts)

def num_to_text_thousands(number):
    th, r = divmod(number, 1000)
    if th > 1:
        return "{} {} {}".format(num_to_text_hundreds(th, True),
                                 thousands[1],
                                 num_to_text_hundreds(r, False))
    elif th == 1:
        return "{} {}".format(thousands[0], num_to_text_hundreds(r, False))
    else:
        return num_to_text_hundreds(r, False)

def num_to_text_millions(number):
    m, r = divmod(number, 1000000)
    if m > 1:
        return "{} {} {}".format(num_to_text_hundreds(m, False),
                              millions[1],
                              num_to_text_thousands(r))
    elif m == 1:
        return "{} {} {}".format(one_to_twenty_n[0],
                                 millions[0],
                                 num_to_text_thousands(r))
    else:
        return num_to_text_thousands(number)

def num_to_text_billions(number):
    m, r = divmod(number, 1000000000)
    if m > 1:
        return "{} {} {}".format(num_to_text_hundreds(m, False),
                                 billions[1],
                                 num_to_text_millions(r))
    elif m == 1:
        return "{} {} {}".format(one_to_twenty_n[0],
                                 billions[0],
                                 num_to_text_millions(r))
    else:
        return num_to_text_millions(number)
    
def num_to_text(number):
    return num_to_text_billions(number)


if len(sys.argv) < 2:
    print "Usage: python invoice.py invoice_data.xml"
    sys.exit(1)

tree = ET.parse(sys.argv[1])
root = tree.getroot()

num = root.find('num').text
date = root.find('date').text
stamp = root.find('stamp').text
client = root.find('client').text
occupation = root.find('occupation').text
taxoffice = root.find('taxoffice').text
address = root.find('address').text
taxnumber = root.find('taxnumber').text
description = root.find('description').text
value_f = float(root.find('value').text)
value = "{:.2f}".format(value_f)
tax_f = value_f * 0.20
vat_f = value_f * 0.23
total_f = value_f + vat_f
tax = "{:.2f}".format(tax_f)
vat = "{:.2f}".format(vat_f)
total = "{:.2f}".format(total_f) 
(intpart, floatpart) = total.split('.')

numbertext = "{} ευρώ".format(num_to_text(int(intpart)))

if floatpart != '' :
    floatpart_i = int(floatpart)
    if floatpart_i > 0:
        numbertext = "{} και {} λεπτά".format(numbertext,
                                              num_to_text(int(floatpart)))

outfn = 'invoice_' + num + '.tex'
  
with codecs.open('invoice.tex', mode='r', encoding='utf-8') as inf:
    with codecs.open(outfn, mode='w', encoding='utf-8') as outf:
        for line in inf:
            line = line.replace("{{NUM}}", num)
            line = line.replace("{{DATE}}", date)
            line = line.replace("{{STAMP}}", stamp)
            line = line.replace("{{CLIENT}}", client)
            line = line.replace("{{OCCUPATION}}", occupation)
            line = line.replace("{{TAXOFFICE}}", taxoffice)
            line = line.replace("{{ADDRESS}}", address)
            line = line.replace("{{TAXNUMBER}}", taxnumber)
            line = line.replace("{{DESCRIPTION}}", description)
            line = line.replace("{{VALUE}}", value)
            line = line.replace("{{TAX}}", tax)
            line = line.replace("{{VAT}}", vat)
            line = line.replace("{{TOTAL}}", total)
            line = line.replace("{{NUMBERTEXT}}",
                                numbertext.decode('utf-8').capitalize())
            outf.write(line)


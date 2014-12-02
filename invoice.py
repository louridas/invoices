#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import sys
import xml.etree.ElementTree as ET
import argparse

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

one_to_twenty_en = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
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

tens_en = [
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
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

hundreds_en = [ x + ' hundred' for x in one_to_twenty_en[0:10]]

thousands = [
    'χίλια',
    'χιλιάδες'
    ]

thousands_en = [
    'one thousand',
    'thousand'
]

millions = [
    'εκατομμύριο',
    'εκατομμύρια'
    ]

millions_en = [
    'one million',
    'million'
]

billions = [
    'δισεκατομμύριο',
    'δισεκατομμύρια'
    ]

billions_en = [
    'one billion',
    'billion'
]

def num_to_text_hundreds(number, f, english=False):
    parts = []
    h, mod100 = divmod(number, 100)
    t, mod10 = divmod(mod100, 10)
    if english:
        one_to_twenty_arr_f = one_to_twenty_en
        one_to_twenty_arr_n = one_to_twenty_en
        hundreds_arr_f = hundreds_en
        hundreds_arr_n = hundreds_en
        tens_arr = tens_en
    else:
        one_to_twenty_arr_f = one_to_twenty_f
        one_to_twenty_arr_n = one_to_twenty_n
        hundreds_arr_f = hundreds_f
        hundreds_arr_n = hundreds_n
        tens_arr = tens
    if h > 0:
        if h == 1 and mod100 > 0 and english:
            parts.append(hundreds_arr_n[h - 1] + 'ν')
        else:
            if f == True:
                parts.append(hundreds_arr_f[h - 1])
            else:
                parts.append(hundreds_arr_n[h - 1])
    if t > 1:
        parts.append(tens_arr[t - 1])
        if mod10 > 0:
            if english:
                parts[-1] = parts[-1] + '-' + one_to_twenty_arr_f[mod10 - 1]
            elif f == True:
                parts.append(one_to_twenty_arr_f[mod10 - 1])
            else:
                parts.append(one_to_twenty_arr_n[mod10 - 1])
    elif t == 1:
        parts.append(one_to_twenty_arr_n[10 + mod10 - 1])
    elif mod10 > 0:
        if f == True:
            parts.append(one_to_twenty_arr_f[mod10 - 1])
        else:
            parts.append(one_to_twenty_arr_n[mod10 - 1])
    return ' '.join(parts)

def num_to_text_thousands(number, english=False):
    th, r = divmod(number, 1000)
    if english:
        thousands_arr = thousands_en
    else:
        thousands_arr = thousands        
    if th > 1:
        return "{0} {1} {2}".format(num_to_text_hundreds(th, True, english),
                                    thousands_arr[1],
                                    num_to_text_hundreds(r, False, english))
    elif th == 1:
        return "{0} {1}".format(thousands_arr[0],
                                num_to_text_hundreds(r, False, english))
    else:
        return num_to_text_hundreds(r, False, english)

def num_to_text_millions(number, english=False):
    m, r = divmod(number, 1000000)
    if english:
        millions_arr = millions_en
    else:
        millions_arr = millions    
    if m > 1:
        return "{0} {1} {2}".format(num_to_text_hundreds(m, False),
                                    millions_arr[1],
                                    num_to_text_thousands(r, english))
    elif m == 1:
        return "{0} {1} {2}".format(one_to_twenty_n[0],
                                    millions_arr[0],
                                    num_to_text_thousands(r, english))
    else:
        return num_to_text_thousands(number, english)

def num_to_text_billions(number, english=False):
    m, r = divmod(number, 1000000000)
    if english:
        billions_arr = billions_en
    else:
        billions_arr = billions
    if m > 1:
        return "{0} {1} {2}".format(num_to_text_hundreds(m, False),
                                    billions_arr[1],
                                    num_to_text_millions(r, english))
    elif m == 1:
        return "{0} {1} {2}".format(one_to_twenty_n[0],
                                    billions_arr[0],
                                    num_to_text_millions(r, english))
    else:
        return num_to_text_millions(number, english)
    
def num_to_text(number, english=False):
    return num_to_text_billions(number, english)


parser = argparse.ArgumentParser(description='Invoice creator')
parser.add_argument('invoice_data')
parser.add_argument('-t', '--template', dest='template',
                    default='invoice.tex')
parser.add_argument('-e', '--english', dest='english',
                    action='store_true',
                    default=False)

args = parser.parse_args()

tree = ET.parse(args.invoice_data)
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
tax_rate_el = root.find('tax_rate')
if tax_rate_el is not None:
    tax_rate = tax_rate_el.text
else:
    tax_rate = "0.20" # default value
tax_rate_f = float(tax_rate)
tax_rate_prc = "{:.2f}".format(tax_rate_f * 100)
if tax_rate_prc.endswith('.00'):
    tax_rate_prc = tax_rate_prc.replace('.00', '')
vat_rate_el = root.find('vat_rate')
if vat_rate_el is not None:
    vat_rate = vat_rate_el.text
else:
    vat_rate = "0.23" # default value
vat_rate_f = float(vat_rate)
vat_rate_prc = "{:.2f}".format(vat_rate_f * 100)
if vat_rate_prc.endswith('.00'):
    vat_rate_prc = vat_rate_prc.replace('.00', '')
value = "{:.2f}".format(value_f)
tax_f = value_f * tax_rate_f
vat_element = root.find('vat')
if vat_element is not None:
    vat_f = float(vat_element.text)
else:
    vat_f = value_f * vat_rate_f
total_f = value_f + vat_f
tax = "{:.2f}".format(tax_f)
vat = "{:.2f}".format(vat_f)
total = "{:.2f}".format(total_f) 
(intpart, floatpart) = total.split('.')

numbertext = "{0} ευρώ".format(num_to_text(int(intpart)))

if args.english:
    numbertext_en = "{0} euros".format(num_to_text(int(intpart), True))
else:
    numbertext_en = ""
    
if floatpart != '' :
    floatpart_i = int(floatpart)
    if floatpart_i > 0:
        if floatpart_i > 1:
            dec_desc = 'λεπτά'
        else:
            dec_desc = 'λεπτό'
        numbertext = "{0} και {1} {2}".format(numbertext,
                                              num_to_text(int(floatpart)),
                                              dec_desc)
        if args.english:
            if floatpart_i > 1:
                dec_desc = 'cents'
            else:
                dec_desc = 'cent'            
            numbertext_en = "{0} and {1} {2}".format(numbertext_en,
                                                     num_to_text(
                                                         int(floatpart),
                                                         True),
                                                     dec_desc)

outfn = 'invoice_' + num + '.tex'
  
with codecs.open(args.template, mode='r', encoding='utf-8') as inf:
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
            line = line.replace("{{TAXRATE}}", tax_rate_prc)
            line = line.replace("{{TAX}}", tax)
            line = line.replace("{{VATRATE}}", vat_rate_prc)
            line = line.replace("{{VAT}}", vat)
            line = line.replace("{{TOTAL}}", total)
            line = line.replace("{{NUMBERTEXT}}",
                                numbertext.decode('utf-8').capitalize())
            line = line.replace("{{NUMBERTEXTEN}}",
                                numbertext_en.decode('utf-8').capitalize())
                
            outf.write(line)


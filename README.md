invoices
========

Generates invoices to be used according to the latest (2012-2013) tax regulations.

Usage
=====

    usage: invoice.py [-h] [-t TEMPLATE] [-e] invoice_data

    Invoice generator

    positional arguments:
      invoice_data

    optional arguments:
      -h, --help            show this help message and exit
      -t TEMPLATE, --template TEMPLATE
                            Use TEMPLATE as LaTeX template
      -e, --english         Include English output

where `invoice_data` is an XML file containing the data to be entered in a particular invoice. A LaTeX (in particular, XeLaTeX) file will be produced, which you can typeset and print out.

The LaTeX file will be based on a template file; by default, this will be `invoice.tex`, but you can set your own by specifying `-t`.

The data are contained in the following elements:

* num: the invoice number; this number will be used to produce the output filename `invoice_<num>.tex` and to number
  the invoice itself
* date: the invoice date
* stamp: the boilerplate that is usually present in the traditional invoice stamps
* client: the client name
* occupation: the client occupation
* taxoffice: the client tax office
* address: the client address
* taxnumber: the client taxnumber
* description: the description of the work performed
* value: the value of the work performed; this is the only amount that needs to be entered, as the withholding tax,  
  the VAT, as well the string representation of the amount are produced automatically
* vat_rate: if present, the VAT rate to be applied; default is 0.23
* tax_rate: if present, the withholding tax rate to be applied; default is 0.20

If you set `-e` then the program will also produce English output. Note that this may require small adjustments in the LaTeX file, as including both Greek and English numbers in full may take more vertical space than you may have foreseen in your LaTeX template file.

A Greek example [invoice.xml](https://github.com/louridas/invoices/blob/master/invoice.xml) is included in the repo, as is its [output](https://github.com/louridas/invoices/blob/master/invoice_1.pdf) produced using an [example template](https://github.com/louridas/invoices/blob/master/invoice.tex). For English, you can check the example [invoice_2.xml](https://github.com/louridas/invoices/blob/master/invoice_2.xml) and its [output](https://github.com/louridas/invoices/blob/master/invoice_2.pdf) produced using [another example template](https://github.com/louridas/invoices/blob/master/invoice_en.tex)

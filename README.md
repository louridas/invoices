invoices
========

Generates invoices to be used according to the latest (2012-2013) tax regulation

Usage
=====

    python invoice.py invoice.xml
    xelatex invoice_<num>.tex

where `invoice.xml` is a file containing the data to be entered in a particular invoice. The data are entered as
the following elements:

* num: the invoice number; this number will be used to produce the output filename `invoice_<num>.tex`
* date: the invoice date
* stamp: the boilerplate that is usually present in the traditional invoice stamps
* client: the client name
* occupation: the client occupation
* taxoffice: the client tax office
* address: the client address
* taxnumber: the client taxnumber
* description: the description of the work performed
* value: the value of the work performed

A sample `invoice.xml` is included in the repo.

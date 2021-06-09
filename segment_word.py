#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function will access URLs that point to word documents and get the text.

Word documents are converted into pdfs in order to break them down into pages.
The text will be broken down into pages to do analysis on each page later on.

Input: 'response' (the result of the requests.get method)
Output: a dictionary where keys are page numbers and values are text

Viktoria, June 2021

"""

import os
import pdfplumber
from docx2pdf import convert
import re


def segment_word(title, response, download):
    
    #Get the correct extension of the output file
    if '.docx' in title:
        title = re.sub(r'.docx', '', title)
        
    if '.pdf' not in title:
        title = title + '.pdf'

    #Initiate empty dictionary which will be populated
    content = {}

    open('myfile.docx', 'wb').write(response.content)
    
    #Convert to pdf
    convert("myfile.docx", title)

    #Segment into pages
    with pdfplumber.open(title) as pdf:

        pages = pdf.pages
        for count,page in enumerate(pages):
            content[count+1] = page.extract_text()
            
    #If download was requested...
    if download == 1:
        #Only remove the word file
        os.remove('myfile.docx')
    else:
        #Remove them both
        os.remove('myfile.docx')
        os.remove(title)
        
    return content
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This function will access URLs that point to htmls and get the text.

Htmls are converted into pdfs in order to break them down into pages.
The text will be broken down into pages to do analysis on each page later on.

Input: a URL
Output: a dictionary where keys are page numbers and values are text

Viktoria, June 2021

"""

import os
import pdfkit
import pdfplumber
import re

#convert html to pdf and process it as such
def segment_html(title, url, download):
    
    #Get the correct extension of the output file
    if '.html' in title:
        title = re.sub(r'.html', '', title)
    
    if '.pdf' not in title:
        title = title + '.pdf'
    
    content = {}
    
    #download as pdf
    pdfkit.from_url(url, title)

    #read in the text as pages
    with pdfplumber.open(title) as pdf:
                
        pages = pdf.pages
        for count,page in enumerate(pages):
            content[count+1] = page.extract_text()
        
    if download == 1:
        pass
    else:
        os.remove(title)
        
    return content
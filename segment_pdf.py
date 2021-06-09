# -*- coding: utf-8 -*-
"""
This function will access URLs that point to pdf files and get the text.

Normal and scanned pdfs are both supported.
The text will be broken down into pages to do analysis on each page later on.

Input: 'response' (the result of the requests.get method)
Output: a dictionary where keys are page numbers and values are text

Viktoria, June 2021

"""

import os
import pdfplumber
import ocrmypdf

def segment_pdf(title, response, download):
    
    if '.pdf' not in title:
        title = title + '.pdf'
    
    #Initiate an empty dictionary which will be populated
    content = {}
    
    #Open a file as myfile.pdf, weird characters can break the download
    open('myfile.pdf', 'wb').write(response.content)
    
    with pdfplumber.open('myfile.pdf') as pdf:
        
        page = pdf.pages[0]
        
        #Scanned pdfs give None for text
        text = page.extract_text()
        
        #Convert scanned pdfs
        if text is None: 
            if __name__ == '__main__':
                ocrmypdf.ocr('myfile.pdf', 'myfile_converted.pdf', deskew=True, progress_bar = False)
                document = 'myfile_converted.pdf'
                os.remove('myfile.pdf')
            
        else:
            document = 'myfile.pdf'
            
    #Populate the content dictionary: keys=page numbers, values=text
    with pdfplumber.open(document) as pdf:
                
        pages = pdf.pages
        for count,page in enumerate(pages):
            content[count+1] = page.extract_text()
            
    #If download was requested, save the file   
    if download == 1:
        os.rename(document, title)
    else:
        os.remove(document)
        
        
    return content
            
            
        
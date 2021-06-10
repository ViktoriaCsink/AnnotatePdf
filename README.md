# NLP_AnnotatePdf

This package will take a set of keyphrases and a list of URLs as input and produces annotated documents as output.

KeyphraseSearch_Tool.ipynb will:
- visit the URLs
- convert scanned pdfs, docx and html into pdf
- segment the documents into pages
- calculate the proportion of keyphrases in each topic on each page
- highlight these keyphrases with different colours for each topic
- if the % of keyphrases is > 5% on a page, then the document will be annotated with a note that specifies the relevant page numbers

Annotated documents arrive into the Results folder.

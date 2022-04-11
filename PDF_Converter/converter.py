from pdf2docx import Converter, parse

pdf_file = 'Jacob_CV.pdf'
word_file = 'Jacob_CV.docx'

# Convertor Method

cv = Converter(pdf_file)
cv.convert(word_file, start=0, end=None)
cv.close()

# parse method

parse(pdf_file, word_file, start=0, end=None)

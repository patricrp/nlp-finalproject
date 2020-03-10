import pandas as pd
from fpdf import FPDF 

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()


#Set Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'Social Media Report', 0, 1, 'C')

#Set first row of data
pdf.set_font('Arial', '', 14)
pdf.cell(10, 10, 'Total of tweets', 'C')

#Set graph
pdf.set_font('Arial', '', 14)
pdf.cell(0, 100, 'Categories distribution', 'C')
pdf.image('../barcategories.png', 20, 100, h=120)


pdf.output('report2.pdf', 'F')
import pandas as pd
from fpdf import FPDF 
import dataready as dataready
import train as train


pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()


#Set Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'Social Media Report', 0, 1, 'C')

#Set first row of data
pdf.set_font('Arial', '', 14)
volume, percentage = dataready.volumeCategories('../predicted.csv')
pdf.cell(10, 10, 'Total of tweets', 'C')

pdf.set_font('Arial', '', 14)
pdf.cell(2000, 30, 'volume', 'C')

#Set graph
#pdf.set_font('Arial', '', 14)
#pdf.cell(15, 150, 'Categories distribution', 'C')
#pdf.image('../output/barcategories.png', 20, 110, h=90)


pdf.output('report.pdf', 'F')
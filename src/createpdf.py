import pandas as pd
from fpdf import FPDF 
import funconstructor as fc


pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

#pdf.cell(ancho, alto, cadena, border, ln)
#Set Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 10, 'Social Media Report', 0, 1, 'C')

#Set first row of data
pdf.set_font('Arial', '', 14)
volume, percentage = fc.volumeCategories('../output/predicted.csv')
pdf.cell(95, 10, f'Total of tweets {volume}')

pdf.set_font('Arial', '', 14)
pdf.cell(95, 10, f'Percentage of tweets classificated {percentage}%')

pdf.set_font('Arial', '', 14)
pdf.cell(50, 10, 'Categories', 0, 1, 'C')
pdf.image('../output/barcategories.png', h=90)

pdf.set_font('Arial', '', 14)
pdf.cell(100, 10, 'Sentiment', 0, 1, 'C')
pdf.image('../output/barcategories.png', h=90)


pdf.output('../output/report.pdf', 'F')


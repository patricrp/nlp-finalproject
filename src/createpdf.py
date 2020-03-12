import pandas as pd
from fpdf import FPDF 
import funconstructor as fc


pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

#pdf.cell(ancho, alto, cadena, border, ln)
#Set Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'Social Media Report', 0, 1, 'C')

#Set first row of data
pdf.set_font('Arial', '', 14)
volume = 1000
percentage = 20
#volume, percentage = dr.volumeCategories('../predicted.csv')
pdf.cell(95, 10, f'Total of tweets {volume}')

pdf.set_font('Arial', '', 14)
pdf.cell(95, 10, f'Percentage of tweets classificated {percentage}%')


#Set graph
pdf.set_font('Arial', '', 16)
pdf.cell(190, 100, 'Categories distribution')
#pdf.image('../output/barcategories.png', 20, 110, h=90)


pdf.output('report.pdf', 'F')


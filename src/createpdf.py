import pandas as pd
from fpdf import FPDF 

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()


#Set Title
pdf.set_font('Roboto', 20)
pdf.cell(0, 10, 'Social Media Report', 'C')


pdf.image('graph.png')

pdf.output('report.pdf', 'F')
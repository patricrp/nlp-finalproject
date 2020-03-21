import pandas as pd
from fpdf import FPDF 
import graphext_funconstructor as fc


def newPDF():
    pdf = FPDF('P', 'mm', 'A4')

    pdf.add_page()

    #Set Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 10, 'Social Media Report', 0, 1, 'C')

    #First row of data
    pdf.cell(0, 10, ' ', 0, 1, 'C')

    pdf.set_font('Arial', '', 14)
    volume, percentage = fc.volumeCategories('../output/predicted.csv')
    pdf.cell(95, 10, f'Total of tweets {volume}')

    pdf.set_font('Arial', '', 14)
    pdf.cell(95, 10, f'Percentage of tweets classificated {percentage}%', 0, 1, 'C')

    pdf.cell(0, 10, ' ', 0, 1, 'C')
    
    
    #Categories
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 10, 'Categories', 0, 1, 'C')
    pdf.image('../output/barcategories.png', 40, h=90)
    
    
    pdf.cell(0, 10, ' ', 0, 1, 'C')
    #Sentiment
    pdf.set_font('Arial', '', 14)
    pdf.cell(95, 10, 'Sentiment', 0, 0, 'C')
    pdf.image('../output/sentimentAnalysis.png', 5, 170, h=70)

    pdf.set_font('Arial', '', 14)
    pdf.cell(95, 10, 'Sentiment by Category', 0, 1, 'C')
    pdf.image('../output/sentimentcat.png', 100, 170, h=70)


    pdf.output('../output/report.pdf', 'F')

    print('Your PDF is ready')


    
    

    


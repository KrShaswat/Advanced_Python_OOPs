import webbrowser
from os import path,getenv

from fpdf import FPDF

from filestack import Client

from dotenv import load_dotenv
load_dotenv()


class ReportPdf:
    """
    Creates a PDF report with home icon, bill duration, Flatmate names and pay split
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Create a pdf document
        pdf = FPDF(orientation="P", unit='pt', format='A4')

        # add page to doc
        pdf.add_page()

        # Add Image
        pdf.image("files/house.png", w=30, h=30)

        # Set the default font for pdf
        pdf.set_font(family="Times", size=24, style='B')

        # Add the Title
        # w = 0  for cell to take entire length
        pdf.cell(w=0, h=80, txt="Flatmate's Bill", border=0, align="C", ln=1)

        # Font change for stuff
        pdf.set_font(family="Times", size=14, style='B')

        # Insert Period label and Value
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Font change for stuff
        pdf.set_font(family="Times", size=14)

        # Insert Flatmate1
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=str(flatmate1.pays(bill=bill, flatmate=flatmate2)), border=0, ln=1)

        # Insert Flatmate2
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=str(flatmate2.pays(bill=bill, flatmate=flatmate1)), border=0, ln=1)

        pdf.output(f"files/{self.filename}")

        # Here Ardit changes Directory to files/
        # os.chdir("files")
        # I prefer it this way
        # webbrowser.open('file://' + path.realpath(f"files/{self.filename}"))

    def url_print(self):
        client = Client(getenv('API_KEY'))

        new_filelink = client.upload(filepath=f'files/{self.filename}')
        print("The pdf file link: "+new_filelink.url)
from flat import Bill, Flatmate
from report import ReportPdf,FileSharer

from dotenv import load_dotenv
load_dotenv()

# CLI
flatmate1_name = input("Hi, Whats your name? ")
time_flatmate1 = float(input("How many days did you stay in flat? "))
flatmate2_name = input("Whats your flatmate's name? ")
time_flatmate2 = float(input(f"How many days did {flatmate2_name} stay in flat? "))

bill_amount = float(input("Whats your bill amount? "))
bill_duration = input("Your bill Duration (example- August 2021)? ")

# check
the_bill = Bill(amount=bill_amount, period=bill_duration)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=time_flatmate1)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=time_flatmate2)

# CLI output
print(f"{flatmate1.name} pays: {flatmate1.pays(bill=the_bill, flatmate=flatmate2)}")
print(f"{flatmate2.name} pays: {flatmate2.pays(bill=the_bill, flatmate=flatmate1)}")

pdf_report = ReportPdf(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

# Print url
file_link = FileSharer(file_path=f'files/{pdf_report.filename}')
print(file_link.share())
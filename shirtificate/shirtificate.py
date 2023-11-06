from fpdf import FPDF

name = input("Name: ").strip()
shirt_print = name + " took CS50"

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", 10, 70, 190)
pdf.set_font("helvetica", style="", size=40)
pdf.cell(h=50,txt="CS50 Shirtificate", center=True)
pdf.set_font("helvetica", style="", size=20)
pdf.set_text_color(255,255,255)
pdf.cell(h=250,txt=shirt_print, center=True)
pdf.output("shirtificate.pdf")
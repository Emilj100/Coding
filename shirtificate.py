from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 20, "CS50 Shirtificate")
pdf.output("tuto1.pdf")

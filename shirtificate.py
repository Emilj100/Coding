from fpdf import FPDF

user_name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(70)
pdf.cell(40, 20, "CS50 Shirtificate")
pdf.image("image.png", x=50, y=40, w=100)
pdf.set_text_color(255, 255, 255)
pdf.cell(-40)
pdf.cell(20, 130, user_name)
pdf.output("shirtificate.pdf")

from fpdf import FPDF

user_name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

pdf.set_font("helvetica", "B", 24)
pdf.cell(0, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

pdf.image("shirtificate.png", x=pdf.epw / 2 - (pdf.epw * 0.5) / 2, y=60, w=pdf.epw * 0.5)

pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
text = f"{user_name} took CS50"
text_width = pdf.get_string_width(text)
pdf.text(x=(pdf.w - text_width) / 2, y=140, txt=text)

pdf.output("shirtificate.pdf")

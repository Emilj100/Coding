from fpdf import FPDF

user_name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

pdf.set_font("helvetica", "B", 24)
pdf.cell(0, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

image_width = pdf.epw * 0.8

image_x = (pdf.w - image_width) / 2

image_y = 60

pdf.image("shirtificate.png", x=image_x, y=image_y, w=image_width)


pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
text = f"{user_name} took CS50"

text_width = pdf.get_string_width(text)

text_x = (pdf.w - text_width) / 2

text_y = image_y + (image_width * 0.5)


pdf.text(x=text_x, y=text_y, txt=text)

pdf.output("shirtificate.pdf")

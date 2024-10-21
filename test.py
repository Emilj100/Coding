from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Set font for the header
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")
        self.ln(20)  # Space below the title

    def add_shirt(self, name):
        # Add shirt image
        self.image("shirtificate.png", x=25, y=60, w=160)

        # Set the font for the name and position it on top of the shirt
        self.set_font("Arial", "B", 36)
        self.set_text_color(255, 255, 255)  # White color
        self.cell(0, 230, name, align="C")  # Adjust position with cell

# Prompt for the user's name
name = input("What's your name? ")

# Create PDF
pdf = Shirtificate()
pdf.set_auto_page_break(auto=False)  # Disable auto page breaks
pdf.add_page(format="A4")

# Add the shirt and the name
pdf.add_shirt(name)

# Output the PDF
pdf.output("shirtificate.pdf")

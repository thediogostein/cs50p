from fpdf import FPDF


class PDF(FPDF):
    def title(self, title):
        self.set_margin(0)
        self.set_font("helvetica", "B", 48)
        self.cell(210, 80, title, align="C")
        self.ln(50)

    def shirt(self, name):
        self.image("shirtificate.png", w=190, x=10, y=70)
        self.set_font("helvetica", "B", 28)
        self.set_y(100)
        self.set_text_color(255, 255, 255)
        self.cell(210, 50, f"{name} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.title("CS50 Shirtificate")
    pdf.shirt(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

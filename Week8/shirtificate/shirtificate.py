from fpdf import FPDF

class PDF(FPDF):
    def shirt_text(self, text):
        self.set_font("helvetica", "B", 22)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 120)
        self.cell(0, 0, text, align="C")



def main():
    name = input("Name: ")
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 32)
    pdf.cell(0, 30, "CS50 Shirtificate", ln=True, align="C")
    pdf.image("shirtificate.png", x=10, y=40, w=190)
    pdf.shirt_text(f"{name} took CS50")
    pdf.output('shirtificate.pdf')




if __name__ == "__main__":
    main()

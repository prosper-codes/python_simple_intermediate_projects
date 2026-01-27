
from fpdf import  FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index , row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times",style="B",size=13)
    pdf.cell(
        w=0,
        h=12,
        text=row["Topic"],
        align="L",
        new_x="LMARGIN",
        new_y="NEXT"
    )
    for y in range(20,198,10):
        pdf.line(10,y,200,y)

    for i in range(row["Pages"]-1):
        pdf.add_page()

        pdf.ln(277)
        pdf.cell(
            w=0,
            h=12,
            text=row["Topic"],
            align="L",
            new_x="LMARGIN",
            new_y="NEXT"
        )

        for y in range(20, 198, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
from fpdf import FPDF
import csv


class PDF(FPDF):

    def header(self):
        self.set_font("helvetica", "", 16)
        width = self.get_string_width(self.title) + 6
        self.set_x((self.w - width) / 2)
        self.set_draw_color(90, 100, 160)
        self.set_fill_color(50, 20, 210)
        self.set_text_color(0, 0, 0)
        self.set_line_width(1)
        self.cell(
            width,
            10,
            self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 12)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


class CSV():

    # ---- READ CSV (unchanged logic) ----
    with open("books.txt", encoding="utf8") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))

    pdf = FPDF()
    pdf.set_font("Times", size=15)
    pdf.add_page()


    usable_width = pdf.w - 2 * pdf.l_margin
    num_cols = len(data[0])
    col_widths = [usable_width / num_cols] * num_cols

    pdf.set_draw_color(200, 0, 5)
    pdf.set_line_width(0.25)

    with pdf.table(
        borders_layout="NO_HORIZONTAL_LINES",
        cell_fill_color=(0, 220, 120),
        col_widths=col_widths,   # 🔧 optimized
        line_height=9,
        width=usable_width,      # 🔧 optimized
    ) as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    pdf.output("table.pdf")

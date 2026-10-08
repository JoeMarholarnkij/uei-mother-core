import os
from fpdf import FPDF

class RFQ_PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 8)
        # Avoid print-overlap by keeping cell height small
        self.cell(0, 8, "JOE'S BROTHER CLEAN ENERGY DIVISION - REQUEST FOR QUOTATION", align='L', new_x="LMARGIN", new_y="NEXT")
        self.line(15, 17, 195, 17)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def build_pdf():
    md_file = "/Users/joem/workspaces/deploy_mother_core/docs/2026-06-19_NV2_BIONIC_TURBINE_RFQ_ENGLISH.md"
    pdf_file = "/Users/joem/workspaces/deploy_mother_core/docs/2026-06-19_NV2_BIONIC_TURBINE_RFQ_ENGLISH.pdf"
    
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    pdf = RFQ_PDF()
    pdf.set_margins(15, 20, 15)
    pdf.add_page()
    
    for line in lines:
        line_str = line.strip()
        if not line_str:
            pdf.ln(3)
            continue
            
        if line_str.startswith("# "):
            title = line_str.replace("# ", "")
            pdf.set_font('Helvetica', 'B', 16)
            pdf.cell(pdf.epw, 10, title, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
        elif line_str.startswith("## "):
            section = line_str.replace("## ", "")
            pdf.set_font('Helvetica', 'B', 12)
            pdf.cell(pdf.epw, 8, section, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
        elif line_str.startswith("### "):
            sub = line_str.replace("### ", "")
            pdf.set_font('Helvetica', 'B', 10)
            pdf.cell(pdf.epw, 6, sub, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
        elif line_str.startswith("* "):
            bullet = line_str.replace("* ", "- ")
            pdf.set_font('Helvetica', '', 10)
            pdf.multi_cell(pdf.epw, 5, bullet)
        else:
            pdf.set_font('Helvetica', '', 10)
            pdf.multi_cell(pdf.epw, 5, line_str)
            
    pdf.output(pdf_file)
    print(f"✅ PDF generated at: {pdf_file}")

if __name__ == "__main__":
    build_pdf()

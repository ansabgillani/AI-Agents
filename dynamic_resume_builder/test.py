from weasyprint import HTML
import sys
import os

def html_to_pdf(input_path: str = "test.html", output_path: str = "test.pdf"):
    """
    Convert an HTML file to PDF using WeasyPrint.
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    HTML(filename=input_path).write_pdf(output_path)
    print(f"Successfully generated PDF: {output_path}")

if __name__ == "__main__":
    # Usage: python convert.py [input_html] [output_pdf]
    input_file = sys.argv[1] if len(sys.argv) > 1 else "test.html"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "test.pdf"

    try:
        html_to_pdf(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

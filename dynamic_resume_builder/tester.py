#!/usr/bin/env python3
import html
from weasyprint import HTML
import os
import json
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_resume(json_path: str,
                    template_name: str,
                    output_path: str) -> None:
    # 1. Load data from JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Create Jinja2 environment, loading templates from current dir
    env = Environment(
        loader=FileSystemLoader(searchpath='.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # 3. Load your template
    template = env.get_template(template_name)

    # 4. Render the template with your data under a 'person' variable
    rendered_html = template.render(person=data)

    # 5. Write the output HTML
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print(f"Generated {output_path} from {json_path} and {template_name}")

def html_to_pdf(input_path: str = "test.html", output_path: str = "test.pdf"):
    """
    Convert an HTML file to PDF using WeasyPrint.
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    HTML(filename=input_path).write_pdf(output_path)
    print(f"Successfully generated PDF: {output_path}")

if __name__ == '__main__':

    json_file     = "resume.json"
    template_file = "template_.html"
    output_file   = "temp.html"

    generate_resume(json_file, template_file, output_file)
    html_to_pdf(output_file, "resume.pdf")

    # Clean up the temporary HTML file
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Removed temporary file: {output_file}")
    else:
        print(f"Temporary file {output_file} does not exist.")
        

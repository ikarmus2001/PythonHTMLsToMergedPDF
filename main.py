from os import getcwd, path, listdir
from weasyprint import HTML
from PyPDF2 import PdfMerger
from io import BytesIO

def html_to_pdf(input_html) -> BytesIO:
    pdf_bytes_io = BytesIO()
    HTML(filename=input_html).write_pdf(pdf_bytes_io)
    pdf_bytes_io.seek(0)
    return pdf_bytes_io


def merge_html_to_pdf(html_pages, output_filename) -> None:
    docs = []
    for h in html_pages:
        docs.append(html_to_pdf(h))
    
    merger = PdfMerger()
    for d in docs:
        merger.append(d)
    merger.write(output_filename)
    merger.close()
        

def get_html_filenames(directory) -> [str]:
    try:
        files = listdir(directory)

        # Filter files with '.html' extension, add full path and fix slashes
        return [path.join(directory, file).replace("\\", "/") for file in files if file.endswith('.html')]
    except Exception as e:
        print(f'Error: {e}')
        return []

if __name__ == "__main__":
    directory_path = getcwd()
    html_pages = get_html_filenames(directory_path)
    print(len(html_pages))

    output_pdf = 'merged_output.pdf'

    merge_html_to_pdf(html_pages, output_pdf)

import io
import re

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

pattern_references = re.compile(r'(.*)^\s*references.*', re.DOTALL | re.MULTILINE | re.IGNORECASE)
pattern_acknowledgments = re.compile(r'(.*)^\s*acknowledg[e]?ments.*', re.DOTALL | re.MULTILINE | re.IGNORECASE)

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass

    
def extract_text(source_path):
    # scan only source_path directory
    for root, dirs, files in os.walk(source_path):
        for name in files:
            if name.endswith('.pdf'):
                file = os.path.join(root, name)
                print(file)

                if not os.path.isfile(file.split('.pdf')[0]+'.txt'):
                    
                    pdf_file = os.path.join(root, file)
                    pdf_file_content = convert_pdf_to_txt(pdf_file)
                    
                    match_ref = pattern_references.match(pdf_file_content)
                    match_ack = pattern_acknowledgments.match(pdf_file_content)

                    if match_ref:
                        text_file_content = match_ref.group(1)
                    elif match_ack:
                        text_file_content = match_ack.group(1)
                    else:
                        text_file_content = pdf_file_content
                        
                        
                    # write text file
                    text = os.path.join(root, file.replace('.pdf', '.txt'))
                    delete_file(text)
                    
                    # Replace unusual text
                    text_file_content = replace_unusual_text(text_file_content)

                    # Replace Greek symbols
                    text_file_content = replace_greek_characters(text_file_content)

                    # Write to file
                    with open(text, 'w', encoding='utf8') as text_file:
                        text_file.write(text_file_content)

                    # Filter material/methods
                    filter_file(text)
                else:
                    print(file.split('.pdf')[0]+'.txt already exists')

#         break

def replace_greek_characters(text_file_content):
    alpha = re.compile(r'(?![A-Z]{2,})-a\b')
    text_file_content = re.sub(alpha,'-alpha', text_file_content)
    
    beta = re.compile(r'(?![A-Z]{2,})-b\b')
    text_file_content = re.sub(beta,'-beta', text_file_content)
    
    gamma = re.compile(r'(?![A-Z]{2,})-c\b')
    text_file_content = re.sub(gamma,'-gamma', text_file_content)
    
    return text_file_content

def replace_unusual_text(text_file_content):
    newline_pattern = re.compile(r'(?![A-Z]{2,})-\n')
    text_file_content = re.sub(newline_pattern,'',text_file_content)
    
    etal_pattern = re.compile(r'(\([^(]+et al[^)]+\))')
    text_file_content = re.sub(etal_pattern,'',text_file_content)
    
    fig_pattern = re.compile(r'(\(.*?[Ff]ig.*?\))')
    text_file_content = re.sub(fig_pattern,'',text_file_content)
    
    fig_pattern2 = re.compile(r'([Ff]ig\. [0-9][a-zA-Z]*)')
    text_file_content = re.sub(fig_pattern2,'',text_file_content)
    
    table_pattern = re.compile(r'(\(.*?[Tt]able.*?\))')
    text_file_content = re.sub(table_pattern,'',text_file_content)
    
    doi_pattern = re.compile(r'([^\s]*doi[^\s]*)')
    text_file_content = re.sub(doi_pattern,'',text_file_content)
    
    pval_pattern = re.compile(r'(\b[Pp](val)*[\s]*[0-9.]*\b)')
    text_file_content = re.sub(pval_pattern,'',text_file_content)
    
    return text_file_content

def methodology_list():
    methodology_raw = """Materials and methods
    Materials and Methods
    Experimental procedures
    Materials and methods
    Methods
    MATERIALS AND METHODS
    Patients and Methods
    Method 
    Materials and Methods
    Materials and methods
    Material and methods
    METHODS AND MATERIALS
    Methods and materials
    Materials"""

    methodology_list =[]
    methodology_split = methodology_raw.split("\n")

    for x in methodology_split:
        methodology_list.append(x.strip())
    
    return methodology_list

def results_list():
    results_list = ['Results','RESULTS','RESULTS AND DISCUSSION']
    
    return results_list

def filter_file(text):
    if not os.path.isfile(text.split('.txt')[0]+'_output.txt'):
            
        with io.open(text.split('.txt')[0]+'_output.txt', 'w', encoding='utf-8') as output_file:
            with io.open(text,'r', encoding='utf-8') as input_data:
                for line in input_data:
                    line=line.lstrip('0123456789.- ')
                    line=line.rstrip()
                    if len(line) > 2:
                        if any(item.lower().startswith(line.strip().lower()) for item in methodology_list()):
                            break

                        # Remove all characters except numbers, letters, punctuations and hyphens
                        line = re.sub("[^.,a-zA-Z0-9 \n\.\-]", '', line)
                        output_file.write(line+" ")

                for line in input_data:
                    line=line.lstrip('0123456789.- ')
                    line=line.rstrip()
                    if len(line) > 2:
                        if any(item.lower().startswith(line.strip().lower()) for item in results_list()):
                            break
                for line in input_data:
                    line=line.lstrip('0123456789.- ')
                    line=line.rstrip()
                    if len(line) > 2:
                        # Remove all characters except numbers, letters, punctuations and hyphens
                        line = re.sub("[^.,a-zA-Z0-9 \n\.\-]", '', line)
                        output_file.write(line+" ")

if __name__ == '__main__':
    # Path to PDF files
    path = "C:\\TNO\\2019\\20190101_SRP_FoodAllergy\\PDF_miner\\3B"
    extract_text(path)

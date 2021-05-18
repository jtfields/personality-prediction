import os
import PyPDF2
directory = "/Users/johnfields/Library/Mobile Documents/com~apple~CloudDocs/Education/Marquette/iPeer/WisconsinVeteransMuseum/OperationOIF-OperationOEF/"
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pathname = os.path.join(directory, filename)
        reader = PyPDF2.PdfFileReader(pathname)
        writer = PyPDF2.PdfFileWriter()
        my_page = reader.getPage(5)
        writer.addPage(my_page)
        print('*',filename,my_page.extractText(), file=open('output.txt','a'))
        continue
    else:
        continue

a_file = open("output.txt", "r")

string_without_line_breaks = ""
for line in a_file:
  stripped_line = line.rstrip()
  string_without_line_breaks += stripped_line
a_file.close()

print(string_without_line_breaks.split('*'),file=open('output2.txt','a'))
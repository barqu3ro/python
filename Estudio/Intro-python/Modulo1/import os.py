import os 
import PyPDF2

pdf_directory = 'Estudio/files/'

pdf_files = [file for file in os.listdir(pdf_directory)]

if len(pdf_files) == 0:
    print ('Error al leer archivos - Not found')
    exit()

# Para qué ordenarlo?
pdf_files.sort()

merger = PyPDF2.pdf_merger()

for pdf_file in pdf_files:
    pdf_file_path = os.path.join(pdf_directory,pdf_file)
    merger.append(pdf_file_path)

output_pdf = 'Estudio/files/result/merged.pdf'

pdf_merger.write(output_pdf)

pdf_merger.close()

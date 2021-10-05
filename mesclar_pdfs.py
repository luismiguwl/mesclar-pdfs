from os import getcwd, chdir
from PyPDF2 import PdfFileMerger
from os import getcwd
from os import listdir
from instalador import instalar_dependencias

# Descomente caso já possua o PyPDF2 :)
# instalar_dependencias()

chdir('./')

arquivos_em_pdf = []
for nome_do_arquivo in listdir(getcwd()):
    if nome_do_arquivo.lower().endswith('.pdf'):
        arquivos_em_pdf.append(nome_do_arquivo)
    
merger = PdfFileMerger()

for pdf in arquivos_em_pdf:
    merger.append(pdf)
    
merger.write('arquivos_mesclados.pdf')
merger.close()
#split input .pdf up into pages as preprocessing measure
from PyPDF2 import PdfFileWriter, PdfFileReader

#point to directory with .pdf
#later, make this user enterable for custom .pdf
dir = './dev/training_data/Cicero_Dataset/'
file_name = 'Cicero_Orations.pdf'
dest = 'cicero_pages/'

inputpdf = PdfFileReader(open(dir+file_name, "rb"))

for page in range(inputpdf.numPages):
	output = PdfFileWriter()
	output.addPage(inputpdf.getPage(page))
	with open(dir+dest+'page%s.pdf' % page, "wb") as outputStream:
		output.write(outputStream)


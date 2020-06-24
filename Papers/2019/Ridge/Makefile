all:
	pdflatex Presentation.tex

clear:
	texclear *.tex

epstopdf:
	bash -ic 'for i in $$(find . -name "*.eps"); do epstopdf $$i; done'

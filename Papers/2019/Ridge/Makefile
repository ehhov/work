all:
	pdflatex Presentation.tex

clear:
	texclean *.tex

epstopdf:
	bash -ic 'for i in $$(find . -name "*.eps"); do epstopdf $$i; done'

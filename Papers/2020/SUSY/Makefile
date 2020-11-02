bib:
	texclear paper
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper

p:
	pdflatex presentation
	pdflatex presentation

clean:
	texclear *.tex

open:
	echo 'nvim -p paper.tex refs.bib presentatoin.tex' | xclip

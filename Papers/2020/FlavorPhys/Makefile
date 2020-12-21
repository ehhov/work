all: paper.pdf

paper.pdf: paper.tex refs.bib local.bst
	texclear paper
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	texclear paper

c: clean

clean:
	texclear *.tex

.PHONY: all c clean

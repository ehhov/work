all: paper.pdf

paper.pdf: paper.tex refs.bib local.bst
	texclean paper
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	texclean paper

p:
	pdflatex presentation
	pdflatex presentation
	texclean presentation

clean:
	texclean *.tex

.PHONY: clean p

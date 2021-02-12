all: paper.pdf

paper.pdf: paper.tex refs.bib local.bst
	texclean paper
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	texclean paper

c: clean

clean:
	texclean *.tex

.PHONY: all c clean

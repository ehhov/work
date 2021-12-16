default: paper.pdf

all: gnu paper.pdf

paper.pdf: paper.tex gnuplot
	pdflatex paper
	pdflatex paper
	texclean paper

gnu:
	./gnuplot

clean:
	texclean *.tex

.PHONY: gnu clean all

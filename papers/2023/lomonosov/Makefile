TEXFIGFILES = $(shell ls figures/*.tex)
TEXFIGURES = $(TEXFIGFILES:.tex=.pdf)


default: all

all: presentation.pdf

presentation.pdf: presentation.tex $(TEXFIGURES)
	pdflatex presentation
	pdflatex presentation
	texclean presentation

figures/%.pdf: figures/%.tex
	pdflatex -output-directory figures $<
	texclean $<

clean:
	texclean presentation $(TEXFIGFILES)

.PHONY: clean default all

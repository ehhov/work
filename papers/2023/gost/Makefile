PAPER = paper
PRESENTATION = presentation
TEXFIGURES = $(shell find figures -name "*.tex")
TEXFIGURESPDF = $(TEXFIGURES:.tex=.pdf)
TEXFILES = tex/*.tex
SUPPFILES = references.bib definitions.sty local.sty gost.bst


default: paper

all: paper presentation

paper: $(PAPER).pdf

presentation: $(PRESENTATION).pdf

$(PAPER).pdf: $(PAPER).tex $(TEXFIGURESPDF) $(TEXFILES) $(SUPPFILES)
	texclean $(PAPER)
	pdflatex $(PAPER)
	pdflatex $(PAPER)
	bibtex $(PAPER)
	pdflatex $(PAPER)
	pdflatex $(PAPER)
	texclean $(PAPER)

$(PRESENTATION).pdf: $(PRESENTATION).tex $(TEXFIGURESPDF)
	pdflatex $(PRESENTATION)
	pdflatex $(PRESENTATION)
	texclean $(PRESENTATION)

figures/%.pdf: figures/%.tex
	pdflatex -output-directory $(dir $<) $<
	texclean $<

clean:
	texclean $(PAPER) $(PRESENTATION) $(TEXFIGURES)

.PHONY: clean default all paper presentation

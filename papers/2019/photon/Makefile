Document="Document"
Presentation="Presentation"
tex="pdflatex"
bib="bibtex"
texflags="-file-line-error -interaction=nonstopmode"

open:
	@echo 'You can now paste from Primary of X11 to edit the files mentioned below'
	echo vim -p PhysVac.tex CasimirEff.tex Document.tex Refs.bib | xclip 

d:
	texclean $(Document)
	$(tex) $(texflags) $(Document)
	$(bib) $(Document)
	$(tex) $(texflags) $(Document)
	$(tex) $(texflags) $(Document)
p:
	$(tex) $(Presentation)
	$(tex) $(Presentation)

clear:
	texclean *.tex

.PHONY: d, p, clear, open

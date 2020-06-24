Document="Document"
tex="pdflatex"
bib="bibtex"
texflags="-file-line-error -interaction=nonstopmode"

open:
	@echo 'You can now paste from Primary of X11 to edit the files mentioned below'
	echo vim -p Document.tex tune.sty Refs.bib | xclip 

d:
	bash -ic 'texclear $(Document)'
	$(tex) $(texflags) $(Document)
	$(bib) $(Document)
	$(tex) $(texflags) $(Document)
	$(tex) $(texflags) $(Document)

clear:
	texclear *.tex

.PHONY: d, clear, open

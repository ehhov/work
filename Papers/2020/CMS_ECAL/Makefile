bib:
	bash -ic 'texclear CMS_ECAL'
	pdflatex CMS_ECAL
	bibtex CMS_ECAL
	pdflatex CMS_ECAL
	pdflatex CMS_ECAL

clean:
	texclear *.tex

open:
	echo 'vim -p CMS_ECAL.tex tune.sty Refs.bib' | xclip



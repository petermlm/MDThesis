ARGS=-file-line-error -halt-on-error
DOC=comments

all:
	pdflatex $(ARGS) $(DOC)
	makeglossaries $(DOC)
	pdflatex $(ARGS) $(DOC)

clean:
	rm -f $(DOC).aux
	rm -f $(DOC).glg
	rm -f $(DOC).glo
	rm -f $(DOC).gls
	rm -f $(DOC).ist
	rm -f $(DOC).log
	rm -f $(DOC).pdf
	rm -f texput.log

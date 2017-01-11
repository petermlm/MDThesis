OUTDIR=bin
DOC=comments

OUTPDF=$(OUTDIR)/$(DOC).pdf
PDF=$(DOC).pdf

PDF_ARGS=-file-line-error -halt-on-error -output-directory=$(OUTDIR)
GLS_ARGS=-d $(OUTDIR)

all:
	mkdir -p bin
	pdflatex $(PDF_ARGS) $(DOC)
	makeglossaries $(GLS_ARGS) $(DOC)
	bibtex $(OUTDIR)/$(DOC)
	pdflatex $(PDF_ARGS) $(DOC)
	pdflatex $(PDF_ARGS) $(DOC)
	mv $(OUTPDF) $(PDF)

clean:
	rm -rf bin
	rm -f $(PDF)

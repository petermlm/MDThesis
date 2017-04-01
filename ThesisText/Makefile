# This file used to be better. But after adding UE's model I gave up on
# organization.

# OUTDIR=bin
OUTDIR=.
DOC=thesis_text

OUTPDF=$(OUTDIR)/$(DOC).pdf
PDF=$(DOC).pdf

PDF_ARGS=-file-line-error -halt-on-error -output-directory=$(OUTDIR)
GLS_ARGS=-d $(OUTDIR)

all:
	# mkdir -p bin
	echo "==============================================================================="
	echo "== PDF Latex"
	echo "==============================================================================="
	xelatex $(PDF_ARGS) $(DOC)
	echo "==============================================================================="
	echo "== Make Glossaries"
	echo "==============================================================================="
	# makeglossaries $(GLS_ARGS) $(DOC)
	echo "==============================================================================="
	echo "== Bib Tex"
	echo "==============================================================================="
	bibtex $(OUTDIR)/$(DOC)
	echo "==============================================================================="
	echo "== PDF Latex"
	echo "==============================================================================="
	xelatex $(PDF_ARGS) $(DOC)
	echo "==============================================================================="
	echo "== PDF Latex"
	echo "==============================================================================="
	xelatex $(PDF_ARGS) $(DOC)
	# mv $(OUTPDF) $(PDF)

clean:
	# After putting the UE model, things became too messy, so no clean
	# rm -rf $(OUTDIR)
	# rm -f $(PDF)
	rm abstract.aux
	rm acronimos.aux
	rm agradecimentos.aux
	rm sumario.aux
	rm thesis_text.aux
	rm thesis_text.bbl
	rm thesis_text.blg
	rm thesis_text.glsdefs
	rm thesis_text.idx
	rm thesis_text.lof
	rm thesis_text.log
	rm thesis_text.lot
	rm thesis_text.out
	rm thesis_text.pdf
	rm thesis_text.toc

THESIS_PATH=/home/lg/cloud/phd/Dropbox/phd/thesis/tex
cd $THESIS_PATH
p=phdThesisLG
echo ">>>>>>>>>>>>>> " $p

echo ">>>" "pdflatex $p.tex" 
pdflatex -halt-on-error $p.tex  
echo ">>>" "bibtex $p.aux"
bibtex $p.aux; 
echo ">>>" "pdflatex $p.aux;"
pdflatex -halt-on-error $p.tex  
pdflatex -halt-on-error $p.tex  

rm -f *.dvi *.lof *.lot *.bbl *.blg *.out *.aux *.log *.lyx~ *.txt *.toc *.*# &> /dev/null &
rm -f *.nav *.snm &> /dev/null &
read

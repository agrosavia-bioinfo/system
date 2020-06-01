ext=`echo $1|cut -d'.' -f2`
input=$1
output=$2
if [ $ext == "pdfx" ]; then
	output=`echo $1|cut -d'.' -f1`".pdf"
fi
#pdf2ps -dLanguageLevel=3 $name.pdf
pdf2ps $input /tmp/b.ps
ps2pdf  -dAutoRotatePages=/None /tmp/b.ps $output


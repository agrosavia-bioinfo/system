#!/bin/bash
pdfpath=/home/lg/tmp/config/pdfoption

arg=$1
first=`echo ${arg:0:1}`
if [ "$first" == '-' ]; then
	case $1 in
		'-f')  echo "FoxitReader  " > /home/lg/tmp/config/pdfoption;;
		'-o')  echo "okular  " > /home/lg/tmp/config/pdfoption;;
		'-O')  echo "okular --unique " > /home/lg/tmp/config/pdfoption;;
		'-q')  echo "qpdfview --unique " > /home/lg/tmp/config/pdfoption;;
		'-M')  echo "mupdf -A 0 -F -r 50 " > $pdfpath;;
		'-m')  echo "mupdf -G -r 50 " > $pdfpath;;
		'-mf')  echo "mupdf -G -r 100 " > $pdfpath;;
		'-z')  echo "zathura" > $pdfpath;;
		#'-k')  echo "konqueror --silent --mimetype text/pdf" > $pdfpath;;
		'-k')  echo "konqueror --silent --mimetype application/pdf" > $pdfpath;;
		'-e')  echo "evince " > $pdfpath;;
		'-g')  echo "gpicview " > $pdfpath;;
		'-v')  echo "epdfview " > $pdfpath;;
		'-V')  echo "ViewPDF " > $pdfpath;;
		'-a')  echo "acroread " > $pdfpath;;
		'-A')  echo "acroread -optimizeForSpeed " > $pdfpath;;
	esac
	exit
fi
viewer=`cat  $pdfpath`
cmm="$viewer '$1'"
echo $cmm > /tmp/a

echo $cmm
eval $cmm  



input=$1
output=$2
quality=$3
cmm="gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/$quality -sOutputFile=$output $input"
#$cmm="gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/$quality -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$output"
echo $cmm
eval $cmm

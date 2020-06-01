# Reduce the size of a pdf when it was done with images
input=$1
output=$2

convert -density 200x200 -quality 60 -compress jpeg $input.pdf $output.pdf

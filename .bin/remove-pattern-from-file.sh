PATTERN=$1
FILE=$2

CMM="sed -i '/$1/d' $FILE"
echo $CMM
eval $CMM

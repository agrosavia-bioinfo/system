DIR=$1
parent=`basename $PWD`
echo $parent
date=`date "+%b%d"`
name=$parent-$DIR-$date
cmm="find $DIR -maxdepth 1 -type f -print0|tar -zcvf $name-onlySources.tgz --null -T -"
echo $cmm
eval $cmm
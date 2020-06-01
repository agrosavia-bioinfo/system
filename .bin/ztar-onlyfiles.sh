parent=`basename $PWD`
echo $parent
date=`date "+%b%d"`
name=$parent-$1-$date
find $parent -maxdept 1 type f -print0|tar -zcvf $name-onlySources.tgz --null -T -


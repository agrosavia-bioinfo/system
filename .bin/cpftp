files=$1
dir=$2
user=$3

if [ "$3" == '' ]; then
	user=lg
fi
if [ "$2" == '' ]; then
	dir=/home/bioinfo/dokuwiki/downloads
fi

cmd="rsync -av $files $user@ftpbio:$dir"

echo $cmd
$cmd

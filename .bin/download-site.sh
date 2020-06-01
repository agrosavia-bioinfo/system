httrack "$1" -O "$1" "+*$2*" -v

httrack "http://www.all.net/" -O "/tmp/www.all.net" "+*.all.net/*" -v

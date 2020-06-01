mkfs -q /dev/ram1 40000
mkdir -p /ramcache
mount /dev/ram1 /ramcache

df -H|grep ramcache

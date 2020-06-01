user=$1
pasw=$1
useradd -s /bin/bash -d /home/bio/$1 -m $1
echo "$user:$pasw" | chpasswd

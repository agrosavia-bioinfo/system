a=`xclip -o`
echo $a>/tmp/a
#echo $a|tr '{S  }' '\n' < /tmp/a > /tmp/b
sed -i 's/S\xef\x81\x93\s/\n/g' /tmp/a
cat /tmp/a|xclip -sel pri

#!/usr/bin/env bash
a=`xclip -o`
echo $a>/tmp/a

# Remove chars
##echo $a|tr '{S  }' '\n' < /tmp/a > /tmp/b
sed -i 's/S\xef\x81\x93\s/\n/g' /tmp/a
cat /tmp/a|xclip -sel pri

## Translate English to Spanish
#LANG=en
#WORD="$(xsel -o)"
#echo $MEANING>/home/lg/a
#URL="$(wget -U "Mozilla/5.0" -qO - "http://translate.googleapis.com/translate_a/single?client=gtx&sl=$LANG&tl=es&dt=t&q=$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')"
#MEANING=$URL
#echo $MEANING|xclip -i
#echo $MEANING>/home/lg/a
#a=`xclip -o`
#echo $a

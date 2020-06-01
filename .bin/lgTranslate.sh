#!/usr/bin/env bash
## Modified to only one word (for many words, error adding "en" ????)

LANG=en
WORD="$(xsel -o)"

URL="http://translate.googleapis.com/translate_a/single?client=gtx&sl=$LANG&tl=es&dt=t&q="
#URLTEST=$(wget -U "Mozilla/5.0" -qO - "$URL$(xsel -o | sed "s/[\"<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')
URLTEST=$(wget -U "Mozilla/5.0" -qO - "$URL$(xsel -o|sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')
#URLTEST=$(wget -U "Mozilla/5.0" -qO - "$URL$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')

# Get meaning and remove a last word "ghost" "en"
MEANING=`echo $URLTEST| awk '{$NF="";sub(/[ \t]+$/,"")}1'`
MEANING=`echo $MEANING| awk '{$NF="";sub(/[ \t]+$/,"")}1'`

#espeak "$WORD" &
#echo $WORD : $MEANING >> /home/lg/tmp/words.txt
#echo "$MEANING"|xclip

notify-send -u critical "$WORD" "$MEANING"; 
sleep 2; 
killall /usr/lib/x86_64-linux-gnu/notify-osd

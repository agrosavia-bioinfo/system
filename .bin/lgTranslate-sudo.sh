#!/usr/bin/env bash
LANG=en
WORD="$(xsel -o)"

URL="http://translate.googleapis.com/translate_a/single?client=gtx&sl=$LANG&tl=es&dt=t&q="
URLTEST=$(wget -U "Mozilla/5.0" -qO - "$URL$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')

MEANING=$URLTEST
echo $URLORG

notify-send -u critical -t 0 --icon=info "$WORD" "$MEANING"|xargs -I {} bash -c "sleep 2 && notify-send --close={}" &
echo $WORD : $MEANING >> /home/lg/tmp/words.txt
echo "$MEANING"|xclip

#!/usr/bin/env bash
LANG=en
WORD="$(xsel -o)"
#URL="$(wget -U "Mozilla/5.0" -qO - "http://translate.googleapis.com/translate_a/single?client=gtx&sl=$LANG&tl=es&dt=t&q=$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')"
URL="$(wget -U "Mozilla/5.0" -qO - "http://translate.googleapis.com/translate_a/single?client=gtx&sl=$LANG&tl=es&dt=t&q=$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')"
MEANING=$URL

sudo notify-send -u critical -t 0 --icon=info "$WORD" "$MEANING"
echo $WORD : $MEANING >> /home/lg/tmp/words.txt
espeak "$WORD" -a 200 -g 5
echo $WORD : $MEANING >> /home/lg/tmp/words.txt

#notify-send -u critical -t 2000 --icon=info "$(xsel -o)" "$(wget -U "Mozilla/5.0" -qO - "http://translate.googleapis.com/translate_a/single?client=gtx&sl=$LANG&tl=es&dt=t&q=$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2}')"

TITLE_PATTERN=$1
NEW_TITLE=$2
xdotool search --name $TITLE_PATTERN set_window --name $NEW_TITLE

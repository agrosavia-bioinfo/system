#### Show key events ####################
# xev : show keycodes
# xmodmap: show all modifiers

##### Remap Caps Lock key to Tab Key ##################
#------ Remap keyboard keys examples ------------------                                                      
# xmodmap -e "remove lock = Caps_Lock" 
# xmodmap -e "keycode 66 = Tab" 
# Remap F1 to 1 exclam key
# xmodmap -e "keycode 49 = 1 exclam 1 exclam"
# xmodmap -e "add control  = Super_L" 

# Menu  key to "/" (slash)
xmodmap -e "keycode 135 = slash backslash backslash" &> /dev/null &
# Key win  key to \  # For MC hot key to saved paths
#xmodmap -e "keycode 133 = backslash" &> /dev/null &
xmodmap -e "keycode 21 = backslash" &> /dev/null &
# Dead cute key ' to ' and @
xmodmap -e "keycode 34 = dead_acute at" &> /dev/null &

# Alt Gr key to \
#xmodmap -e "keycode 108 = backslash" &> /dev/null &

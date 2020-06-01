cvt 1440 900
xrandr --newmode "1440"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync
xrandr --addmode VGA1 1440
xrandr --output VGA1 --mode 1440
xrandr --output LVDS1 --mode 1024x600 --output VGA1 --mode 1440 --left-of LVDS1

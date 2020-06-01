# ~/.bashrc: executed by bash(1) for non-login shells.
#echo "...bashrc"
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

#wmctrl-set.py > /dev/null  # Resize and move to the right or left

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
export HISTCONTROL=ignoredups
# ... and ignore same sucessive entries.
export HISTCONTROL=ignoreboth

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
#if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
#    debian_chroot=$(cat /etc/debian_chroot)
#fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

#. ~/cloud/fm/framework/profile-framework
. ~/.profile

#export PATH=/home/lg/labrpi/cago/lg/utils:$PATH;$PHD_PATH
export BROWSER=/opt/bin/firefox

export PATH=$HOME/bin:$PATH

#so as not to be disturbed by Ctrl-S ctrl-Q in terminals:
stty -ixon

# Some aliases...
# Clipboard
alias clipboard='xclip -sel clip'
alias ek="setxkbmap us_intl"
# Libreoffice
calc="libreoffice --calc"

# To edit PDF metadata
editPDFmetadata() {
OUTPUT="${1}-new.pdf"
METADATA="tmp${1}-report.txt"
pdftk ${1} dump_data output $METADATA
$EDITOR $METADATA
pdftk ${1} update_info $METADATA  output $OUTPUT
touch -r ${1} ${OUTPUT}
}

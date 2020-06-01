#echo "loading .profile..."
#----------------------------------------------------------
## Added by Luis Garreta
#----------------------------------------------------------
export LC_ALL=en_US.UTF-8
#export TERM="xterm-256color"

############## PROMPT COLORING ####################################
#export PS1="$COLOR[\W$COLOR\h$COLOR:\W$COLOR]\$ \e[-1m "
COLOR="\[\033[0;34m\]"
COLOR1="\[\033[1;35m\]"
	export PS1="$COLOR<\h>[\W]$COLOR1\$ \e[m"
############## Alias definitions ##################################
eval "`dircolors -b`"
alias ls='ls --color=auto'
alias ll='ls -lgGh --time-style=iso'
alias la='ls -A'
alias l='ll'
alias lt='ll -tr'
alias ltr='ll -tr'
alias lf='ls -l -f'
alias rm='rm -i'
alias dfs='df -h|grep sd'

#alias grep='grep -n'
#alias lvim='vim -c "normal '\''0"'
#alias lvim1='vim -c "normal '\''1"'
#alias lvim2='vim -c "normal '\''2"'

alias dup="du -h;p"
alias timeu='/usr/bin/time -f "%e"'

alias lsu='ls -U'
#alias lsc='ls -U|wc -l'

alias ocalc="libreoffice --calc"
######################################################
# SYSTEM path
######################################################
export PATH=
SYS_PATH=/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin

#-----------------------------------------------------
# LG BIN PATH
#-----------------------------------------------------
BIN_PATH=.:$HOME/.bin:/opt/bin
export PATH=$BIN_PATH:$SYS_PATH:$PHD_PATH

#-----------------------------------------------------
# JAVA PATH 
#-----------------------------------------------------
#export JAVA_HOME=/opt/apps/jdk
#export CLASSPATH=.:$CLASSPATH
#export PATH=$PATH:$JAVA_HOME/bin

# Environment setting for trajectories from Geofold's DAGs
TRAJ_GF_DAG=/home/lg/phd/labrpi/xcago/lggo/src

#------ MC ---------
export EDITOR=vim
#export PAGER=
#export CDPATH=$HOME/cloud/courses


#echo "... LG profile loaded"

######## Thesis Phd ###############3
#. ~/.profile-latex
#export TEX_PATH=/home/lg/cloud/phd/Dropbox/phd/thesis/tex
#export TEXMFHOME=/home/lg/cloud/phd/Dropbox/phd/thesis/tex/texmf
#PATH=$PATH;:$TEX_PATH/adds:$TEX_PATH:

#. /home/fm/Dropbox/framework/profile-framework

#--------------------------------------------------------
# Dropbox cli configuration
#--------------------------------------------------------
DROPBOX_BIN=/home/lg/.bin/dropbox_cli/bin
export PATH=$PATH:$DROPBOX_BIN
export DROPBOX_HOME=/data/lg/papers
#export DROPBOX_HOME=/home/lg/cloud/phd


#-----------------------------------------------------
# Metagenomics
#-----------------------------------------------------
proxy=""
DNS=`cat /etc/resolv.conf|grep search|cut -d ' ' -f2`
if [ "$DNS" = "unicauca.edu.co" ]; then
	echo "...unicauca"
	proxy="http://proxy.unicauca.edu.co:3128"
fi

if [ "$DNS" = "bibliotecapdvc.com" ]; then
	echo "... proxy biblioteca departamental"
	proxy="http://192.168.100.1:8080"
fi

export http_proxy=$proxy

#export http_proxy="http://proxy.unicauca.edu.co:3128"

#---- Load gebixw's profile --------------------------------#
export GW_PATH=$HOME/cloud/gebixw/Dropbox/dev
#. $GW_PATH/profile-gebixw.sh

#---- Load gebixw's profile --------------------------------#
	export EVALPATHS_PATH=$HOME/cl/people/MMartinez/tesis
#. $EVALPATHS_PATH/profile-evalpaths.sh

export PATH=$PATH:/opt/apps/meme/bin
#-----------------------------------------------------------#

#-----------------------------------------------------
# Config
#-----------------------------------------------------
if [ "$TODO" = "yes" ]; then 
	todo 
fi
#todo list
setxkbmap latam

#alias clipboard='xclip -sel clip'
#key-win-hotdir

### For protein analysis MMTSB toolset
toolset=/DATA/cloud/pathways/eval/tools/programs/mmtsb_toolset
export PATH=$PATH:$toolset

export HOME_PPATH=/home/ppath


#----------------------------------------------------------
# Agrosavia
#----------------------------------------------------------
AGROPATH=/home/lg/agrosavia
#------------------- multiGWAS.R tool profile ---------------------
source /home/lg/agrosavia/GWAS/multiGWAS-dev/multiGWAS-profile.sh

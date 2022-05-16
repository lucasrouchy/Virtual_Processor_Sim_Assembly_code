# Setting PATH for Python 3.8
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
export PATH

#terminal with color
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# basic alias
alias ls='ls -GFhr'
alias ll='ls -l'
alias la='ll -a'
alias h='history'
alias eh='echo $HOME'
alias cs='cscope'

# git alias
alias g='git'
alias ga='git add'
alias gs='git status'
alias gd='git diff'
alias gl='git log'
alias gp='git pull'
alias gc='git checkout'

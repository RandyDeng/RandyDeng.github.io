---
layout: post
title: "Creating Useful Aliases"
categories: programming bash
---

# Why do we create aliases?
So I recently decided to revisit the aliases I had a set up in the past on my Ubuntu machine. It was simply something I threw together a while back and I didn't really care how long they lasted or if the commands were a bit wonky. Now that I finally got around to improving them, it's time to share what I did!

Aliases are great for when you have to repeatedly use a set of commands.
Instead of typing out long commands over and over, it's much easier to create an alias that is a few characters long and easier to type.
I highly recommend it since it has saved me a lot of time and effort in trying to type and remember a lot of commands.
Convinced? Cool, let's create some.

# How do you create an alias?
To create an alias we will modify two files: `.bashrc` and `.bash_alises`.
We will add a short command to `.bashrc` that will load in our `.bash_aliases` file and our `.bash_alises` file will contain all of our aliases.
While you could directly add the aliases directly to `.bashrc`, it's more organized to just keep them all in a separate file.

Create both files in your root directory by running the following:

``` bash
cd ~
# touch is used to create new files
touch .bashrc
touch .bash_aliases
```

If you're unsure whether these files exist, run `ls -a` to view all files including hidden ones.

In your `.bashrc` file, add the following text:

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Lastly, add your aliases into `.bash_aliases`. Aliases have the following syntax:
``` bash
# alias your_alias='actual_command' e.g.
alias s='sudo'
```

To remove aliases, modify `.bash_aliases` and start up a new terminal to reload the changes.

# 10 Useful Aliases for Development
Now that you know how to create aliases, here are some that I've been using and enjoy.

## General Commands
```
alias h='cat ~/.bash_aliases'
alias dev='cd ~/Documents/Github'
alias c='clear'
alias s='sudo'
alias update='sudo apt-get update'
alias upgrade='sudo apt-get upgrade'
alias get='sudo apt-get install'
```

## Git
```
alias gs='git status'
alias ga='git add'
alias gcm='git commit -m'
alias gl='git log'
alias gb='git branch'
alias gbd='git branch -d'
alias gco='git checkout'
alias gcob='git checkout -b'
alias gp='git push'
alias gpf='git push -f'
alias gd='git diff'
alias gdm='git diff master'
alias grim='git rebase -i master'
```

## Docker
```
alias dps='docker ps'
alias di='docker images'
alias dsp='docker system prune'
alias dcb='docker-compose build'
alias dcu='docker-compose up'
```

## Conda
```
alias cle='conda list env'
alias ci='conda install'
alias ca='conda activate'
alias ccn='conda create -n'
alias crn='conda remove -n'
alias cua='conda update -n base conda'
```

## Pip & Pipenv
```
alias pi='pip install'
alias pei='pipenv install'
```

At the end of the day, aliases are best when you can use them easily and quickly. It is much better to have a few aliases that you use frequently than fumbling around with dozens you don't understand. Customize your aliases to your liking and enjoy!
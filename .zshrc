#source ~/data/linuxapps/zsnaps/zsh-snap/znap.zsh

if [[ -r "$HOME/dotfiles/.config/zsh/vars.zsh" ]];
then
  source "$HOME/dotfiles/.config/zsh/vars.zsh"
else 
  source "$HOME/dotfiles/.config/zsh/vars.example.zsh"
fi
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Dependancies You Need for this Config
# zsh-syntax-highlighting - syntax highlighting for ZSH in standard repos
# autojump - jump to directories with j or jc for child or jo to open in file manager
# zsh-autosuggestions - Suggestions based on your history

# History in cache directory:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zshhistory
setopt appendhistory

# Basic auto/tab complete:
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)               # Include hidden files.

#up arrow and down arrow
autoload -Uz up-line-or-beginning-search down-line-or-beginning-search

zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

bindkey '^[[A'  up-line-or-beginning-search    # Arrow up
bindkey '^[OA'  up-line-or-beginning-search
bindkey '^[[B'  down-line-or-beginning-search  # Arrow down
bindkey '^[OB'  down-line-or-beginning-search

# Custom ZSH Binds
bindkey '^ ' autosuggest-accept
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
# Android platform-tools
[ -d "$HOME/lapps/android-cli" ] && export PATH=${PATH}:$HOME/lapps/android-cli || echo 'no android-cli'

# NVM installation
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# set default pager to most
export PAGER="less"

# Load aliases and shortcuts if existent.
[ -f "$ZSH_DIR/aliasrc" ] && source "$ZSH_DIR/aliasrc"
[ -f "$ZSH_DIR/systemctl-alias" ] && source "$ZSH_DIR/systemctl-alias"
[ -f "$GITALIAS_DIR/alias-git.zsh" ] && source "$GITALIAS_DIR/alias-git.zsh"

# Load ; should be last.
source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh 
source /usr/share/autojump/autojump.zsh
source /usr/share/doc/fzf/examples/key-bindings.zsh
#source <(fzf --zsh)
source /usr/share/doc/fzf/examples/completion.zsh
[ -f "$SYNTAXHL/zsh-syntax-highlighting.zsh" ] && source "$SYNTAXHL/zsh-syntax-highlighting.zsh"
[ -f "$PWRL10_DIR/powerlevel10k.zsh-theme" ] && source "$PWRL10_DIR/powerlevel10k.zsh-theme"
#znap source marlonrichert/zsh-autocomplete

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

#autoload -Uz compinit
fpath+=~/.zfunc
# add our dotfiles completion folder
fpath+=~/dotfiles/zsh/completions
autoload -Uz compinit

if [ -e /home/daniel/.nix-profile/etc/profile.d/nix.sh ]; then . /home/daniel/.nix-profile/etc/profile.d/nix.sh; fi # added by Nix installer


eval "$(zoxide init zsh)"
eval "$(atuin init zsh)"
#eval "$(atuin init zsh --disable-up-arrow)"

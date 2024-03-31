. "$HOME/.cargo/env"
eval "$(/home/daniel/.rakubrew/bin/rakubrew init Zsh)"
export XDG_DATA_DIRS=/home/daniel/.local/share:/snap/bin:/usr/share/applications:/usr/share:/var/lib/flatpak/exports/share:/usr/local
export PATH=$PATH:/usr/local/go/bin # add go to path
export PATH=$PATH:/home/daniel/.local/share/applications #add local apps
export PATH=$PATH:/usr/lib/python3/dist-packages # add python packages to path
export GOPATH=/home/daniel/goi
export XDG_CACHE_HOME=/home/daniel/.cache
# add snaps bin to path
export PATH="$PATH:/snap/bin"
# add user bin to path
export PATH="$PATH:/home/daniel/.local/bin"
# add composer to path
export PATH="$PATH:$HOME/.config/composer/vendor/bin"
export LESS=-R

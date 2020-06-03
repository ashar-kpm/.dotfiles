#!/bin/bash

just-colors --theme $1 --no-apply
cat $HOME/.dotfiles/.config/i3/config.base $HOME/.config/just-colors/cache/colors.local > $HOME/.dotfiles/.config/i3/config

ln -sfn ~/.config/just-colors/cache/colors.conf ~/.config/kitty/colors.conf	
ln -sfn ~/.config/just-colors/cache/colors.Xresources ~/colors.Xresources
mkdir -pv ~/.config/qutebrowser
ln -sfn ~/.config/just-colors/cache/config.py ~/.config/qutebrowser/config.py
mkdir -pv ~/.config/alacritty
ln -sfn ~/.config/just-colors/cache/alacritty.yml ~/.config/alacritty/alacritty.yml
mkdir -pv ~/.config/zathura
ln -sfn ~/.config/just-colors/cache/zathurarc ~/.config/zathura/zathurarc
ln -sfn ~/.dotfiles/.config/i3/config ~/.config/i3/config

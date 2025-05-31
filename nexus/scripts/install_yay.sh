#!/bin/bash  

  if ! command -v yay &> /dev/null; then
    echo "🛠 Installing yay AUR helper..."
    pkexec pacman -S --needed git base-devel --noconfirm
    rm -rf yay
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd ..
    rm -rf yay
  else
    echo "yay is already installed."
  fi

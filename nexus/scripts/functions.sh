#!/bin/bash

install_packages() {
  local pkgs=("$@")
  for pkg in "${pkgs[@]}"; do
    if ! yay -S --noconfirm --needed "$pkg"; then
    fi
  done
}

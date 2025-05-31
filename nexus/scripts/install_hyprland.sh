#!/bin/bash 

source ./packages.sh
source ./functions.sh

install_packages "${hypr_packages[@]}"
enable_user_service "waybar.service"

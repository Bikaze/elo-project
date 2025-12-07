#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting bootstrap process..."

# 1. Update the server
echo "Updating the system..."
sudo apt-get update -y

# 2. Install Docker using the convenience script from get.docker.com
echo "Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
rm get-docker.sh

# 3. Make ubuntu a sudoer (usually default on Ubuntu cloud images, but ensuring it)
echo "Ensuring 'ubuntu' user is in the sudo group..."
sudo usermod -aG sudo ubuntu
newgrp docker

echo "Bootstrap complete!"
echo "Please log out and log back in (or close and reopen your SSH session) for the group changes to take effect."

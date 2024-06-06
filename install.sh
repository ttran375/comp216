#!/bin/bash

# Update package list
sudo apt-get update

# Install Wireshark
sudo apt-get install -y wireshark

# Allow non-root users to capture packets
sudo dpkg-reconfigure wireshark-common

# Add current user to the Wireshark group
sudo usermod -aG wireshark $USER

# Verify installation
wireshark --version

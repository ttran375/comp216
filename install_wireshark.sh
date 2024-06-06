sudo apt-get update
sudo apt-get install -y wireshark
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark $USER
wireshark --version
sudo apt-get install -y tshark
sudo tshark -i eth0

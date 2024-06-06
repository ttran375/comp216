# Wireshark

1. **Update the Package List**: Open the terminal in your Codespace and run the following command to update the package list:

   ```sh
   sudo apt-get update
   ```

2. **Install Wireshark**: Run the following command to install Wireshark:

   ```sh
   sudo apt-get install wireshark
   ```

3. **Allow Non-root Users to Capture Packets**: During the installation, you will be prompted to allow non-root users to capture packets. Select "Yes".

4. **Verify the Installation**: Once the installation is complete, you can verify it by running:

   ```sh
   wireshark --version
   ```

Here is a more comprehensive script to automate the process:

```sh
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
```

You can create a file named `install-wireshark.sh`, copy the above script into it, and run it in your Codespace terminal:

```sh
chmod +x install-wireshark.sh
./install-wireshark.sh
```

This script will handle the installation and necessary configurations for Wireshark in your GitHub Codespace environment.

5. **Install `tshark`**:

   ```sh
   sudo apt-get install -y tshark
   ```

6. **Run `tshark`**: You can start capturing packets with `tshark` using a command like this:

   ```sh
   sudo tshark -i <interface>
   ```

   Replace `<interface>` with the appropriate network interface you want to capture packets on (e.g., `eth0`, `wlan0`, etc.).

7. **Example Commands**:
   - List available network interfaces:

     ```sh
     tshark -D
     ```

   - Capture packets on a specific interface:

     ```sh
     sudo tshark -i eth0
     ```

   - Save captured packets to a file:

     ```sh
     sudo tshark -i eth0 -w capture.pcap
     ```

   - Read packets from a file:

     ```sh
     tshark -r capture.pcap
     ```

Using `tshark`, you can still capture and analyze network traffic in a text-based environment, which is suitable for GitHub Codespaces.

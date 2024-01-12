#!/usr/bin/env python3

import subprocess

def enable_bluetooth():
    # Enables Bluetooth service
    subprocess.run(["sudo", "systemctl", "start", "bluetooth"])
    print("Bluetooth service started")

def main():
    enable_bluetooth()
    print("Bluetooth enabled successfully! Enjoy !! Github : pinkythegawd")

if __name__ == "__main__":
    main()

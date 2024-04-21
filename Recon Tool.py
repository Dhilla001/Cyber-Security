# This simple Recon tool uses nmap, so it can be used in linux OS

import os

def nmap(ip):
    print("nmap scan: \n")
    scan = f"nmap -A -p- -Pn {ip} -v"
    os.system(scan)
    print("\nDirbuster scan: \n")
    os.system(f"dirb {ip}")

nmap(input("enter ip: "))

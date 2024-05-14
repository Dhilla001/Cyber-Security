#This is a Packet Sniffer similar to Wireshark
#This program is compatible in linux OS with root permission

from scapy.all import *
from scapy.layers.l2 import Ether

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

interface = "eth0"  #Enter the interface to capture
sniffer.bind((interface, 0))

try:
    while True:
        rawdata, addr = sniffer.recvfrom(65535)  #recieve from ports
        packet = Ether(rawdata)
        print(packet.summary())
except KeyboardInterrupt:
    sniffer.close()

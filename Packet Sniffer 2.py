#This a simple Packet Sniffer for 'Windows' OS

from scapy.all import *
from scapy.layers.dot11 import Dot11
from scapy.layers.l2 import Ether

def packet_handler(packet):
    if Ether in packet or Dot11 in packet:
        print(packet.summary())


# Start sniffing packets
interface = "Wi-Fi"
sniff(iface=interface, prn=packet_handler, store=0)

from scapy.all import *

if __name__ == '__main__':
    source_IP = input("Enter IP Addr of Source : ")
    target_IP = input("Enter IP Addr of Destination : ")
    source_port = int(input("Enter IP Addr of Sourec : "))
    for i in range(0, 65536):
        sIP = scapy.all.IP(source = source_IP, destination = target_IP)
        #sTCP = TCP
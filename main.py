from scapy.all import Ether,ARP,srp

#Input to ask for the ip range (exp: 192.168.1.0/24)
ip_range = input("Enter ip range: ")

#Make the ethernet header and the arp option, set FF:FF:FF:FF:FF:FF as a destination mac for broadcast.
ether_header = Ether(dst="FF:FF:FF:FF:FF:FF")
arp_options = ARP(pdst=ip_range)

#Crafting the full packet
full_packet = ether_header / arp_options

#Sending the full packet
Response, noresponse = srp(full_packet,timeout=3)

print("----------------------------------")
print(f"Live hosts in : {ip_range}")
print()

#Printing only the IP and MAC address of the hosts that responded 
for send, receive in Response:
    print(f"IP: " + receive[Ether].psrc + "   " "MAC: " + receive[Ether].hwsrc)



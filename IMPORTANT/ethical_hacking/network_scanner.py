import scapy.all as scapy


def grab_info(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    clients = []
    for el in answered_list:
        client_dict = {"ip": el[1].psrc, "mac": el[1].hwsrc}
        clients.append(client_dict)

    return clients


def print_info(client_list):
    print("IP\t\t\t\tMAC address\t\t\t\t\n---------------------------------")
    for client in client_list:
        print(f"{client['ip']}\t\t{client['mac']}")


if __name__ == '__main__':
    print_info(grab_info("10.60.0.1/24"))

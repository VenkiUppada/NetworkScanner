
from ssl import Options
from tabnanny import verbose
from time import time
import scapy.all as scapy
import optparse as opp

def get_args():
    parser = opp.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="ip address range you want to scan.\t\Ex: 192.168.0/24"
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-]Please specify IP Address to scan\t\tuse --help for more info")
    else:
        return options



def scan(ip):
    arp_rqst = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_rqst_b = broadcast/arp_rqst     # ARP request broadcast
    answered_list = scapy.srp(arp_rqst_b, timeout = 10 , verbose=False)[0]


    target_list = []
    for i in answered_list:             #Displays each element in answered_list
        target_dict = {"IP": i[1].psrc, "MAC": i[1].hwsrc}
        target_list.append(target_dict)
 
    return target_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for target in result_list:
        print(target["IP"] + "\t\t" + target["MAC"])



options = get_args()
        
scan_result = scan(options.ip)
print_result(scan_result)

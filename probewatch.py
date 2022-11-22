from scapy.all import *
from threading import Thread
from mac_vendor_lookup import MacLookup, BaseMacLookup
import argparse
import pandas
import time
import os

BaseMacLookup.cache_path = "probe_cache"
networks = pandas.DataFrame(columns=["MAC", "Vendor", "SSID", "BSSID"])
networks.set_index("MAC", inplace=True)


def callback(packet):
    if packet.haslayer(Dot11ProbeReq) and packet.subtype == 4 and len(packet.info.decode()) > 0:
        mac = packet.addr2.upper()
        ssid = packet.info.decode()
        bssid = packet.addr3.upper()
        try:
            vendor = MacLookup().lookup(mac)
        except:
            vendor = '[N/A]'
        networks.loc[mac] = (vendor,ssid,bssid)


def print_all():
    while True:
        os.system("clear")
        print(networks)
        time.sleep(1)
        
        
def check_for_updates():
    print("Please wait while database is updated")
    MacLookup().update_vendors()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', action="store_true", help="Update MAC address database")
    parser.add_argument('-i','--interface', default="wlan0", help="Interface to use. Must be in monitor mode") 
    args = parser.parse_args()
    if args.update:
        check_for_updates()
    

    log = Thread(target=print_all)
    log.daemon = True
    log.start()

    sniff(prn=callback, iface=args.interface)

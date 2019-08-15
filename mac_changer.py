#!/usr/bin/python3

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter the network interface whose mac address needs to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter New Mac")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac address, use --help for more info")

    return options


def change_mac(interface, new_mac):
    print("[+] Mac address for {} has been changed to {}".format(interface, new_mac))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call("ifconfig", interface, "hw", "ether", new_mac)
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
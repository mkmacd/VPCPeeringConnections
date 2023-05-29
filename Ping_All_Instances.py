#!/bin/env python3
import os
import socket
import sys


def pingallinstances():
    hostname = socket.gethostname()
    host_ipaddress = str(socket.gethostbyname(hostname))
    # Dictionary of hard coded ip addresses based on IP addresses from cloudformation template
    ipaddresses = {"10.1.2.249":"Production Server (VPC1)", "10.2.1.29":"Dev Server (VPC2)", "10.3.1.129":"Test Server(VPC3)", "10.4.1.22":"Shared Server(VPC4)"}
    passfaildict = {}
    success = True
    print()
    print()
    print("-----------------------------------------------------")
    print(f"Starting to ping all ip addresses from: {host_ipaddress} ({ipaddresses[host_ipaddress]})")
    print("------------------------------------------------------")
    print()
    print()
    sys.stdout.flush()
    #iterates through dictionary of IP addresses and attempts to ping each one from current machine
    for ipaddress in ipaddresses:
        print(f"Pinging: {ipaddresses[ipaddress]}")
        sys.stdout.flush()
        individual_result = os.system(f"ping -c 2 -W 1 {ipaddress}")
        print()
        print("---------------------")
        print()
        sys.stdout.flush()
        if individual_result == 0:
            passfaildict[ipaddress] = "Success"
        else:
            passfaildict[ipaddress] = "Fail"
            success = False
    for i in [4]:
        print()
    print("//////////////////////////////////////////////////////////////")
    if success:
        print(f"{ipaddresses[host_ipaddress]} has succeeded in pinging all other machines.")
    else:
        print(f"Unfortunately the {ipaddresses[host_ipaddress]} ({host_ipaddress}) has failed to ping all other machines.")
    for ipaddress in passfaildict:
        print(f"{ipaddresses[ipaddress]} ({ipaddress}): {passfaildict[ipaddress]}")
    # print(passfaildict)
    print("//////////////////////////////////////////////////////////////")
    for i in [4]:
        print()
    if not success:
        return 1

    return 0


exit(pingallinstances())



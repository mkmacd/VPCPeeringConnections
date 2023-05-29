#!/bin/env python3
import os

def run_ping_on_all_instances():
    # hardcoded dictionary of ip addresses based on cloudformation template
    ipaddresses = {"10.1.2.249":"Production Server (VPC1)", "10.2.1.29":"Dev Server (VPC2)", "10.3.1.129":"Test Server(VPC3)", "10.4.1.22":"Shared Server(VPC4)"}
    results_dict = {}
    #iterates through each ip addresses and tries to copy python script to the instance then runs the script.
    for ipaddress in ipaddresses:
        scp_result = os.system(f"scp -o StrictHostKeyChecking=no -o ConnectTimeout=5 ~/pythonfiles/Ping_All_Instances.py {ipaddress}:/tmp/ ")
        if scp_result != 0:
            results_dict[ipaddress] = "Fail"
            continue
        ssh_result = os.system(f"ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 {ipaddress} python3 /tmp/Ping_All_Instances.py")

        if ssh_result != 0:
            results_dict[ipaddress] = "Fail"
        else:
            results_dict[ipaddress] = "Success"

    print("----------------------------------------------")
    print("These are the overall results for each machine:")
    for ipaddress in results_dict:
        print(f"{ipaddresses[ipaddress]} ({ipaddress}): {results_dict[ipaddress]}")
    print("----------------------------------------------")

run_ping_on_all_instances()




#!/usr/bin/python3

import os

print("whoami: ")
whoami_output = os.system("whoami")
print("ip a: ")
ip_a_output = os.system("ip a")
print("lshw -short: ")
lshw_output = os.system("lshw -short")
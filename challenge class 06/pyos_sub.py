#!/usr/bin/python3

import subprocess

print("whoami: ")
whoami_output = subprocess.run("whoami")
print("ip a: ")
ip_a_output = subprocess.run(["ip", "a"])
print("lshw -short: ")
lshw_output = subprocess.run(["lshw", "-short"])
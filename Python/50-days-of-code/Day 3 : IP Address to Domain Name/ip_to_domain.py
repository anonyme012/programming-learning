# Import
import socket

# Input
ip = input("Enter an IP address : ")

# Execution
domain_name = socket.getfqdn(ip)
print("Domain name of", ip, "is :", domain_name)
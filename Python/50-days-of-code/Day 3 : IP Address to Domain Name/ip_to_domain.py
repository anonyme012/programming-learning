# Import
import socket

# Input
ip = input("Enter an IP address : ")

# Execution
domain_name = socket.getfqdn(ip)
print("Domain name of", ip, "is :", domain_name)

# My errors during programming : 
# - I initially used gethostbyaddr() instead of getfqdn() to get the domain name whithout parsing needed.

# Possibles improvements :
# - Nothing I think.
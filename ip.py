import socket
from urllib.parse import urlparse

website = input("Enter Website URL: ")
hostname = urlparse(website if "://" in website else "https://" + website).hostname

try:
    ip = socket.gethostbyname(hostname)
    print(f"Website: {hostname}")
    print(f"IP Address: {ip}")

except socket.gaierror:
    print("Error: Unable to resolve the domain name.")
    print("Check your internet connection or website URL.")

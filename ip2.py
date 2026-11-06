
import socket
from urllib.parse import urlparse

website = input("Enter Website URL: ")

hostname = urlparse(
    website if "://" in website else "https://" + website
).hostname

try:
    results = socket.getaddrinfo(hostname, None)

    print("\nWebsite:", hostname)
    print("\nResolved IP Addresses:")

    ips = set()

    for result in results:
        ip = result[4][0]
        ips.add(ip)

    for ip in sorted(ips):
        print(ip)

except socket.gaierror as e:
    print("DNS Resolution Failed:", e)

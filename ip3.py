
import socket
from urllib.parse import urlparse
import http.client

SERVICES = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3000: "Development Web Server",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Alternative"
}

website = input("Enter Website URL: ").strip()

hostname = urlparse(
    website if "://" in website else "https://" + website
).hostname

if not hostname:
    print("Invalid website URL.")
    raise SystemExit

try:
    ip = socket.gethostbyname(hostname)

    print("\n========== WEBSITE INFORMATION ==========")
    print("Website:", hostname)
    print("IP Address:", ip)

    print("\n========== PORT INFORMATION ==========")

    for port, service in SERVICES.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        try:
            result = sock.connect_ex((hostname, port))

            if result == 0:
                print(f"Port: {port}")
                print(f"Service: {service} (common association)")
                print("Status: OPEN")
                print("----------------------------------")
        finally:
            sock.close()

    print("\n========== WEB SERVER INFORMATION ==========")

    for scheme, port in [("https", 443), ("http", 80)]:
        try:
            if scheme == "https":
                conn = http.client.HTTPSConnection(
                    hostname, port, timeout=5
                )
            else:
                conn = http.client.HTTPConnection(
                    hostname, port, timeout=5
                )

            try:
                conn.request("HEAD", "/")
                response = conn.getresponse()

                print("Protocol:", scheme.upper())
                print("HTTP Status:", response.status)
                print("Server:", response.getheader("Server", "Not disclosed"))
                break
            finally:
                conn.close()

        except (OSError, http.client.HTTPException):
            continue
    else:
        print("Could not retrieve web server information.")

except socket.gaierror as e:
    print("DNS Resolution Failed:", e)

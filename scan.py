import socket
import requests

def scan_ports(ip_address, start_port, end_port):
    print(f"\n[Port Scanner] Scanning {ip_address} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"--> Port {port} is open")
            sock.close()
        except socket.error as e:
            print(f"Error checking port {port}: {e}")


def brute_force(login_url, usernames, passwords):
    print(f"\n[Brute Force] Attempting login on {login_url}")
    for user in usernames:
        for pwd in passwords:
            payload = {'username': user, 'password': pwd}
            try:
                response = requests.post(login_url, data=payload, timeout=5)
                if "Login Failed" not in response.text:
                    print(f"--> Credentials found: {user}:{pwd}")
                    return
            except requests.exceptions.RequestException:
                print("Could not connect to the server.")
                return
    print("No valid credentials found.")

def directory_enumerator(base_url, paths):
    print(f"\n[Directory Enumerator] Checking common paths on {base_url}")
    for path in paths:
        full_url = f"{base_url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"--> Found: {full_url}")
        except requests.exceptions.RequestException:
            pass  

print("""

  PENETRATION TESTING TOOLKIT

1. Port Scanner
2. Brute Force Login
3. Directory Enumerator
""")

choice = input("Select a test(1-3): ")

if choice == '1':
    ip = input("Enter target IP: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_ports(ip, start, end)

elif choice == '2':
    url = input("Enter login URL: ")
    users = ['admin', 'user', 'test']
    passwords = ['admin', '1234', 'test123', 'password']
    brute_force(url, users, passwords)

elif choice == '3':
    base_url = input("Enter the website URL: ")
    common_dirs = ['admin', 'login', 'dashboard', 'config', 'uploads']
    directory_enumerator(base_url, common_dirs)

else:
    print("Invalid selection. Please choose between 1 and 3.")



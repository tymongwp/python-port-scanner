import socket

def port_scanner(ip, ports):
    print(f"Scanning {ip}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                print(f"Port {port} is open.")

# Example 
if __name__ == "__main__":
    target_ip = "127.0.0.1"  
    target_ports = range(20, 300)  
    port_scanner(target_ip, target_ports)

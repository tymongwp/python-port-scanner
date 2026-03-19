import socket
import threading

print_lock = threading.Lock()


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            with print_lock:
                print(f"[OPEN] Port {port}")

        sock.close()

    except:
        pass


def scan_ports(target, start_port, end_port):
    print(f"\n[+] Scanning {target} from port {start_port} to {end_port}\n")

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Scan complete.")


if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    scan_ports(target, start, end)
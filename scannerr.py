import socket

target = "127.0.0.1"

ports = [443,80,8080,21,22]

for port in ports:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((target,port))
    if result==0:
        print(f"Port {port} is Open")
    else:
        print(f"Port {port} is Closed")
    
    sock.close()

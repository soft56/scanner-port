import socket

def scan_ports(host, start_port=1, end_port=1024):
    print(f"Scan en cours sur {host} de {start_port} à {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"✅ Port {port} ouvert")
            s.close()
        except:
            pass

if __name__ == "__main__":
    target = input("Entrez l'adresse IP ou le nom de domaine à scanner : ")
    scan_ports(target)

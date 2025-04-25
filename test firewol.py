import socket

# Список дозволених IP-адрес
allowed_ips = ["127.0.0.1", "192.168.1.100"]

def handle_connection(conn, addr):
    ip = addr[0]
    if ip in allowed_ips:
        print(f"[ALLOW] Connection from {ip}")
        conn.send(b"Access granted.\n")
    else:
        print(f"[BLOCK] Connection from {ip}")
        conn.send(b"Access denied.\n")
    conn.close()

def run_firewall(port=9999):
    server = socket.socket()
    server.bind(("", port))  # Прив'язка до порту / всі інтерфейси
    server.listen()
    print(f"Firewall is active on port {port}")

    while True:
        conn, addr = server.accept()
        handle_connection(conn, addr)

if __name__ == "__main__":
    run_firewall()
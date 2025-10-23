import socket

# Klient soketini yaratish
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))  # Serverga ulanish

# Serverga ma'lumot yuborish
client_socket.sendall(b"Salom, server!")

# Serverdan javob olish
response = client_socket.recv(1024)
print(f"Server javobi: {response.decode('utf-8')}")

client_socket.close()  # Soketni yopish

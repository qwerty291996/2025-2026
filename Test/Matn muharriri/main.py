import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen(5)

print("Server ulanishlarni kutmoqda...")
conn, addr = server_socket.accept()  # Yangi ulanishni kutib olish

print(f"Yangi mijoz ulanishi: {addr}")

import socket

# Server soketini yaratish
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))  # Serverni localhost va 5000-portga bog'lash
server_socket.listen(5)

print("Server ulanishlarni kutmoqda...")

# Yangi ulanishni qabul qilish
conn, addr = server_socket.accept()
print(f"Yangi mijoz ulanishi: {addr}")

# Mijozdan ma'lumot olish
data = conn.recv(1024)
print(f"Mijozdan keldi: {data.decode('utf-8')}")

# Serverdan javob yuborish
response = "Xabar qabul qilindi".encode("utf-8")
conn.sendall(response)  # Javob yuborish

conn.close()  # Soketni yopish

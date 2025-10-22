import socket

# 1) Soket yaratish
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) Soketni localhost va port 5000 ga bog'lash
server_socket.bind(("127.0.0.1", 5000))

# 3) Serverni ulanishlarni kutish holatiga o‘tkazish
server_socket.listen(5)
print("Server ulanishlarni kutmoqda...")

# 4) Yangi ulanishni qabul qilish
conn, addr = server_socket.accept()  # Yangi ulanishni kutib olish
print(f"Yangi mijoz ulanishi: {addr}")

# Mijozdan ma'lumot olish va qaytarish
while True:
    data = conn.recv(1024)  # Mijozdan ma'lumot olish
    if not data:
        break  # Ma'lumot bo'lmasa, chiqish
    print(f"Mijozdan keldi: {data.decode('utf-8')}")
    conn.sendall(data)  # Qaytadan yuborish

conn.close()  # Soketni yopish

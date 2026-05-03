import socket
import threading
import json

# Server sozlamalari
HOST = '0.0.0.0'  # Barcha tarmoq interfeyslarini tinglaydi
PORT = 5555       # Ixtiyoriy bo'sh port

# Onlayn foydalanuvchilar: {nickname: socket_object}
clients = {}

def handle_client(client_socket, addr):
    nickname = None
    try:
        # 1. Birinchi xabar - foydalanuvchi ismi bo'lishi kerak
        nickname = client_socket.recv(1024).decode('utf-8')
        clients[nickname] = client_socket
        print(f"[ULANDI] {nickname} ({addr})")
        
        # Hamma onlayn foydalanuvchilarga yangi odam qo'shilganini bildirish (ro'yxatni yangilash uchun)
        broadcast_user_list()

        while True:
            # 2. Xabarlarni qabul qilish
            # Eslatma: Keyinchalik bu yerga JSON header logikasini qo'shamiz
            data = client_socket.recv(1024 * 1024) # 1MB gacha xabar
            if not data:
                break
            
            # Xabarni tahlil qilish (Sodda ko'rinishda "KIMGA:XABAR")
            message = data.decode('utf-8')
            if ":" in message:
                receiver, msg_content = message.split(":", 1)
                if receiver in clients:
                    # Xabarni faqat qabul qiluvchiga yuborish
                    clients[receiver].send(f"{nickname}:{msg_content}".encode('utf-8'))

    except Exception as e:
        print(f"[XATO] {nickname} bilan muammo: {e}")
    finally:
        if nickname in clients:
            del clients[nickname]
            print(f"[UZILDI] {nickname} chiqib ketdi.")
            broadcast_user_list()
        client_socket.close()

def broadcast_user_list():
    """Hamma mijozlarga onlayn foydalanuvchilar ro'yxatini yuboradi"""
    user_list = ",".join(clients.keys())
    # "USERS_LIST:Ali,Vali,Sardor" ko'rinishida yuboramiz
    for client in clients.values():
        try:
            client.send(f"USERS_LIST:{user_list}".encode('utf-8'))
        except:
            pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[START] Server {HOST}:{PORT} portida ishlamoqda...")

    while True:
        client_sock, addr = server.accept()
        # Har bir mijoz uchun alohida oqim (Thread) ochamiz
        thread = threading.Thread(target=handle_client, args=(client_sock, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
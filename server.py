import socket
import threading
import logging
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Load encryption key from .env file
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
cipher = Fernet(ENCRYPTION_KEY)

logging.basicConfig(level=logging.INFO)

def handle_client_connection(client_socket):
    try:
        while True:
            encrypted_data = client_socket.recv(4096)
            if not encrypted_data:
                break

            # Decrypt data received from the client
            data = cipher.decrypt(encrypted_data)
            logging.info(f"Received: {data}")

            # Echo the data back to the client (or handle it as needed)
            response = cipher.encrypt(data)
            client_socket.sendall(response)
    except Exception as e:
        logging.error(f"Exception in client connection handler: {e}")
    finally:
        client_socket.close()

def start_server(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    logging.info(f"VPN Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        logging.info(f"Connection established with client {addr}")

        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server(SERVER_IP, SERVER_PORT)

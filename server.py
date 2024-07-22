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

def handle_client(client_socket, addr):
    logging.info(f"Connection established with {addr}")

    try:
        while True:
            # Receive data from client
            encrypted_data = client_socket.recv(4096)
            if not encrypted_data:
                break

            # Decrypt data
            data = cipher.decrypt(encrypted_data)

            # Log and handle data
            logging.info(f"Received data: {data.decode()}")

            # Example: Echo data back to client (encrypted)
            encrypted_response = cipher.encrypt(data)
            client_socket.sendall(encrypted_response)
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection closed with {addr}")

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    logging.info(f"Server listening on port {port}")

    try:
        while True:
            client_socket, addr = server.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()
    except Exception as e:
        logging.error(f"Server exception: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    from config import SERVER_PORT
    start_server(SERVER_PORT)

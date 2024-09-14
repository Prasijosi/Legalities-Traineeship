# Server script
import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024)
            if message:
                print(f"Received message: {message.decode()}")
                response = f"Server: {message.decode()}"
                client_socket.send(response.encode())
            else:
                break
    except ConnectionResetError:
        print("Client disconnected unexpectedly.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 8080))
        server_socket.listen(5)

        print("Server started. Listening for incoming connections...")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Connected by {address}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
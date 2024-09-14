# Client script
import socket

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8080))

        print("Connected to server. Type 'exit' to exit.")

        while True:
            message = input()
            if message == "exit":
                break
            try:
                client_socket.send(message.encode())
                response = client_socket.recv(1024)
                print(f"Server: {response.decode()}")
            except ConnectionResetError:
                print("Server disconnected unexpectedly.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

main()
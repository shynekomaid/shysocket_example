import socket
import time
import json
import datetime

with open("settings.json", "r") as f:
    settings = json.loads(f.read())["server"]

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((settings["ip"], settings["port"]))
serv.listen(settings["listen"])
while True:
    time.sleep(settings["sleepTime"])
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(settings["recv"])
        if not data:
            break
        resp = json.loads(data.decode())
        print(resp)
        if settings["saveHistory"]:
            with open(settings["history"], "a") as f:
                f.write(f"{datetime.datetime.now()} > {resp}\n")
        conn.send(settings["returnMessage"].encode())
    conn.close()


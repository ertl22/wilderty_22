from telethon.events import StopPropagation
from telethon.sync import TelegramClient, events
import asyncio
import time

api_id = 3427706
api_hash = "9af47dec6ef4d0bc16707c0778dc83f6"
Done_Coins = 0
Group = input("User : @").replace("@", "")
with TelegramClient('Demo', api_id, api_hash) as client:
  client.send_message(Group, "ارقام")
  while True:
     time.sleep(0.1)
     @client.on(events.NewMessage(func=lambda message:True))
     async def handler(event):
       if "الرقم ↢ " in event.text:
        try:
          StartMessage = str(event.text.split('الرقم ↢ ( ')[1])
          Num = str(StartMessage.split(' )')[0])
          await client.send_message(Group, Num)
          print(event.text)
        except:print("Error")
        @client.on(events.NewMessage(func=lambda message:True))
        async def handler(event):
          if "فلوسك" in event.text:
             Done = True
          else:
             time.sleep(0.10)
        await client.send_message(Group, "ارقام")
     client.run_until_disconnected()

#by @FlinGer_Bs
from time import sleep
from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.govno", outgoing=True))
async def _(event):
        for i in range(25):
            a = i + 1
            sleep(0.1)
            await event.edit("Рот " +"в " +"говне " +"💩" * a + "...")


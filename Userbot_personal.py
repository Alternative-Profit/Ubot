from telethon import TelegramClient, events, sync
from telethon import Button
from telethon import functions, types
from datetime import datetime
from pathlib import Path

import os
import asyncio
import telethon
import glob


API_ID = 1641545
API_HASH = "5e2f76a9ef8d04cb1386a9f9d246dd9f"

userbot_personal = TelegramClient("userbot_personal", API_ID, API_HASH)


async def usbot():

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.status"))
    async def statususerbot(event):
        await event.edit("userbot personal online")

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.name"))
    async def nameprofilyou(event):
        x = event.text.split(" ", maxsplit=1)[1]
        result = await userbot_personal(functions.account.UpdateProfileRequest(
            first_name=x,
        ))
        await event.edit(f"name put as **{x}**")

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.stopuserbot"))
    async def _stopuserbot(event):
        await event.edit("in 3 seconds the userbot will go offline")
        await userbot_personal.disconnect()
        await asyncio.sleep(3)

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.reboot"))
    async def reboot(event):
        await event.delete()
        import os
        import sys
        import threading
        os.system("clear")

        os.execl(sys.executable, sys.executable, *sys.argv)
        thereading.Thread(target=_restart, args=(bot, msg)).start()

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r".ping"))
    async def _ping(event):
        if event.fwd_from:
            return
        start = datetime.now()
        await event.edit("**Pong!**")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit("**Pong!**\n`{}`".format(ms))

    @userbot_personal.on(events.NewMessage(outgoing=True))
    async def t_p(event):
        if event.text == ".ironia":
            await event.edit("L'ironia consiste nell'affermare il contrario di ciò che si pensa con lo scopo di ridicolizzare o sottolineare concetti per provocare una risata. L'ironia implica una critica, ma si differenzia nettamente dal sarcasmo, che implica anche disprezzo.")

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.delm"))
    async def _delm(event):
        await event.delete()
        d = await event.get_reply_message()
        await d.delete()
        await event.respond("deleted message")

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.del"))
    async def _delm(event):
        await event.delete()
        d = await event.get_reply_message()
        await d.delete()

    @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.version_telethon"))
    async def versiontelethon(e):
        g = (telethon.__version__)
        await e.edit(f"version telethon -> {g}")


print("Userbot Personal Online!")


with userbot_personal:
    userbot_personal.loop.run_until_complete(usbot())
    userbot_personal.run_until_disconnected()

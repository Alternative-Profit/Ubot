from asyncio import Event
from telethon import functions, types


@userbot_personal.on(events.NewMessage)
async def statusOffline(event):
    result = await client(functions.account.UpdateStatusRequest(
        offline=True
    ))
    await Event.respond("I'm offline")

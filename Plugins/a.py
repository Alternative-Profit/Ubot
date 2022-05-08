from telethon import events


@userbot_personal.on(events.NewMessage(pattern=r"\.a"))
async def a(event):
    await event.edit("ª")

# command a

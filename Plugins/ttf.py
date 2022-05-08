from telethon import events




""" 
✘ Comandi disponibili - 
• {i}ttf TTF ti consente di creare qualsiasi file 
Esempio: py html php ecc..
"""


@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.ttf ?(.*)"))
async def get(event):
    name = event.text[4:]
    m = await event.get_reply_message()
    with open(name, "w") as f:
        f.write(m.message)
    await event.delete()
    await userbot_personal.send_file(event.chat_id, name, force_document=True)

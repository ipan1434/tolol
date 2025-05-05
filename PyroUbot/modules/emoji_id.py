from pyrogram import Client, filters

app = Client("emojiprem")  # atau sesuai session kamu

@app.on_message(filters.me & filters.text)
async def get_emoji_id(client, message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "custom_emoji":
                emoji_id = entity.custom_emoji_id
                await message.reply(f"Emoji ID: <code>{emoji_id}</code>", quote=True)

app.run()

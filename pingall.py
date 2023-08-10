from pyrogram import Client, filters

# Api ID и Api Hash находятся на https://my.telegram.org/apps. Делал Blaing
api_id = 'ваш апи ид'
api_hash = 'ваш апи хеш'

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@ app.on_message(filters.command("nuke", prefixes="."))
def ping_all(client, message):
    message.delete()

    members = client.get_chat_members(message.chat.id)

    for member in members:
        if member.user.is_bot:
            continue
        client.send_message(message.chat.id, f"@{member.user.username} ПИНГ ВСЕХ ОТ BLAING")

app.run()

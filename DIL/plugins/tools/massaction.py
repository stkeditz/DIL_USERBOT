from ... import *
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
import asyncio

@app.on_message(cdx("banall"))
@sudo_users_only
async def banall(client, message):
    chat_id = message.chat.id
    chat_name = message.chat.title
    
    if len(message.command) > 1:
        try:
            chat = await client.get_chat(message.command[1])
            chat_id = chat.id
            chat_name = chat.title
        except Exception as e:
            return await eor(message, f"**❌ Error:**\n`{e}`")

    m = await eor(message, f"**➻ ʙᴀɴɴɪɴɢ ᴀʟʟ ᴜsᴇʀs ɪɴ {chat_name} ...**")
    
    total = 0
    success = 0
    async for users in client.get_chat_members(chat_id):
        total += 1
        try:
            await client.ban_chat_member(chat_id, users.user.id)
            success += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except Exception:
            pass

    await m.edit(f"**➻ ʙᴀɴᴀʟʟ ᴇxᴇᴄᴜᴛᴇᴅ !**\n\n**ᴛᴏᴛᴀʟ:** {total}\n**ʙᴀɴɴᴇᴅ:** {success}\n**ғᴀɪʟᴇᴅ:** {total - success}")


@app.on_message(cdx("unbanall"))
@sudo_users_only
async def unbanall(client, message):
    chat_id = message.chat.id
    chat_name = message.chat.title

    if len(message.command) > 1:
        try:
            chat = await client.get_chat(message.command[1])
            chat_id = chat.id
            chat_name = chat.title
        except Exception as e:
            return await eor(message, f"**❌ Error:**\n`{e}`")

    m = await eor(message, f"**➻ ᴜɴʙᴀɴɴɪɴɢ ᴀʟʟ ᴜsᴇʀs ɪɴ {chat_name} ...**")

    total = 0
    success = 0
    async for users in client.get_chat_members(chat_id, filter=ChatMembersFilter.BANNED):
        total += 1
        try:
            await client.unban_chat_member(chat_id, users.user.id)
            success += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except Exception:
            pass

    await m.edit(f"**➻ ᴜɴʙᴀɴᴀʟʟ ᴇxᴇᴄᴜᴛᴇᴅ !**\n\n**ᴛᴏᴛᴀʟ:** {total}\n**ᴜɴʙᴀɴɴᴇᴅ:** {success}\n**ғᴀɪʟᴇᴅ:** {total - success}")


__NAME__ = "Mass Ban"
__MENU__ = """
`.banall` <chat_id> - **ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.**
`.unbanall` <chat_id> - **ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.**
"""

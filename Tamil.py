import re
import os
from asyncio import gather, get_event_loop, sleep

from aiohttp import ClientSession
from pyrogram import Client, filters, idle
from Python_ARQ import ARQ

is_config = os.path.exists("config.py")
if is_config:
    from config import *
else:
    from config import *

Tamil = Client(
    ":memory:",
    api_id="8962397",
    api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
)

bot_id = int(bot_token.split(":")[0])
arq = None


async def TamilQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "ta"
        else (await arq.translate(query, "ta")).result.translatedText
    )
    resp = (await arq.Tamil(query, user_id)).result
    return (
        resp
        if LANGUAGE == "ta"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(TamilQuery(query, user_id), sleep(2))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, "cancel")

async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,} Tamil[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)



async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await Tamil.start()
    print(
        """
Possessing.....................
"""
    )



idle()


loop = get_event_loop()
loop.run_until_complete(main())

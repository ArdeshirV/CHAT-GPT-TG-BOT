#!/usr/bin/env python3
from pyrogram.client import Client
from pyrogram.types import Message
import os
os.environ['OPENAI_API_KEY'] = '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'

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo-0301",
#   messages=[
#     {"role": "user", "content": "write me trade solidity code"}
#   ]
# )

# print(completion.choices[0].message)


app=Client("gpt-sess",api_hash="7168e8bfff59cb5970faac852cd1bda6",api_id=841862,bot_token="1909721625:AAEiqU1kneYEoN4NB490GnCtHhNJuUEEf4k")

@app.on_message()
def all(bot:Client,msg:Message):
    if msg.text=="/start":
        bot.send_message(msg.chat.id,"hello")
    else:
        bot.send_message(msg.chat.id,"wait...")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": msg.text}
        ]
        )
        answer=completion.choices[0].message
        bot.send_message(msg.chat.id,answer.content)
app.run()

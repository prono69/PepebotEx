# For UniBorg
# By Priyam Kalra
# Syntax (.say <text_to_print>)
from uniborg.util import admin_cmd
from telethon.tl import functions, types
import time


@borg.on(admin_cmd(pattern="say ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    if not input:
    	abe = await event.get_reply_message()
    	input = abe.text
    strings = input.split()
    count = 0
    output = ""
    for _ in strings:
        output += f"{strings[count]}\n"
        count += 1
        await event.edit(output)
        time.sleep(0.25)

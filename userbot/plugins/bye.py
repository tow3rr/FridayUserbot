# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
import time

@borg.on(admin_cmd("bye", outgoing=True))
@borg.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    starkgang = await edit_or_reply(e, "Addio coglioni")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await starkgang.edit("`Sto uscendo dalla chat, fottetevi!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await starkgang.edit('`Smettila di trollare`')

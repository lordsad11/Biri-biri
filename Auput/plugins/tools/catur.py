from Auput import *


@Auput.on_message(filters.me & anjay("catur"))
async def _(client, message):
    await catur_cmd(client, message)

async def catur_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("GameFactoryBot")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)
